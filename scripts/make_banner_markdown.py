#!/usr/bin/env python3
"""
Create Markdown files from a CSV AND build a GeoJSON map from the same rows.

- Each row -> docs/banner/<number>_<slugified-title>_<date>.md
- Writes all CSV columns into YAML front matter.
- If target file already exists, the row is skipped (unless --overwrite).
- Body shows fields present in frontmatter with {{ page.meta.<key> }} or {{ page.meta['key'] }}.
- Picture-like columns are embedded as images using their {{ page.meta... }} values.
- Replace ":" with "-" in all frontmatter values EXCEPT for keys "bg-link" and "picture".
- Ensure 'description' is quoted and newlines encoded as "\n".

New:
- Builds a FeatureCollection GeoJSON at data/map.geojson (configurable via --geojson-out)
  mirroring the provided example schema:
  properties: nummer, title, picture, region, country, completed, missions, category,
              date, bg_link, description, length_km
  geometry: Point [lon, lat]

Usage:
  python make_banner_markdown.py --csv path/to/banner.csv --out docs/banner \
    [--overwrite] [--pad-width 6] [--geojson-out data/map.geojson]
"""
import argparse
import csv
import json
import os
import re
from datetime import datetime

# Keys that are treated as picture sources in the body (embedded as images)
PICTURE_KEYS = [
    "picture", "pictures", "image", "images", "img", "pic", "pic_url",
    "picture_url", "image_url", "bild", "bilder", "pictureurl", "imageurl"
]

# URL-like fields we don't list under Links if already treated as picture
URL_HINT_KEYS = set(PICTURE_KEYS)

# Keys that MUST NOT be sanitized (no ":" replacement)
EXCLUDED_SANITIZE_KEYS = {"bg-link", "picture"}

IDENTIFIER_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*$")

LAT_KEYS = ["lat", "latitude", "y", "breite", "breitengrad"]
LON_KEYS = ["lon", "lng", "long", "longitude", "x", "laenge", "länge", "laengengrad", "längengrad"]

# Property inference map: (target_property_name, candidate_source_keys_in_csv)
PROP_MAP = [
    ("nummer",        ["nummer", "number", "no", "id"]),
    ("title",         ["title", "titel", "name"]),
    ("picture",       list(PICTURE_KEYS)),
    ("region",        ["region", "city", "stadt", "ort"]),
    ("country",       ["country", "land"]),
    ("completed",     ["completed", "fertig", "gesamt", "sum"]),
    ("missions",      ["missions", "missionen", "anzahl_missionen", "missions_count"]),
    ("category",      ["category", "kategorie"]),
    ("date",          ["date", "datum", "year", "jahr"]),
    ("bg_link",       ["bg_link", "bg-link", "bannergress", "bannergress_url"]),
    ("description",   ["description", "beschreibung", "desc"]),
    ("length_km",     ["length_km", "lengthKMeters", "km", "dist_km", "length"]),
]

def jinja_meta(k: str) -> str:
    if IDENTIFIER_RE.fullmatch(k):
        return f"page.meta.{k}"
    safe = k.replace("'", "\\'")
    return f"page.meta['{safe}']"

def slugify(value: str) -> str:
    value = value.strip().lower()
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

def infer_field(row: dict, keys: list[str]) -> str:
    lower_map = {k.lower(): v for k, v in row.items()}
    for k in keys:
        if k.lower() in lower_map:
            val = str(lower_map[k.lower()] if lower_map[k.lower()] is not None else "").strip()
            if val:
                return val
    return ""

def yaml_escape(value: str) -> str:
    if value is None:
        return '""'
    s = str(value)
    if re.fullmatch(r"(true|false|null)", s, flags=re.IGNORECASE):
        need = True
    elif re.fullmatch(r"-?\d+(\.\d+)?", s):
        need = True
    else:
        need = False
        if (
            re.search(r"[\\:#{}\\[\\],&*!|>@`?-]", s)
            or s.startswith(" ")
            or s.endswith(" ")
            or "\n" in s
            or '"' in s
            or "'"
        ):
            need = True
    if need:
        s = s.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{s}"'
    return s

def is_urlish(value: str) -> bool:
    return isinstance(value, str) and value.strip().startswith(("http://", "https://"))

def sanitize_value(key: str, val: str) -> str:
    if not isinstance(val, str):
        val = str(val)
    if key.lower() in EXCLUDED_SANITIZE_KEYS:
        return val.strip()
    return val.replace(":", "-").strip()

def write_markdown(out_path: str, frontmatter: dict, ordered_fields: list[str]):
    lines = ["---"]
    for k in ordered_fields:
        raw_v = frontmatter.get(k, "")
        v = sanitize_value(k, raw_v)
        if k.lower() == "description":
            esc = v.replace("\\", "\\\\").replace('"', '\\"')
            esc = esc.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "\\n")
            lines.append(f'{k}: "{esc}"')
        else:
            lines.append(f"{k}: {yaml_escape(v)}")
    lines.append("---")
    lines.append("")

    title_key = next((cand for cand in ("title", "name", "titel") if cand in frontmatter and str(frontmatter[cand]).strip()), None)
    if title_key:
        lines.append(f"# {{{{ {jinja_meta(title_key)} }}}}")
    else:
        lines.append("# {{ page.meta.title | default('Untitled') }}")

    meta_line = []
    if "date" in frontmatter and str(frontmatter["date"]).strip():
        meta_line.append("**Datum:** {{ page.meta.date }}")
    elif "datum" in frontmatter and str(frontmatter["datum"]).strip():
        meta_line.append("**Datum:** {{ page.meta.datum }}")

    for loc_key in ("city","stadt","ort","location","place","country","land"):
        if loc_key in frontmatter and str(frontmatter[loc_key]).strip():
            meta_line.append(f"**{loc_key.capitalize()}:** {{{{ {jinja_meta(loc_key)} }}}}")

    if meta_line:
        lines.append("_" + " • ".join(meta_line) + "_\n")

    pic_keys_present = [k for k in ordered_fields if k.lower() in PICTURE_KEYS and str(frontmatter.get(k, "")).strip()]
    if pic_keys_present:
        lines.append("## Bild" if len(pic_keys_present)==1 else "## Bilder")
        for k in pic_keys_present:
            lines.append(f"![{{{{ {jinja_meta('title')} | default('Bild') }}}}]({{{{ {jinja_meta(k)} }}}})")
        lines.append("")

    link_lines = []
    for k in ordered_fields:
        if k.lower() in PICTURE_KEYS:
            continue
        val = frontmatter.get(k, "")
        if is_urlish(val):
            jm = jinja_meta(k)
            link_lines.append(f"- **{k}**: [{{{{ {jm} }}}}]({{{{ {jm} }}}})")
    if link_lines:
        lines.append("## Links")
        lines.extend(link_lines)
        lines.append("")

    info_lines = []
    for k in ordered_fields:
        if k.lower() in PICTURE_KEYS or k in ("title","name","titel","date","datum"):
            continue
        val = str(frontmatter.get(k, "")).strip()
        if not val or is_urlish(val):
            continue
        jm = jinja_meta(k)
        info_lines.append(f"- **{k}**: {{{{ {jm} }}}}")
    if info_lines:
        lines.append("## Infos")
        lines.extend(info_lines)
        lines.append("")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

def format_number_for_filename(num_raw: str, min_width: int) -> str:
    s = str(num_raw).strip()
    digits = re.sub(r"\D", "", s)
    if not digits:
        return s or "000000"
    width = max(min_width, len(digits))
    return digits.zfill(width)

def to_int_or_none(s: str):
    if s is None or str(s).strip() == "":
        return None
    try:
        return int(float(str(s).strip()))
    except Exception:
        digits = re.sub(r"[^0-9]", "", str(s))
        return int(digits) if digits else None

def to_float_or_none(s: str):
    if s is None or str(s).strip() == "":
        return None
    try:
        return float(str(s).replace(",", ".").strip())
    except Exception:
        return None

def build_feature(row: dict) -> dict | None:
    # Coordinates
    lat = to_float_or_none(infer_field(row, LAT_KEYS))
    lon = to_float_or_none(infer_field(row, LON_KEYS))
    if lat is None or lon is None:
        # No coordinates -> skip feature
        return None

    # Map CSV to target properties
    props = {}
    for target, candidates in PROP_MAP:
        val = infer_field(row, candidates)
        if target == "nummer":
            props["nummer"] = to_int_or_none(val)
        elif target in ("completed", "missions", "category"):
            props[target] = to_int_or_none(val)
        elif target == "date":
            # keep as year or ISO, not forcing conversion; if purely numeric -> int, else keep string
            yr = to_int_or_none(val)
            props["date"] = yr if yr is not None else (val if val else None)
        elif target == "length_km":
            # take as-is in km (do NOT divide by 1000)
            props["length_km"] = to_float_or_none(val)
        elif target == "bg_link":
            # normalize key name to bg_link
            props["bg_link"] = val if val else None
        else:
            props[target] = val if val else None

    # fallbacks for title/picture if missing
    if not props.get("title"):
        props["title"] = infer_field(row, ["title", "titel", "name"]) or ""
    if not props.get("picture"):
        props["picture"] = infer_field(row, list(PICTURE_KEYS)) or None

    # remove keys with None to keep output tidy
    props = {k: v for k, v in props.items() if v is not None}

    return {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [lon, lat]},
        "properties": props,
    }

def main():
    parser = argparse.ArgumentParser(description="Create Markdown files from CSV rows and build a GeoJSON map.")
    parser.add_argument("--csv", required=True, help="Path to input CSV file")
    parser.add_argument("--out", default="docs/banner", help="Output directory (default: docs/banner)")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing Markdown files")
    parser.add_argument("--pad-width", type=int, default=6, help="Minimum zero-pad width for the number prefix (default: 6)")
    parser.add_argument("--geojson-out", default="data/map.geojson", help="Output path for the generated GeoJSON (default: data/map.geojson)")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)
    os.makedirs(os.path.dirname(args.geojson_out), exist_ok=True)

    features = []

    with open(args.csv, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise SystemExit("CSV has no header row. Please include column names.")

        created, skipped, overwritten = 0, 0, 0

        for idx, row in enumerate(reader, start=1):
            # --- Filenames ---
            num_raw = infer_field(row, ["nummer", "number", "no", "id"]) or str(idx)
            num_padded = format_number_for_filename(num_raw, args.pad_width)
            title = infer_field(row, ["title", "titel", "name"]) or f"row-{idx}"
            date_raw = infer_field(row, ["date", "datum", "created", "when", "planned_date"])
            date_norm = normalize_date(date_raw)
            slug = slugify(title)
            filename = f"{num_padded}_{slug}_{date_norm}.md"
            out_path = os.path.join(args.out, filename)

            # --- Frontmatter construction ---
            ordered_fields = list(reader.fieldnames)
            frontmatter = {}
            for k in ordered_fields:
                val = row.get(k, "")
                if isinstance(val, str):
                    val = val.strip()
                frontmatter[k] = sanitize_value(k, val)

            # convenience fields
            if "title" not in frontmatter or not str(frontmatter.get("title","")).strip():
                if "titel" in frontmatter and str(frontmatter["titel"]).strip():
                    frontmatter["title"] = frontmatter["titel"]
                    if "title" not in ordered_fields:
                        ordered_fields.append("title")
            if date_raw and ("date" not in frontmatter or not str(frontmatter.get("date","")).strip()):
                frontmatter["date"] = date_norm
                if "date" not in ordered_fields:
                    ordered_fields.append("date")

            # --- Write Markdown (create/overwrite/skip) ---
            if os.path.exists(out_path):
                if args.overwrite:
                    write_markdown(out_path, frontmatter, ordered_fields)
                    overwritten += 1
                else:
                    skipped += 1
            else:
                write_markdown(out_path, frontmatter, ordered_fields)
                created += 1

            # --- Build Feature for GeoJSON (optional if coords available) ---
            feat = build_feature(row)
            if feat is not None:
                features.append(feat)

    # --- Write GeoJSON ---
    fc = {"type": "FeatureCollection", "features": features}
    with open(args.geojson_out, "w", encoding="utf-8") as jf:
        json.dump(fc, jf, ensure_ascii=False, indent=4)

    print(
        f"✅ Done.\n"
        f"  Markdown -> Created: {created}, Overwritten: {overwritten}, Skipped (exists): {skipped}. Output: {os.path.abspath(args.out)}\n"
        f"  GeoJSON  -> Features: {len(features)} written to: {os.path.abspath(args.geojson_out)}"
    )

if __name__ == "__main__":
    main()
