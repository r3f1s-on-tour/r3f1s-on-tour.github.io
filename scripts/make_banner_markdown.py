#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSV -> Markdown (Bannergress banners)
Variant B (neutral English template) + support for:
- missionDay => Yes/No via {{__VALYESNO:missionDay__}}
- notice => highlighted notice box (with <br>)
- Distance formatted to 2 decimals ({{__VAL2DP:lengthKMeters__}})
"""
import argparse, csv, json, os, re, sys
from datetime import datetime
from typing import List, Dict, Any, Optional

# optional jinja
try:
    import jinja2
    HAVE_JINJA = True
except Exception:
    HAVE_JINJA = False

# config
PICTURE_KEYS = [
    "picture","pictures","image","images","img","pic","pic_url",
    "picture_url","image_url","bild","bilder","pictureurl","imageurl"
]
EXCLUDED_SANITIZE_KEYS = {"bg-link","picture"}
URL_PREFIXES = ("http://","https://")
IDENTIFIER_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*$")

# utils
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

# template handling
_BLOCK_IF      = re.compile(r"\{\{__IF:([^}]+)__\}\}(.*?)\{\{__/IF__\}\}", re.DOTALL)
_BLOCK_IFANY   = re.compile(r"\{\{__IFANY:([^}]+)__\}\}(.*?)\{\{__/IFANY__\}\}", re.DOTALL)

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
    tpl = template_text
    meta = ctx["meta"]
    tpl = _expand_if_blocks(tpl, meta)

    # __VAL:key__
    for m in re.findall(r"\{\{__VAL:([^}]+)__\}\}", tpl):
        tpl = tpl.replace(f"{{{{__VAL:{m}__}}}}", str(meta.get(m, "")).strip())

    # __VALBR:key__  -> replaces \n with <br>
    for m in re.findall(r"\{\{__VALBR:([^}]+)__\}\}", tpl):
        val = str(meta.get(m, "")).strip().replace("\\n", "<br>")
        tpl = tpl.replace(f"{{{{__VALBR:{m}__}}}}", val)

    # __VAL2DP:key__ -> numeric 2 decimals
    for m in re.findall(r"\{\{__VAL2DP:([^}]+)__\}\}", tpl):
        raw = str(meta.get(m, "")).strip().replace(",", ".")
        try: val = f"{float(raw):.2f}"
        except Exception: val = raw
        tpl = tpl.replace(f"{{{{__VAL2DP:{m}__}}}}", val)

    # __VALYESNO:key__ -> Yes/No/blank
    for m in re.findall(r"\{\{__VALYESNO:([^}]+)__\}\}", tpl):
        val = str(meta.get(m, "")).strip().lower()
        yes = val in ("1","true","yes","y")
        no = val in ("0","false","no","n")
        out = "Yes" if yes else "No" if no or val else ""
        tpl = tpl.replace(f"{{{{__VALYESNO:{m}__}}}}", out)

    # __IMG:key__
    for m in re.findall(r"\{\{__IMG:([^}]+)__\}\}", tpl):
        url = str(meta.get(m, "")).strip()
        tpl = tpl.replace(f"{{{{__IMG:{m}__}}}}", f"![{meta.get('title','Image')}]({url})" if url else "")

    # static info
    tpl = tpl.replace("{{__TITLE__}}", str(meta.get("title") or meta.get("name") or meta.get("titel") or "Untitled"))
    tpl = tpl.replace("{{__DATE_DE__}}", fmt_date_de(meta.get("date") or meta.get("datum") or ""))
    tpl = tpl.replace("{{__CITY__}}", str(meta.get("city") or meta.get("stadt") or meta.get("ort") or ""))
    tpl = tpl.replace("{{__COUNTRY__}}", str(meta.get("country") or meta.get("land") or ""))
    tpl = tpl.replace("{{__NUMBER__}}", ctx["number_padded"])
    tpl = tpl.replace("{{__SLUG__}}", ctx["slug"])
    tpl = tpl.replace("{{__FILENAME__}}", ctx["filename"])
    return tpl.strip() + "\n"

def read_template(path: str) -> str:
    if not os.path.isfile(path): raise SystemExit(f"Template not found: {path}")
    with open(path, "r", encoding="utf-8") as f: return f.read()

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
    lines.append("---\n")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + body)

def yaml_escape(v: str) -> str:
    s = str(v)
    if not s: return '""'
    if any(x in s for x in [":","[","]","{","}","\\","\n","'","\""]):
        s = s.replace("\\","\\\\").replace('"','\\"')
        return f'"{s}"'
    return s

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--csv", required=True)
    p.add_argument("--out", default="docs/banner")
    p.add_argument("--overwrite", action="store_true")
    p.add_argument("--template", required=True)
    p.add_argument("--pad-width", type=int, default=6)
    args = p.parse_args()

    tpl = read_template(args.template)
    os.makedirs(args.out, exist_ok=True)

    with open(args.csv, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=1):
            num_raw = infer_field(row, ["nummer","number","no","id"]) or str(i)
            number_padded = format_number_for_filename(num_raw, args.pad_width)
            title = infer_field(row, ["title","titel","name"]) or f"row-{i}"
            date_raw = infer_field(row, ["date","datum","created","when","planned_date"])
            date_norm = normalize_date(date_raw)
            slug = slugify(title)
            filename = f"{number_padded}_{slug}_{date_norm}.md"
            out_path = os.path.join(args.out, filename)

            ordered_fields = list(reader.fieldnames)
            frontmatter = {k: sanitize_value(k, (row.get(k,"") or "").strip()) for k in ordered_fields}
            frontmatter["title"] = frontmatter.get("title") or frontmatter.get("titel") or title
            frontmatter["date"] = frontmatter.get("date") or date_norm

            ctx = {
                "meta": frontmatter,
                "number_padded": number_padded,
                "slug": slug,
                "filename": filename
            }
            body = render_placeholders(tpl, ctx)
            write_markdown(out_path, frontmatter, ordered_fields, body)
    print(f"✅ Markdown generated in {args.out}")

if __name__ == "__main__":
    main()
