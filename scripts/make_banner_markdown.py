#!/usr/bin/env python3
"""
Create Markdown files from a CSV, with rich *placeholder* templates (no Jinja required)
and optional full Jinja rendering.

- Each row -> docs/banner/<zero_padded_number>_<slugified-title>_<date>.md
- YAML front matter from CSV (with description quoted and \n escaped)
- ":" sanitized to "-" except for keys in EXCLUDED_SANITIZE_KEYS
- Zero-padding for number prefix (default 6)
- Template via --template
- Modes:
  * Default (no --template): auto-composed body
  * Placeholder mode (with --template): powerful non-Jinja placeholders (IF/EACH etc.)
  * Jinja mode (--template + --render-jinja): full Jinja with context

Usage:
  python make_banner_markdown.py --csv scripts/banner.csv --out docs/banner \
    [--overwrite] [--pad-width 6] [--template template/banner.md] [--render-jinja]
"""
import argparse
import csv
import json
import os
import re
from datetime import datetime
from typing import List, Dict, Tuple, Any, Optional

try:
    import jinja2  # optional
    HAVE_JINJA = True
except Exception:
    HAVE_JINJA = False

# ---------- Config ----------
PICTURE_KEYS = [
    "picture", "pictures", "image", "images", "img", "pic", "pic_url",
    "picture_url", "image_url", "bild", "bilder", "pictureurl", "imageurl"
]
EXCLUDED_SANITIZE_KEYS = {"bg-link", "picture"}
IDENTIFIER_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*$")
URL_PREFIXES = ("http://", "https://")

# ---------- Utils ----------
def slugify(value: str) -> str:
    value = (value or "").strip().lower()
    value = re.sub(r"[\s_]+", "-", value)
    value = re.sub(r"[^a-z0-9-]+", "", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "untitled"

def normalize_date(s: str) -> str:
    if not s:
        return "nodate"
    s = s.strip()
    fmts = [
        "%Y-%m-%d","%d.%m.%Y","%d.%m.%y","%Y.%m.%d",
        "%d/%m/%Y","%m/%d/%Y","%Y/%m/%d","%d-%m-%Y","%m-%d-%Y",
    ]
    try:
        return datetime.fromisoformat(s).date().isoformat()
    except Exception:
        pass
    for fmt in fmts:
        try:
            return datetime.strptime(s, fmt).date().isoformat()
        except Exception:
            continue
    digits = re.sub(r"[^0-9]", "", s)
    return digits if digits else slugify(s)

def fmt_date_de(iso_or_any: str) -> str:
    if not iso_or_any:
        return ""
    s = str(iso_or_any)
    try:
        dt = datetime.fromisoformat(s)
        return dt.strftime("%d.%m.%Y")
    except Exception:
        pass
    # fallback: best effort for typical formats
    for fmt in ("%Y-%m-%d","%d.%m.%Y","%Y.%m.%d"):
        try:
            return datetime.strptime(s, fmt).strftime("%d.%m.%Y")
        except Exception:
            pass
    return s

def infer_field(row: dict, keys: List[str]) -> str:
    lower_map = {k.lower(): v for k, v in row.items()}
    for k in keys:
        if k.lower() in lower_map:
            val = str(lower_map[k.lower()] or "").strip()
            if val:
                return val
    return ""

def yaml_escape(value: Any) -> str:
    if value is None:
        return '""'
    s = str(value)
    if re.fullmatch(r"(true|false|null)", s, flags=re.IGNORECASE):
        need = True
    elif re.fullmatch(r"-?\d+(\.\d+)?", s):
        need = True
    else:
        need = False
        if (re.search(r"[\\:#{}\[\],&*!|>@`?-]", s)
            or s.startswith(" ")
            or s.endswith(" ")
            or "\n" in s
            or '"' in s
            or "'"):
            need = True
    if need:
        s = s.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{s}"'
    return s

def is_urlish(value: Any) -> bool:
    return isinstance(value, str) and value.strip().startswith(URL_PREFIXES)

def sanitize_value(key: str, val: Any) -> str:
    s = "" if val is None else str(val)
    if key.lower() in EXCLUDED_SANITIZE_KEYS:
        return s.strip()
    return s.replace(":", "-").strip()

def format_number_for_filename(num_raw: str, min_width: int) -> str:
    s = str(num_raw or "").strip()
    digits = re.sub(r"\D", "", s)
    if not digits:
        return s or "000000"
    width = max(min_width, len(digits))
    return digits.zfill(width)

def jinja_meta(k: str) -> str:
    if IDENTIFIER_RE.fullmatch(k):
        return f"page.meta.{k}"
    safe = k.replace("'", "\\'")
    return f"page.meta['{safe}']"

# ---------- Default composed sections (for placeholder-fallbacks) ----------
def build_sections(frontmatter: Dict[str, str], ordered_fields: List[str]) -> Tuple[str, str, str, str, str]:
    # Title
    if any(k in frontmatter and str(frontmatter[k]).strip() for k in ("title", "name", "titel")):
        title_line = f"# {{{{ {jinja_meta('title')} | default('Untitled') }}}}"
    else:
        title_line = "# {{ page.meta.title | default('Untitled') }}"

    # Meta line
    meta_bits = []
    if frontmatter.get("date","").strip():
        meta_bits.append("**Datum:** {{ page.meta.date }}")
    elif frontmatter.get("datum","").strip():
        meta_bits.append("**Datum:** {{ page.meta.datum }}")
    for loc_key in ("city","stadt","ort","location","place","country","land"):
        if frontmatter.get(loc_key,"").strip():
            meta_bits.append(f"**{loc_key.capitalize()}:** {{{{ {jinja_meta(loc_key)} }}}}")
    meta_block = "_" + " • ".join(meta_bits) + "_\n" if meta_bits else ""

    # Pictures
    pic_keys_present = [k for k in ordered_fields if k.lower() in PICTURE_KEYS and str(frontmatter.get(k, "")).strip()]
    pictures_lines = []
    if pic_keys_present:
        pictures_lines.append("## Bild" if len(pic_keys_present) == 1 else "## Bilder")
        for k in pic_keys_present:
            pictures_lines.append(f"![{{{{ {jinja_meta('title')} | default('Bild') }}}}]({{{{ {jinja_meta(k)} }}}})")
        pictures_lines.append("")
    pictures_block = "\n".join(pictures_lines).strip()

    # Links
    link_lines = []
    for k in ordered_fields:
        if k.lower() in PICTURE_KEYS:
            continue
        val = frontmatter.get(k, "")
        if is_urlish(val):
            jm = jinja_meta(k)
            link_lines.append(f"- **{k}**: [{{{{ {jm} }}}}]({{{{ {jm} }}}})")
    links_block = ("## Links\n" + "\n".join(link_lines) + "\n").strip() if link_lines else ""

    # Infos
    info_lines = []
    for k in ordered_fields:
        if k.lower() in PICTURE_KEYS or k in ("title","name","titel","date","datum"):
            continue
        val = str(frontmatter.get(k, "")).strip()
        if not val or is_urlish(val):
            continue
        jm = jinja_meta(k)
        info_lines.append(f"- **{k}**: {{{{ {jm} }}}}")
    infos_block = ("## Infos\n" + "\n".join(info_lines) + "\n").strip() if info_lines else ""

    return title_line, meta_block.strip(), pictures_block, links_block, infos_block

# ---------- Template IO ----------
def read_template(path: Optional[str]) -> Optional[str]:
    if not path:
        return None
    if not os.path.isfile(path):
        raise SystemExit(f"Template not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# ---------- Placeholder Engine (no Jinja) ----------
_BLOCK_IF_RE = re.compile(r"\{\{__IF:([^}]+)__\}\}(.*?)\{\{__/IF__\}\}", re.DOTALL)
_BLOCK_IFNOT_RE = re.compile(r"\{\{__IFNOT:([^}]+)__\}\}(.*?)\{\{__/IFNOT__\}\}", re.DOTALL)
_BLOCK_EACH_PIC_RE = re.compile(r"\{\{__EACH_PICTURE__\}\}(.*?)\{\{__/EACH_PICTURE__\}\}", re.DOTALL)
_BLOCK_EACH_LINK_RE = re.compile(r"\{\{__EACH_LINK__\}\}(.*?)\{\{__/EACH_LINK__\}\}", re.DOTALL)
_BLOCK_EACH_INFO_RE = re.compile(r"\{\{__EACH_INFO__\}\}(.*?)\{\{__/EACH_INFO__\}\}", re.DOTALL)

def _truthy(meta: Dict[str, Any], key: str, pics: list, links: list, infos: list) -> bool:
    k = key.lower()
    if k == "pictures": return len(pics) > 0
    if k == "links": return len(links) > 0
    if k == "infos": return len(infos) > 0
    return bool(str(meta.get(key, "")).strip())

def _expand_if_blocks(tpl: str, meta: Dict[str, Any], pics, links, infos) -> str:
    # IF
    while True:
        m = _BLOCK_IF_RE.search(tpl)
        if not m: break
        key, inner = m.group(1), m.group(2)
        repl = inner if _truthy(meta, key, pics, links, infos) else ""
        tpl = tpl[:m.start()] + repl + tpl[m.end():]
    # IFNOT
    while True:
        m = _BLOCK_IFNOT_RE.search(tpl)
        if not m: break
        key, inner = m.group(1), m.group(2)
        repl = "" if _truthy(meta, key, pics, links, infos) else inner
        tpl = tpl[:m.start()] + repl + tpl[m.end():]
    return tpl

def _expand_each_block(tpl: str, regex, items, item_mapper) -> str:
    while True:
        m = regex.search(tpl)
        if not m: break
        inner = m.group(1)
        chunks = []
        for idx, it in enumerate(items, start=1):
            chunk = inner
            mapping = item_mapper(idx, it)
            for k, v in mapping.items():
                chunk = chunk.replace(k, v)
            chunks.append(chunk)
        tpl = tpl[:m.start()] + "".join(chunks) + tpl[m.end():]
    return tpl

def render_placeholders(template_text: str, ctx: Dict[str, Any]) -> str:
    tpl = template_text

    meta: Dict[str, Any] = ctx["meta"]
    number_padded = ctx["number_padded"]
    number_raw = ctx["number_raw"]
    slug = ctx["slug"]
    date_iso = ctx["date_norm"]
    filename = ctx["filename"]
    pics = ctx["pictures"]  # [{key,url}]
    links = ctx["links"]    # [{key,url}]
    infos = ctx["infos"]    # [{key,value}]

    # ---- IF / IFNOT blocks ----
    tpl = _expand_if_blocks(tpl, meta, pics, links, infos)

    # ---- EACH blocks ----
    def pic_mapper(idx, it):
        return {
            "{{__INDEX__}}": str(idx),
            "{{__KEY__}}": it["key"],
            "{{__URL__}}": it["url"],
        }
    def link_mapper(idx, it):
        return {
            "{{__INDEX__}}": str(idx),
            "{{__KEY__}}": it["key"],
            "{{__URL__}}": it["url"],
        }
    def info_mapper(idx, it):
        return {
            "{{__INDEX__}}": str(idx),
            "{{__KEY__}}": it["key"],
            "{{__VALUE__}}": it["value"],
        }

    tpl = _expand_each_block(tpl, _BLOCK_EACH_PIC_RE, pics, pic_mapper)
    tpl = _expand_each_block(tpl, _BLOCK_EACH_LINK_RE, links, link_mapper)
    tpl = _expand_each_block(tpl, _BLOCK_EACH_INFO_RE, infos, info_mapper)

    # ---- Scalar placeholders (core) ----
    replacements = {
        "{{__TITLE__}}": str(meta.get("title") or meta.get("name") or meta.get("titel") or "Untitled"),
        "{{__DATE__}}": str(meta.get("date") or meta.get("datum") or ""),
        "{{__DATE_ISO__}}": date_iso,
        "{{__DATE_DE__}}": fmt_date_de(meta.get("date") or meta.get("datum") or date_iso),
        "{{__CITY__}}": str(meta.get("city") or meta.get("stadt") or meta.get("ort") or ""),
        "{{__COUNTRY__}}": str(meta.get("country") or meta.get("land") or ""),
        "{{__LOCATION__}}": str(meta.get("location") or meta.get("place") or ""),
        "{{__NUMBER__}}": number_padded,
        "{{__NUMBER_RAW__}}": number_raw,
        "{{__SLUG__}}": slug,
        "{{__FILENAME__}}": filename,
        "{{__PICTURES__}}": "\n".join(f"![{meta.get('title','Bild')}]({p['url']})" for p in pics),
        "{{__LINKS__}}": "\n".join(f"- **{l['key']}**: [{l['url']}]({l['url']})" for l in links),
        "{{__INFOS__}}": "\n".join(f"- **{i['key']}**: {i['value']}" for i in infos),
        "{{__FIRST_PICTURE__}}": (pics[0]["url"] if pics else ""),
    }
    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    # ---- Parameterized scalar accessors ----
    # {{__VAL:key__}} raw meta value
    for m in re.findall(r"\{\{__VAL:([^}]+)__\}\}", tpl):
        v = str(meta.get(m, "")).strip()
        tpl = tpl.replace(f"{{{{__VAL:{m}__}}}}", v)

    # {{__LINK:key__}} -> meta[key] as URL (or blank)
    for m in re.findall(r"\{\{__LINK:([^}]+)__\}\}", tpl):
        url = str(meta.get(m, "")).strip()
        repl = f"[{url}]({url})" if is_urlish(url) else ""
        tpl = tpl.replace(f"{{{{__LINK:{m}__}}}}", repl)

    # {{__IMG:key__}} -> markdown image with meta[key]
    for m in re.findall(r"\{\{__IMG:([^}]+)__\}\}", tpl):
        url = str(meta.get(m, "")).strip()
        repl = f"![{meta.get('title','Bild')}]({url})" if url else ""
        tpl = tpl.replace(f"{{{{__IMG:{m}__}}}}", repl)

    return tpl.strip() + "\n"

# ---------- Jinja mode (optional) ----------
def jinja_env() -> "jinja2.Environment":
    env = jinja2.Environment(
        loader=jinja2.BaseLoader(),
        autoescape=False,
        undefined=jinja2.StrictUndefined,
    )
    env.filters["slugify"] = slugify
    env.filters["tojson"] = lambda x: json.dumps(x, ensure_ascii=False)
    def nl2br(s: Any) -> str:
        return ("" if s is None else str(s)).replace("\n", "<br>")
    env.filters["nl2br"] = nl2br
    def md_esc(s: Any) -> str:
        t = "" if s is None else str(s)
        return re.sub(r"([\\`*_{}\[\]()#+\-.!|])", r"\\\1", t)
    env.filters["md_esc"] = md_esc
    def fmt_date(val: Any, fmt: str = "%Y-%m-%d") -> str:
        if not val: return ""
        try: return datetime.fromisoformat(str(val)).strftime(fmt)
        except Exception: pass
        for f in ("%Y-%m-%d","%d.%m.%Y","%Y.%m.%d"):
            try: return datetime.strptime(str(val), f).strftime(fmt)
            except Exception: pass
        return str(val)
    env.globals["fmt_date"] = fmt_date
    env.globals["is_urlish"] = is_urlish
    return env

def render_with_jinja(template_text: str, ctx: dict) -> str:
    env = jinja_env()
    tmpl = env.from_string(template_text)
    return tmpl.render(**ctx).strip() + "\n"

# ---------- IO ----------
def write_markdown(out_path: str, frontmatter: dict, ordered_fields: list[str], body: str):
    fm_lines = ["---"]
    for k in ordered_fields:
        raw_v = frontmatter.get(k, "")
        v = sanitize_value(k, raw_v)
        if k.lower() == "description":
            esc = v.replace("\\", "\\\\").replace('"', '\\"')
            esc = esc.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "\\n")
            fm_lines.append(f'{k}: "{esc}"')
        else:
            fm_lines.append(f"{k}: {yaml_escape(v)}")
    fm_lines.append("---")
    fm_lines.append("")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(fm_lines) + body)

# ---------- Main ----------
def main():
    parser = argparse.ArgumentParser(description="Create Markdown files from CSV rows.")
    parser.add_argument("--csv", required=True, help="Path to input CSV file")
    parser.add_argument("--out", default="docs/banner", help="Output directory (default: docs/banner)")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing Markdown files")
    parser.add_argument("--pad-width", type=int, default=6, help="Minimum zero-pad width for the number prefix (default: 6)")
    parser.add_argument("--template", help="Path to a Markdown body template (e.g. template/banner.md)")
    parser.add_argument("--render-jinja", action="store_true", help="Render the template with Jinja (requires jinja2)")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)
    template_text = read_template(args.template)

    if args.render_jinja and not HAVE_JINJA:
        raise SystemExit("jinja2 is not installed. Run: pip install jinja2")

    with open(args.csv, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise SystemExit("CSV has no header row. Please include column names.")

        created, skipped, overwritten = 0, 0, 0

        for idx, row in enumerate(reader, start=1):
            num_raw = infer_field(row, ["nummer", "number", "no", "id"]) or str(idx)
            number_padded = format_number_for_filename(num_raw, args.pad_width)

            title = infer_field(row, ["title", "titel", "name"]) or f"row-{idx}"
            date_raw = infer_field(row, ["date", "datum", "created", "when", "planned_date"])
            date_norm = normalize_date(date_raw)
            slug = slugify(title)

            filename = f"{number_padded}_{slug}_{date_norm}.md"
            out_path = os.path.join(args.out, filename)

            ordered_fields = list(reader.fieldnames)
            frontmatter = {k: sanitize_value(k, (row.get(k, "") or "").strip()) for k in ordered_fields}

            if "title" not in frontmatter or not str(frontmatter.get("title","")).strip():
                if "titel" in frontmatter and str(frontmatter["titel"]).strip():
                    frontmatter["title"] = frontmatter["titel"]
                    if "title" not in ordered_fields:
                        ordered_fields.append("title")
            if date_raw and ("date" not in frontmatter or not str(frontmatter.get("date","")).strip()):
                frontmatter["date"] = date_norm
                if "date" not in ordered_fields:
                    ordered_fields.append("date")

            # Build lists for placeholder/Jinja context
            pics = [{"key": k, "url": str(frontmatter.get(k)).strip()}
                    for k in ordered_fields
                    if k.lower() in PICTURE_KEYS and str(frontmatter.get(k, "")).strip()]
            lnks = [{"key": k, "url": str(frontmatter.get(k)).strip()}
                    for k in ordered_fields
                    if k.lower() not in PICTURE_KEYS and is_urlish(frontmatter.get(k, ""))]
            infs = [{"key": k, "value": str(frontmatter.get(k)).strip()}
                    for k in ordered_fields
                    if k.lower() not in PICTURE_KEYS
                    and k not in ("title","name","titel","date","datum")
                    and str(frontmatter.get(k, "")).strip()
                    and not is_urlish(frontmatter.get(k, ""))]

            if template_text:
                if args.render_jinja:
                    ctx = {
                        "meta": frontmatter,
                        "ordered_fields": ordered_fields,
                        "number_padded": number_padded,
                        "number_raw": num_raw,
                        "slug": slug,
                        "date_norm": date_norm,
                        "filename": filename,
                        "pictures": pics,
                        "links": lnks,
                        "infos": infs,
                    }
                    body = render_with_jinja(template_text, ctx)
                else:
                    # --- Rich placeholder mode ---
                    ctx = {
                        "meta": frontmatter,
                        "ordered_fields": ordered_fields,
                        "number_padded": number_padded,
                        "number_raw": num_raw,
                        "slug": slug,
                        "date_norm": date_norm,
                        "filename": filename,
                        "pictures": pics,
                        "links": lnks,
                        "infos": infs,
                    }
                    body = render_placeholders(template_text, ctx)
            else:
                # Fallback: composed sections
                t, m, p, l, i = build_sections(frontmatter, ordered_fields)
                parts = [x for x in (t, m, p, l, i) if x]
                body = "\n\n".join(parts) + "\n"

            if os.path.exists(out_path):
                if args.overwrite:
                    write_markdown(out_path, frontmatter, ordered_fields, body)
                    overwritten += 1
                else:
                    skipped += 1
            else:
                write_markdown(out_path, frontmatter, ordered_fields, body)
                created += 1

    print(f"✅ Done. Created: {created}, Overwritten: {overwritten}, Skipped (exists): {skipped}. Output: {os.path.abspath(args.out)}")

if __name__ == "__main__":
    main()
