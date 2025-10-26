#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSV -> Markdown (Bannergress banners)

Features:
- CSV -> 1 Markdown pro Zeile (Dateiname: <padded-number>_<slug>_<date>.md)
- YAML Frontmatter: alle CSV-Spalten + Helper (slug, href, title-Aliasse)
- Spezielle Felder:
    * description + notice: immer in Anführungszeichen, '\n' -> '\\n'
    * notice: unterstützt Markdown-Links und nackte URLs (autolink) via {{__VALBRLINKS:notice__}}
- Zahl mit führenden Nullen (--pad-width)
- Titel-Aliasse: title, name, titel
- Helper: slug, href
- region->city Alias (falls city leer)
- Link-Spalten normalisiert: 'Trips' -> 'trips', 'Umap' -> 'umap'
- Template-Platzhalter:
    {{__VAL:key__}}, {{__VALBR:key__}}, {{__VAL2DP:key__}}, {{__VALYESNO:key__}},
    {{__VALBRLINKS:key__}}, {{__IMG:key__}},
    {{__IF:key__}}...{{__/IF__}}, {{__IFANY:a,b__}}...{{__/IFANY__}}

Usage:
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
# Niemals ":"-Sanitizing für diese Keys (und nie URLs generell)
EXCLUDED_SANITIZE_KEYS = {"bg-link", "picture", "notice", "description", "trips"}
URL_PREFIXES = ("http://","https://")
IDENTIFIER_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*$")

# -------- Utils ----------
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

def is_urlish(value: Any) -> bool:
    return isinstance(value, str) and value.strip().startswith(URL_PREFIXES)

def yaml_escape(value: Any) -> str:
    """YAML-safe: quote bei Sonderzeichen, insbesondere '#' immer quoten."""
    if value is None: return '""'
    s = str(value)
    # Hash erzwingt Quote (vermeidet YAML-Kommentar)
    if "#" in s:
        s = s.replace("\\","\\\\").replace('"','\\"')
        return f'"{s}"'
    # Typische Problemmuster
    need = False
    if re.fullmatch(r"(true|false|null)", s, flags=re.IGNORECASE) or re.fullmatch(r"-?\d+(\.\d+)?", s):
        need = True
    if (re.search(r"[\\:#{}\[\],&*!|>@`?-]", s) or s.startswith(" ") or s.endswith(" ") or "\n" in s or '"' in s or "'"):
        need = True
    if need:
        s = s.replace("\\","\\\\").replace('"','\\"')
        return f'"{s}"'
    return s

def sanitize_value(key: str, val: Any) -> str:
    """
    Ersetze ':' -> '-' zur YAML-Sicherheit, außer:
    - Keys in EXCLUDED_SANITIZE_KEYS
    - Werte, die wie URL aussehen (http/https)
    """
    s = "" if val is None else str(val)
    if key.lower() in EXCLUDED_SANITIZE_KEYS:
        return s.strip()
    if is_urlish(s):
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

def render_placeholders(template_text: str, ctx: Dict[str,Any], open_new_tab: bool = False) -> str:
    tpl  = template_text
    meta = ctx["meta"]

    tpl = _expand_if_blocks(tpl, meta)

    # __VAL
    for m in re.findall(r"\{\{__VAL:([^}]+)__\}\}", tpl):
        tpl = tpl.replace(f"{{{{__VAL:{m}__}}}}", str(meta.get(m, "")).strip())

    # __VALBR (Zeilenumbrüche)
    for m in re.findall(r"\{\{__VALBR:([^}]+)__\}\}", tpl):
        val = str(meta.get(m, "")).strip().replace("\\n", "<br>")
        tpl = tpl.replace(f"{{{{__VALBR:{m}__}}}}", val)

    # __VALBRLINKS (Zeilenumbrüche + Markdown-Links + Autolinks)
    for m in re.findall(r"\{\{__VALBRLINKS:([^}]+)__\}\}", tpl):
        raw = str(meta.get(m, "")).strip()
        html = raw.replace("\\n", "<br>")
        link_attr = ' target="_blank" rel="noopener"' if open_new_tab else ""

        # Markdown Links [text](url)
        def md_link_sub(match):
            text = match.group(1)
            url  = match.group(2)
            return f'<a href="{url}"{link_attr} style="color:#FFD500;text-decoration:underline;word-break:break-word;">{text}</a>'
        html = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", md_link_sub, html)

        # Autolink nackter URLs
        def auto_link_sub(match):
            url = match.group(0)
            return f'<a href="{url}"{link_attr} style="color:#FFD500;text-decoration:underline;word-break:break-word;">{url}</a>'
        html = re.sub(r"(?<!href=\")(?<!\])(?P<url>https?://[^\s<]+)", auto_link_sub, html)

        tpl = tpl.replace(f"{{{{__VALBRLINKS:{m}__}}}}", html)

    # __VAL2DP
    for m in re.findall(r"\{\{__VAL2DP:([^}]+)__\}\}", tpl):
        raw = str(meta.get(m, "")).strip().replace(",", ".")
        try: val = f"{float(raw):.2f}"
        except Exception: val = raw
        tpl = tpl.replace(f"{{{{__VAL2DP:{m}__}}}}", val)

    # __VALYESNO
    for m in re.findall(r"\{\{__VALYESNO:([^}]+)__\}\}", tpl):
        val = str(meta.get(m, "")).strip().lower()
        yes = val in ("1","true","yes","y")
        no  = val in ("0","false","no","n")
        out = "Yes" if yes else "No" if no or val else ""
        tpl = tpl.replace(f"{{{{__VALYESNO:{m}__}}}}", out)

    # __LINK & __IMG
    for m in re.findall(r"\{\{__LINK:([^}]+)__\}\}", tpl):
        url = str(meta.get(m, "")).strip()
        tpl = tpl.replace(f"{{{{__LINK:{m}__}}}}", f"[{url}]({url})" if is_urlish(url) else "")
    for m in re.findall(r"\{\{__IMG:([^}]+)__\}\}", tpl):
        url = str(meta.get(m, "")).strip()
        tpl = tpl.replace(f"{{{{__IMG:{m}__}}}}", f"![{meta.get('title','Image')}]({url})" if url else "")

    # Helfer (CITY bevorzugt region)
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
            # für Multiline interpretierbar speichern
            esc = v.replace("\\","\\\\").replace('"','\\"').replace("\r\n","\n").replace("\r","\n").replace("\n","\\n")
            lines.append(f'{k}: "{esc}"')
        else:
            lines.append(f"{k}: {yaml_escape(v)}")
    # Helper sicherstellen (falls nicht in CSV-Header)
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
    ap.add_argument("--notice-links-new-tab", action="store_true",
                    help="Open links inside notice in a new tab (default: same tab)")
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
            title_csv = infer_field(row, ["title","titel","name"]) or f"row-{idx}"
            date_raw  = infer_field(row, ["date","datum","created","when","planned_date"])
            date_norm = normalize_date(date_raw)
            slug_val  = slugify(title_csv)
            filename  = f"{number_padded}_{slug_val}_{date_norm}.md"
            out_path  = os.path.join(args.out, filename)

            ordered_fields = list(reader.fieldnames)
            fm = {k: sanitize_value(k, (row.get(k,"") or "").strip()) for k in ordered_fields}

            # Titel/Datum sicherstellen
            if not str(fm.get("title","")).strip():
                fm["title"] = title_csv
                if "title" not in ordered_fields: ordered_fields.append("title")
            if not str(fm.get("date","")).strip() and date_norm:
                fm["date"] = date_norm
                if "date" not in ordered_fields: ordered_fields.append("date")

            # Titel-Aliasse
            t = (fm.get("title") or fm.get("titel") or fm.get("name") or title_csv).strip()
            fm["title"] = t
            if not str(fm.get("name","")).strip():  fm["name"]  = t
            if not str(fm.get("titel","")).strip(): fm["titel"] = t

            # region -> city alias
            if str(fm.get("region","")).strip() and not str(fm.get("city","")).strip():
                fm["city"] = fm["region"]

            # Link-Key Normalisierung (Trips/Umap groß -> klein)
            if "Trips" in fm and "trips" not in fm and str(fm["Trips"]).strip():
                fm["trips"] = fm["Trips"]
            if "Umap" in fm and "umap" not in fm and str(fm["Umap"]).strip():
                fm["umap"] = fm["Umap"]

            # Helper
            fm["slug"] = fm.get("slug") or slug_val
            fm["href"] = fm.get("href") or f"banner/{number_padded}_{slug_val}_{date_norm}.md"

            # Render
            ctx = {
                "meta": fm,
                "number_padded": number_padded,
                "slug": slug_val,
                "filename": filename,
            }
            body = render_placeholders(tpl, ctx, open_new_tab=args.notice_links_new_tab)

            # Schreiben
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
