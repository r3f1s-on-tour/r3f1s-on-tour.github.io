#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a banner gallery page from a CSV.
(… unveränderte Kopfzeilen / Docstring …)
"""
import argparse, csv, os, re, sys, hashlib
from datetime import datetime
from typing import Any, Dict, List, Optional

URL_PREFIXES = ("http://", "https://")
PICTURE_KEYS = [
    "picture","pictures","image","images","img","pic","pic_url",
    "picture_url","image_url","bild","bilder","pictureurl","imageurl"
]
IDENTIFIER_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*$")

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

def infer(row: Dict[str, Any], keys: List[str]) -> str:
    lm = {k.lower(): (row.get(k) or "") for k in row}
    for k in keys:
        if k.lower() in lm:
            v = str(lm[k.lower()]).strip()
            if v:
                return v
    return ""

def first_picture(front: Dict[str, str], ordered_fields: List[str]) -> str:
    for k in ordered_fields:
        if k.lower() in PICTURE_KEYS:
            v = str(front.get(k, "")).strip()
            if v:
                return v
    return ""

def read_template(path: str) -> str:
    if not os.path.isfile(path):
        raise SystemExit(f"Template not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def _sha1(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()

def write_text(path: str, content: str, overwrite: bool, debug: bool):
    path = os.path.normpath(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            old = f.read()
        if old == content:
            dprint(debug, f"No change for {path} (identical content).")
            # Trotzdem als Erfolg melden, damit CI nicht abbricht:
            with open(path, "w", encoding="utf-8") as wf:
                wf.write(content)
            return

        if not overwrite:
            raise SystemExit(
                f"Output exists and differs: {path}\n"
                f"Tip: pass --overwrite or set BANNER_GALLERY_OVERWRITE=1"
            )
        dprint(debug, f"Overwriting {path} (old sha1={_sha1(old)} -> new sha1={_sha1(content)})")
    else:
        dprint(debug, f"Creating {path}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def format_number_for_filename(num_raw: str, min_width: int) -> str:
    s = str(num_raw or "").strip()
    digits = re.sub(r"\D","", s)
    if not digits: return s or "000000"
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

def build_card_html(href: str, img: str, title: str, date_de: str, city: str, country: str) -> str:
    meta_bits = []
    if date_de: meta_bits.append(date_de)
    if city:    meta_bits.append(city)
    if country: meta_bits.append(country)
    meta = " • ".join(meta_bits)
    return (
        f'<a class="gallery-card" href="{href}">\n'
        f'  <img src="{img}" alt="{title}">\n'
        f'  <div class="content">\n'
        f'    <h3>{title}</h3>\n'
        f'    <div class="gallery-meta">{meta}</div>\n'
        f'  </div>\n'
        f'</a>\n'
    )

def expand_each_banner(template_text: str, items: List[Dict[str, str]]) -> Optional[str]:
    m = re.search(r"\{\{__EACH_BANNER__\}\}(.*?)\{\{__/EACH_BANNER__\}\}", template_text, re.DOTALL)
    if not m:
        return None
    inner = m.group(1)
    chunks = []
    for it in items:
        chunk = inner
        for k, v in it.items():
            chunk = chunk.replace(f"{{{{__{k}__}}}}", v)
        chunks.append(chunk)
    return template_text[:m.start()] + "".join(chunks) + template_text[m.end():]

def main():
    p = argparse.ArgumentParser(description="Build banner gallery page from CSV")
    # NEW flags
    p.add_argument("--csv", help="Path to input CSV (or env BANNER_GALLERY_CSV)")
    p.add_argument("--out", default="docs/gallery/index.md", help="Output file (default: docs/gallery/index.md)")
    p.add_argument("--template", default="template/gallery.md", help="Template path (default: template/gallery.md)")
    p.add_argument("--pad-width", type=int, default=6, help="Zero-pad width for number prefix (default: 6)")
    p.add_argument("--overwrite", action="store_true", help="Overwrite output file if exists")
    p.add_argument("--debug", action="store_true", help="Verbose debug output")
    # LEGACY flags (compat)
    p.add_argument("--root", default=None, help="(legacy) site root; if --outfile present, out = root/outfile")
    p.add_argument("--banner_dir", default=None, help="(legacy) ignored (CSV is the source)")
    p.add_argument("--outfile", default=None, help="(legacy) single output file; overrides --out as <root>/<outfile>")
    p.add_argument("--verbose", action="store_true", help="(legacy) alias for --debug")
    p.add_argument("--force", action="store_true", help="(legacy) alias for --overwrite")
    args = p.parse_args()

    # Map legacy -> new
    if args.verbose and not args.debug:
        args.debug = True
    if args.force and not args.overwrite:
        args.overwrite = True
    if os.environ.get("BANNER_GALLERY_OVERWRITE", "").strip() in ("1","true","yes","on"):
        args.overwrite = True

    if args.outfile:
        root = args.root or "."
        args.out = os.path.join(root, args.outfile)

    # CSV required (allow env fallback)
    csv_path = args.csv or os.environ.get("BANNER_GALLERY_CSV")
    if not csv_path:
        raise SystemExit("error: --csv is required (or set env BANNER_GALLERY_CSV)")
    if not os.path.isfile(csv_path):
        raise SystemExit(f"CSV not found: {csv_path}")

    dprint(args.debug, f"overwrite={args.overwrite}, out={os.path.normpath(args.out)}")
    dprint(args.debug, f"template={args.template}")

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

    # Build items for gallery
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
        href = f"../banner/{md_filename}" if args.out.endswith("gallery/index.md") else f"banner/{md_filename}"

        items.append({
            "URL": href,
            "PICTURE": picture or "",
            "TITLE": title,
            "DATE_DE": date_de,
            "CITY": city,
            "COUNTRY": country,
        })

    # Load template
    tpl = read_template(args.template)

    # 1) Loop expansion
    expanded = expand_each_banner(tpl, items)
    if expanded is not None:
        out_text = expanded
    else:
        # 2) Replace <!-- GALLERY -->
        cards = []
        for it in items:
            cards.append(
                build_card_html(
                    href=it["URL"],
                    img=it["PICTURE"],
                    title=it["TITLE"],
                    date_de=it["DATE_DE"],
                    city=it["CITY"],
                    country=it["COUNTRY"],
                )
            )
        cards_html = "".join(cards)
        if "<!-- GALLERY -->" in tpl:
            out_text = tpl.replace("<!-- GALLERY -->", cards_html)
        else:
            out_text = tpl + "\n\n" + cards_html

    # Hide empty-state if cards exist
    if "<div class=\"gallery-empty\"" in out_text and "gallery-card" in out_text:
        out_text = out_text.replace('id="gallery-empty"', 'id="gallery-empty" style="display:none"')

    # Write output (with explicit overwrite handling)
    write_text(args.out, out_text, overwrite=args.overwrite, debug=args.debug)
    print(f"✅ Gallery written: {os.path.abspath(args.out)}")

if __name__ == "__main__":
    main()
