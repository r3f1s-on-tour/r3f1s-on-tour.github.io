#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSV -> Markdown (Bannergress banners)

- Reads a CSV and creates one Markdown page per row.
- Writes all CSV columns into YAML front matter (sanitizing ":" except for some keys).
- Special handling:
  * 'description' and 'notice' are always quoted and store newlines as "\\n".
  * One banner image (first matching picture-like column).
  * Zero-padded numeric prefix in filename (default width 6; --pad-width).
  * Title aliases ensured: title, name, titel.
  * Always writes slug and href into front matter (useful for overview pages).
  * Region/City: if 'region' is given and 'city' is empty, city is set to region.
    Placeholders also prefer region where applicable.

- Template system (no Jinja needed):
  {{__VAL:key__}}        → value
  {{__VALBR:key__}}      → value with "\\n" rendered as <br>
  {{__VAL2DP:key__}}     → numeric value formatted with 2 decimals
  {{__VALYESNO:key__}}   → "Yes"/"No" for truthy/falsy values (1/0, true/false, yes/no)
  {{__IMG:key__}}        → Markdown image if url present
  {{__IF:key__}} ... {{__/IF__}}            → conditional block if key has a value
  {{__IFANY:a,b__}} ... {{__/IFANY__}}      → block if any of the given keys has a value

- English UI text expected in the template file (see template/banner.md).

Usage example:
  python scripts/make_banner_markdown.py \
    --csv scripts/banner.csv \
    --out docs/banner \
    --template template/banner.md \
    --overwrite
"""
import argparse, csv, os, re, sys
from datetime import datetime
from typing import List, Dict, Any

# -------- Config ----------
PICTURE_KEYS = [
    "picture","pictures","image","images","img","pic","pic_url",
    "picture_url","image_url","bild","bilder","pictureurl","imageurl"
]
EXCLUDED_SANITIZE_KEYS = {"bg-link","picture"}  # do not replace ":" in these
URL_PREFIXES = ("http://","https://")
IDENTIFIER_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*$")

# -------- Utils ----------
def dprint(enabled: bool, *args):
    if enabled:
        print("[DEBUG]", *args, file=sys.stderr)

def slugify(value: str) -> str:
    value = (value or "").strip().lower()
    value = re.sub(r"[\s_]+","-", value)
    value = re.sub(r"[^a-z0-9-]+","", value)
    value = re.sub(r"-{2,}","-", value).strip("-")
    return value or "untitled"

def normalize_date(s: str) -> str:
    if not s: return "nodate"
    s = s.strip()
    fmts = ["%Y-%m-%d","%d.%m.%Y","%d.%m.%y","%Y.%m.%d","%d/%m/%Y","%m/%d/%Y","%Y/%m/%d","%d-%m-%Y","%m-%d-%Y"]
    try:
        return datetime.fromisoformat(s).date().isoformat()
    except Exception:
        pass
    for fmt in fmts:
        try:
            return datetime.strptime(s, fmt).date().isoformat()
        except Exception:
            continue
    digits = re.sub(r"[^0-9]","", s)
    return digits if digits else slugify(s)

def fmt_date_de(iso_or_any: str) -> str:
    if not iso_or_any: return ""
    s = str(iso_or_any)
    try:
        return datetime.fromisoformat(s).strftime("%d.%m.%Y")
    except Exception:
        pass
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
    if value is None: return '""'
    s = str(value)
    if re.fullmatch(r"(true|false|null)", s, flags=re.IGNORECASE) or re.fullmatch(r"-?\d+(\.\d+)?", s):
        need = True
    else:
        need = bool(
            re.search(r"[\\:#{}\[\],&*!|>@`?-]", s)
            or s.startswith(" ") or s.endswith(" ")
            or "\n" in s or '"' in s or "'"
        )
    if need:
        s = s.replace("\\","\\\\").replace('"','\\"')
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
    digits = re.sub(r"\D","", s)
    if not digits: return s or "000000"
    width = max(min_width, len(digits))
    return digits.zfill(width)

# -------- Template engine ----------
_BLOCK_IF    = re.compile(r"\{\{__IF:([^}]+)__\}\}(.*?)\{\{__/IF__\}\}", re.DOTALL)
_BLOCK_IFANY = re.compile(r"\{\{__IFANY:([^}]+)__\}\}(.*?)\{\{__/IFANY__\}\}", re.DOTALL)

def _truthy(meta: Dict[str,Any], key: str) -> bool:
    return bool(str(meta.get(key, "")).strip())

def _expand_if_blocks(tpl: str, meta: Dict[str,Any]) -> str:
    while True:
        m = _BLOCK_IF.search(tpl)
        if not m: break
        key, inner = m.group(1), m.group(2)
        tpl = tpl[:m.start()] + (inner if _truthy(meta, key) else "") + tpl[m.end():]
    while True:
        m = _BLOCK_IFANY.search(tpl)
        if not m: break
        keys = [k.strip() for k in m.group(1).split(",") if k.strip()]
        inner = m.group(2)
        cond = any(_truthy(meta, k) for k in keys)
        tpl = tpl[:m.start()] + (inner if cond else "") + tpl[m.end():]
    return tpl

def render_placeholders(template_text: str, ctx: Dict[str,Any]) -> str:
    tpl  = template_text
    meta = ctx["meta"]

    # conditions
    tpl = _expand_if_blocks(tpl, meta)

    # values
    for m in re.findall(r"\{\{__VAL:([^}]+)__\}\}", tpl):
        tpl = tpl.replace(f"{{{{__VAL:{m}__}}}}", str(meta.get(m, "")).strip())

    for m in re.findall(r"\{\{__VALBR:([^}]+)__\}\}", tpl):
        val = str(meta.get(m, "")).strip().replace("\\n", "<br>")
        tpl = tpl.replace(f"{{{{__VALBR:{m}__}}}}", val)

    for m in re.findall(r"\{\{__VAL2DP:([^}]+)__\}\}", tpl):
        raw = str(meta.get(m, "")).strip().replace(",", ".")
        try: val = f"{float(raw):.2f}"
        except Exception: val = raw
        tpl = tpl.replace(f"{{{{__VAL2DP:{m}__}}}}", val)

    for m in re.findall(r"\{\{__VALYESNO:([^}]+)__\}\}", tpl):
        val = str(meta.get(m, "")).strip().lower()
        yes = val in ("1","true","yes","y")
        no  = val in ("0","false","no","n")
        out = "Yes" if yes else "No" if no or val else ""
        tpl = tpl.replace(f"{{{{__VALYESNO:{m}__}}}}", out)

    for m in re.findall(r"\{\{__LINK:([^}]+)__\}\}", tpl):
        url = str(meta.get(m, "")).strip()
        tpl = tpl.replace(f"{{{{__LINK:{m}__}}}}", f"[{url}]({url})" if is_urlish(url) else "")

    for m in re.findall(r"\{\{__IMG:([^}]+)__\}\}", tpl):
        url = str(meta.get(m, "")).strip()
        tpl = tpl.replace(f"{{{{__IMG:{m}__}}}}", f"![{meta.get('title','Image')}]({url})" if url else "")

    # helpers (prefer region for CITY placeholder)
    tpl = tpl.replace("{{__TITLE__}}",   str(meta.get("title") or meta.get("name") or meta.get("titel") or "Untitled"))
    tpl = tpl.replace("{{__DATE_DE__}}", fmt_date_de(meta.get("date") or meta.get("datum") or ""))
    tpl = tpl.replace("{{__CITY__}}",    str(meta.get("region") or meta.get("city") or meta.get("stadt") or meta.get("ort") or ""))
    tpl = tpl.replace("{{__COUNTRY__}}", str(meta.get("country") or meta.get("land") or ""))
    tpl = tpl.replace("{{__NUMBER__}}",  ctx["number_padded"])
    tpl = tpl.replace("{{__SLUG__}}",    ctx["slug"])
    tpl = tpl.replace("{{__FILENAME__}}",ctx["filename"])
    return tpl.strip() + "\n"

# -------- IO ----------
def read_template(path: str) -> str:
    if not os.path.isfile(path):
        raise SystemExit(f"Template not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_markdown(out_path: str, fm: dict, ordered: list[str], body: str):
    lines = ["---"]
    for k in ordered:
        raw = fm.get(k, "")
        v = sanitize_value(k, raw)
        if k.lower() in {"description", "notice"}:
            esc = v.replace("\\","\\\\").replace('"','\\"').replace("\r\n","\n").replace("\r","\n").replace("\n","\\n")
            lines.append(f'{k}: "{esc}"')
        else:
            lines.append(f"{k}: {yaml_escape(v)}")
    # also ensure these helper fields are present even if not in CSV header
    if "slug" not in ordered:   lines.append(f"slug: {yaml_escape(fm.get('slug',''))}")
    if "href" not in ordered:   lines.append(f"href: {yaml_escape(fm.get('href',''))}")
    if "name" not in ordered:   lines.append(f"name: {yaml_escape(fm.get('name',''))}")
    if "titel" not in ordered:  lines.append(f"titel: {yaml_escape(fm.get('titel',''))}")
    lines.append("---\n")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + body)

# -------- Main ----------
def main():
    ap = argparse.ArgumentParser(description="CSV -> Markdown generator (Banner)")
    ap.add_argument("--csv", required=True, help="Path to input CSV")
    ap.add_argument("--out", default="docs/banner", help="Output directory")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    ap.add_argument("--pad-width", type=int, default=6, help="Zero-pad width for number prefix")
    ap.add_argument("--template", required=True, help="Markdown template path")
    ap.add_argument("--debug", action="store_true")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    tpl = read_template(args.template)

    with open(args.csv, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise SystemExit("CSV has no header row. Please include column names.")

        created = overwritten = skipped = 0

        for idx, row in enumerate(reader, start=1):
            num_raw = infer_field(row, ["nummer","number","no","id"]) or str(idx)
            number_padded = format_number_for_filename(num_raw, args.pad_width)

            # core fields from CSV
            title_csv = infer_field(row, ["title","titel","name"]) or f"row-{idx}"
            date_raw  = infer_field(row, ["date","datum","created","when","planned_date"])
            date_norm = normalize_date(date_raw)
            slug_val  = slugify(title_csv)
            filename  = f"{number_padded}_{slug_val}_{date_norm}.md"
            out_path  = os.path.join(args.out, filename)

            # front matter straight from CSV (sanitized)
            ordered_fields = list(reader.fieldnames)
            fm = {k: sanitize_value(k, (row.get(k,"") or "").strip()) for k in ordered_fields}

            # ensure title/date
            if not str(fm.get("title","")).strip():
                fm["title"] = title_csv
                if "title" not in ordered_fields: ordered_fields.append("title")
            if not str(fm.get("date","")).strip() and date_norm:
                fm["date"] = date_norm
                if "date" not in ordered_fields: ordered_fields.append("date")

            # title aliases
            t = (fm.get("title") or fm.get("titel") or fm.get("name") or title_csv).strip()
            fm["title"] = t
            if not str(fm.get("name","")).strip():  fm["name"]  = t
            if not str(fm.get("titel","")).strip(): fm["titel"] = t

            # region -> city alias if city empty
            if str(fm.get("region","")).strip() and not str(fm.get("city","")).strip():
                fm["city"] = fm["region"]

            # helpers
            fm["slug"] = fm.get("slug") or slug_val
            fm["href"] = fm.get("href") or f"banner/{number_padded}_{slug_val}_{date_norm}.md"

            # render body via simple placeholders
            ctx = {
                "meta": fm,
                "number_padded": number_padded,
                "slug": slug_val,
                "filename": filename,
            }
            body = render_placeholders(tpl, ctx)

            if os.path.exists(out_path):
                if args.overwrite:
                    write_markdown(out_path, fm, ordered_fields, body)
                    overwritten += 1
                else:
                    skipped += 1
            else:
                write_markdown(out_path, fm, ordered_fields, body)
                created += 1

    print(f"✅ Done. Created: {created}, Overwritten: {overwritten}, Skipped: {skipped}. Output: {os.path.abspath(args.out)}")

if __name__ == "__main__":
    main()
