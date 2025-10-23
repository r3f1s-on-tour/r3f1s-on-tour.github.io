#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a banner gallery page from a CSV as a single-column HTML gallery.

- Default output: docs/banner/gallery.md
- Images render via <a><img></a> (reliable inside HTML blocks).
- Rows without picture are skipped (no empty boxes).
- Links computed relative to output location; supports directory URLs.

Overwrite controls:
  --overwrite | legacy --force | env BANNER_GALLERY_OVERWRITE=1

Template support:
  1) {{__EACH_BANNER__}} ... {{__/EACH_BANNER__}} with placeholders:
     {{__URL__}}, {{__PICTURE__}}, {{__TITLE__}}, {{__DATE_DE__}}, {{__CITY__}}, {{__COUNTRY__}}
  2) <!-- GALLERY --> placeholder (safe replacement; strips <p> wrapper)
"""

import argparse, csv, os, re, sys, hashlib
from datetime import datetime
from typing import Any, Dict, List, Optional

PICTURE_KEYS = [
    "picture","pictures","image","images","img","pic","pic_url",
    "picture_url","image_url","bild","bilder","pictureurl","imageurl"
]

# -------------------- utils --------------------

def dprint(enabled: bool, *args):
    if enabled:
        print("[GALLERY DEBUG]", *args, file=sys.stderr)

def slugify(value: str) -> str:
    value = (value or "").strip().lower()
    value = re.sub(r"[\s_]+","-", value)
    value = re.sub(r"[^a-z0-9-]+","", value)
    value = re.sub(r"-{2,}","-", value).strip("-")
    return value or "untitled"

def normalize_date(s: str) -> str:
    if not s: return "nodate"
    s = s.strip()
    fmts = ["%Y-%m-%d","%d.%m.%Y","%d.%m.%y","%Y.%m.%d","%d/%m/%Y","%m/%d/%Y",
            "%Y/%m/%d","%d-%m-%Y","%m-%d-%Y"]
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

def infer(row: Dict[str, Any], keys: List[str]) -> str:
    lm = {k.lower(): (row.get(k) or "") for k in row}
    for k in keys:
        if k.lower() in lm:
            v = str(lm[k.lower()]).strip()
            if v:
                return v
    return ""

def sha1(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()

def write_text(path: str, content: str, overwrite: bool, debug: bool):
    path = os.path.normpath(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            old = f.read()
        if old == content and not overwrite:
            dprint(debug, f"Identical content; leaving {path} as-is.")
            return
        if not overwrite:
            raise SystemExit(
                f"Output exists and differs: {path}\n"
                f"Pass --overwrite or set BANNER_GALLERY_OVERWRITE=1"
            )
        dprint(debug, f"Overwriting {path} (old sha1={sha1(old)} -> new sha1={sha1(content)})")
    else:
        dprint(debug, f"Creating {path}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def format_number_for_filename(num_raw: str, min_width: int) -> str:
    s = str(num_raw or "").strip()
    digits = re.sub(r"\D", "", s)
    if not digits:
        return s or "000000"
    width = max(min_width, len(digits))
    return digits.zfill(width)

def build_banner_filename(row: Dict[str, Any], idx: int, pad_width: int) -> str:
    num_raw = infer(row, ["nummer","number","no","id"]) or str(idx)
    num_padded = format_number_for_filename(num_raw, pad_width)
    title = infer(row, ["title","titel","name"]) or f"row-{idx}"
    date_raw = infer(row, ["date","datum","created","when","planned_date"])
    date_norm = normalize_date(date_raw)
    slug = slugify(title)
    return f"{num_padded}_{slug}_{date_norm}.md"

def read_template(path: str) -> str:
    if not os.path.isfile(path):
        raise SystemExit(f"Template not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# -------------------- rendering --------------------

def expand_each_banner(template_text: str, items: List[Dict[str, str]]) -> Optional[str]:
    """
    Expand {{__EACH_BANNER__}} ... {{__/EACH_BANNER__}} for items that have pictures.
    Supported placeholders:
      {{__URL__}}, {{__PICTURE__}}, {{__TITLE__}}, {{__DATE_DE__}}, {{__CITY__}}, {{__COUNTRY__}}
    """
    m = re.search(r"\{\{__EACH_BANNER__\}\}(.*?)\{\{__/EACH_BANNER__\}\}", template_text, re.DOTALL)
    if not m:
        return None
    inner = m.group(1)
    chunks = []
    for it in items:
        if not it["PICTURE"]:
            continue
        chunk = inner
        for k, v in it.items():
            chunk = chunk.replace(f"{{{{__{k}__}}}}", v)
        chunks.append(chunk)
    return template_text[:m.start()] + "".join(chunks) + template_text[m.end():]

def render_html_gallery(items: List[Dict[str, str]]) -> str:
    """
    Robust HTML rendering: one <p><a><img></a></p> per banner (skips missing pictures).
    """
    lines = []
    for it in items:
        if not it["PICTURE"]:
            continue
        title = (it["TITLE"] or "").replace('"', '&quot;')
        lines.append(f'<p><a href="{it["URL"]}"><img src="{it["PICTURE"]}" alt="{title}"></a></p>')
    return ("\n".join(lines) + "\n") if lines else "\n"

def compute_href(stem: str, out_path: str, directory_urls: bool) -> str:
    """
    If output is docs/banner/gallery.md  -> './<stem>/' or './<stem>.md'
    If output is docs/gallery/index.md   -> '../banner/<stem>/' or '../banner/<stem>.md'
    Else                                 -> 'banner/<stem>/' or 'banner/<stem>.md'
    """
    out_dir = os.path.normpath(os.path.dirname(out_path))
    tail = out_dir.replace("\\", "/").split("/")[-1]
    suffix = "/" if directory_urls else ".md"

    if tail == "banner":
        return f"./{stem}{suffix}"
    if out_path.replace("\\", "/").endswith("docs/gallery/index.md") or tail == "gallery":
        return f"../banner/{stem}{suffix}"
    return f"banner/{stem}{suffix}"

# -------------------- main --------------------

def main():
    p = argparse.ArgumentParser(description="Build banner gallery page from a CSV (HTML, 1 column, full width)")
    # New flags
    p.add_argument("--csv", help="Path to input CSV (or env BANNER_GALLERY_CSV)")
    p.add_argument("--out", default="docs/banner/gallery.md", help="Output file (default: docs/banner/gallery.md)")
    p.add_argument("--template", default="template/gallery.md", help="Template path (default: template/gallery.md)")
    p.add_argument("--pad-width", type=int, default=6, help="Zero-pad width for number prefix (default: 6)")
    p.add_argument("--overwrite", action="store_true", help="Overwrite output file if exists")
    p.add_argument("--debug", action="store_true", help="Verbose debug output")
    p.add_argument("--no-skip-missing-pictures", action="store_true",
                   help="Include entries even if picture is missing (not recommended)")
    p.add_argument("--no-directory-urls", action="store_true",
                   help="Link to '<stem>.md' instead of '<stem>/'")
    # Legacy flags
    p.add_argument("--root", default=None, help="(legacy) site root; with --outfile => out = root/outfile")
    p.add_argument("--banner_dir", default=None, help="(legacy) ignored")
    p.add_argument("--outfile", default=None, help="(legacy) single output file; maps to --out")
    p.add_argument("--verbose", action="store_true", help="(legacy) alias for --debug")
    p.add_argument("--force", action="store_true", help="(legacy) alias for --overwrite")
    args = p.parse_args()

    # Map legacy/env
    if args.verbose and not args.debug:
        args.debug = True
    if args.force:
        args.overwrite = True
    if os.environ.get("BANNER_GALLERY_OVERWRITE", "").strip().lower() in ("1","true","yes","on"):
        args.overwrite = True
    if args.outfile:
        root = args.root or "."
        args.out = os.path.join(root, args.outfile)

    # CSV
    csv_path = args.csv or os.environ.get("BANNER_GALLERY_CSV")
    if not csv_path:
        raise SystemExit("error: --csv is required (or set env BANNER_GALLERY_CSV)")
    if not os.path.isfile(csv_path):
        raise SystemExit(f"CSV not found: {csv_path}")

    dprint(args.debug, f"out={args.out} overwrite={args.overwrite} template={args.template} directory_urls={not args.no_directory_urls}")

    # Read CSV
    rows: List[Dict[str, Any]] = []
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise SystemExit("CSV has no header row. Please include column names.")
        fieldnames = list(reader.fieldnames)
        for row in reader:
            rows.append(row)

    dprint(args.debug, f"Loaded {len(rows)} rows from {csv_path}")

    # Build items
    items: List[Dict[str, str]] = []
    for idx, row in enumerate(rows, start=1):
        title = infer(row, ["title","titel","name"]) or f"row-{idx}"
        date_raw = infer(row, ["date","datum","created","when","planned_date"])
        date_iso = normalize_date(date_raw)
        date_de  = fmt_date_de(date_iso)
        city     = infer(row, ["city","stadt","ort","location","place"])
        country  = infer(row, ["country","land"])

        picture = ""
        for k in fieldnames:
            if k.lower() in PICTURE_KEYS:
                val = str(row.get(k,"")).strip()
                if val:
                    picture = val
                    break

        md_filename = build_banner_filename(row, idx, args.pad_width)
        stem = md_filename[:-3]  # drop .md
        href = compute_href(stem, args.out, directory_urls=not args.no_directory_urls)

        if picture or args.no_skip_missing_pictures:
            items.append({
                "URL": href,
                "PICTURE": picture or "",
                "TITLE": title,
                "DATE_DE": date_de,
                "CITY": city,
                "COUNTRY": country,
            })
        else:
            dprint(args.debug, f"Skip row {idx} ('{title}') because no picture found.")

    # Render gallery HTML
    gallery_html = render_html_gallery(items)

    # Apply template if present
    out_text = gallery_html
    if os.path.isfile(args.template):
        tpl = read_template(args.template)
        # Prefer EACH block
        expanded = expand_each_banner(tpl, items)
        if expanded is not None:
            out_text = expanded
        else:
            # Replace <!-- GALLERY -->; strip possible <p> wrappers first
            cleaned_tpl = re.sub(
                r"<p>\s*<!--\s*GALLERY\s*-->\s*</p>",
                "<!-- GALLERY -->",
                tpl,
                flags=re.IGNORECASE,
            )
            if "<!-- GALLERY -->" in cleaned_tpl:
                out_text = cleaned_tpl.replace("<!-- GALLERY -->", "\n" + gallery_html + "\n")
            else:
                out_text = cleaned_tpl.rstrip() + "\n\n" + gallery_html

    # Write
    write_text(args.out, out_text, overwrite=args.overwrite, debug=args.debug)
    print(f"✅ Gallery written: {os.path.abspath(args.out)}")

if __name__ == "__main__":
    main()
