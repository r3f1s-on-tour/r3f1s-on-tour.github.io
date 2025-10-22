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

GeoJSON:
- Builds FeatureCollection at data/map.geojson (configurable via --geojson-out).
- Detects coordinates in many column name variants (incl. startLatitude/startLongitude) + combined formats.
- --include-missing-geometry includes features without coords (geometry=null).
- --lat-key/--lon-key can force columns. --debug-geo prints skip reasons.

Usage:
  python make_banner_markdown.py --csv scripts/banner.csv --out docs/banner \
    [--overwrite] [--pad-width 6] [--geojson-out data/map.geojson] \
    [--lat-key LAT] [--lon-key LON] [--include-missing-geometry] [--debug-geo]
"""
import argparse
import csv
import json
import os
import re
from datetime import datetime
from typing import Optional, Tuple, Any

# --- Configs ---
PICTURE_KEYS = [
    "picture","pictures","image","images","img","pic","pic_url",
    "picture_url","image_url","bild","bilder","pictureurl","imageurl"
]
URL_HINT_KEYS = set(PICTURE_KEYS)
EXCLUDED_SANITIZE_KEYS = {"bg-link", "picture"}
IDENTIFIER_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*$")

# Canonical latitude/longitude keys (lowercased); includes startLatitude/startLongitude
LAT_KEYS_CANON = [
    "lat","latitude","y","breite","breitengrad","gps_lat","geo_lat",
    "lat_dd","lat_deg","latitude_dd","latitude_deg",
    "startLatitude",  # <— added
]
LON_KEYS_CANON = [
    "lon","lng","long","longitude","x","laenge","länge","laengengrad","längengrad",
    "gps_lon","geo_lon","lon_dd","lon_deg","longitude_dd","longitude_deg",
    "startLongitude", # <— added
]
COMBINED_COORD_KEYS = [
    "coords","coordinates","coordinate","coord","location","geo",
    "geopoint","point","centroid","wkt"
]

PROP_MAP = [
    ("nummer",      ["nummer","number","no","id"]),
    ("title",       ["title","titel","name"]),
    ("picture",     list(PICTURE_KEYS)),
    ("region",      ["region","city","stadt","ort"]),
    ("country",     ["country","land"]),
    ("completed",   ["completed","fertig","gesamt","sum"]),
    ("missions",    ["missions","missionen","anzahl_missionen","missions_count"]),
    ("category",    ["category","kategorie"]),
    ("date",        ["date","datum","year","jahr"]),
    ("bg_link",     ["bg_link","bg-link","bannergress","bannergress_url"]),
    ("description", ["description","beschreibung","desc"]),
    ("length_km",   ["length_km","lengthKMeters","km","dist_km","length"]),
]

# --- Helpers ---
def jinja_meta(k: str) -> str:
    if IDENTIFIER_RE.fullmatch(k):
        return f"page.meta.{k}"
    return f"page.meta['{k.replace(\"'\",\"\\\\'\")}']"

def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[\s_]+","-",value)
    value = re.sub(r"[^a-z0-9-]+","",value)
    value = re.sub(r"-{2,}","-",value).strip("-")
    return value or "untitled"

def normalize_date(s: str) -> str:
    if not s:
        return "nodate"
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
    digits = re.sub(r"[^0-9]","",s)
    return digits if digits else slugify(s)

def infer_field(row: dict, keys: list[str]) -> str:
    lower_map = {k.lower(): (v if v is not None else "") for k,v in row.items()}
    for k in keys:
        if k.lower() in lower_map:
            val = str(lower_map[k.lower()]).strip()
            if val:
                return val
    return ""

def yaml_escape(value: str) -> str:
    if value is None: return '""'
    s = str(value)
    if re.fullmatch(r"(true|false|null)", s, re.I) or re.fullmatch(r"-?\d+(\.\d+)?", s):
        need = True
    else:
        need = (
            bool(re.search(r"[\\:#{}\[\],&*!|>@`?-]", s)) or
            s.startswith(" ") or s.endswith(" ") or "\n" in s or '"' in s or "'"
        )
    if need:
        s = s.replace("\\","\\\\").replace('"','\\"')
        return f'"{s}"'
    return s

def is_urlish(value: str) -> bool:
    return isinstance(value,str) and value.strip().startswith(("http://","https://"))

def sanitize_value(key: str, val: str) -> str:
    if not isinstance(val,str):
        val = str(val)
    if key.lower() in EXCLUDED_SANITIZE_KEYS:
        return val.strip()
    return val.replace(":", "-").strip()

def write_markdown(out_path: str, frontmatter: dict, ordered_fields: list[str]):
    lines = ["---"]
    for k in ordered_fields:
        raw_v = frontmatter.get(k,"")
        v = sanitize_value(k, raw_v)
        if k.lower()=="description":
            esc = v.replace("\\","\\\\").replace('"','\\"')
            esc = esc.replace("\r\n","\n").replace("\r","\n").replace("\n","\\n")
            lines.append(f'{k}: "{esc}"')
        else:
            lines.append(f"{k}: {yaml_escape(v)}")
    lines.append("---")
    lines.append("")

    title_key = next((c for c in ("title","name","titel") if c in frontmatter and str(frontmatter[c]).strip()), None)
    lines.append(f"# {{{{ {jinja_meta(title_key)} }}}}" if title_key else "# {{ page.meta.title | default('Untitled') }}")

    meta_line = []
    if frontmatter.get("date","").strip(): meta_line.append("**Datum:** {{ page.meta.date }}")
    elif frontmatter.get("datum","").strip(): meta_line.append("**Datum:** {{ page.meta.datum }}")

    for loc_key in ("city","stadt","ort","location","place","country","land"):
        if frontmatter.get(loc_key,"").strip():
            meta_line.append(f"**{loc_key.capitalize()}:** {{{{ {jinja_meta(loc_key)} }}}}")
    if meta_line:
        lines.append("_" + " • ".join(meta_line) + "_")
        lines.append("")

    pic_keys_present = [k for k in ordered_fields if k.lower() in PICTURE_KEYS and str(frontmatter.get(k,"")).strip()]
    if pic_keys_present:
        lines.append("## Bild" if len(pic_keys_present)==1 else "## Bilder")
        for k in pic_keys_present:
            lines.append(f"![{{{{ {jinja_meta('title')} | default('Bild') }}}}]({{{{ {jinja_meta(k)} }}}})")
        lines.append("")

    link_lines = []
    for k in ordered_fields:
        if k.lower() in PICTURE_KEYS: continue
        val = frontmatter.get(k,"")
        if is_urlish(val):
            jm = jinja_meta(k)
            link_lines.append(f"- **{k}**: [{{{{ {jm} }}}}]({{{{ {jm} }}}})")
    if link_lines:
        lines.append("## Links")
        lines.extend(link_lines)
        lines.append("")

    info_lines = []
    for k in ordered_fields:
        if k.lower() in PICTURE_KEYS or k in ("title","name","titel","date","datum"): continue
        val = str(frontmatter.get(k,"")).strip()
        if not val or is_urlish(val): continue
        jm = jinja_meta(k)
        info_lines.append(f"- **{k}**: {{{{ {jm} }}}}")
    if info_lines:
        lines.append("## Infos")
        lines.extend(info_lines)
        lines.append("")

    with open(out_path,"w",encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

def format_number_for_filename(num_raw: str, min_width: int) -> str:
    s = str(num_raw).strip()
    digits = re.sub(r"\D","",s)
    if not digits: return s or "000000"
    return digits.zfill(max(min_width, len(digits)))

def to_float_or_none(s: Any) -> Optional[float]:
    if s is None: return None
    txt = str(s).strip()
    if not txt: return None
    txt = txt.replace(",", ".")
    try:
        return float(txt)
    except Exception:
        m = re.search(r"-?\d+(?:\.\d+)?", txt)
        return float(m.group(0)) if m else None

def to_int_or_none(s: Any) -> Optional[int]:
    if s is None: return None
    txt = str(s).strip()
    if not txt: return None
    try:
        return int(float(txt.replace(",", ".")))
    except Exception:
        m = re.search(r"-?\d+", txt)
        return int(m.group(0)) if m else None

def parse_combined_coords(v: str) -> Optional[Tuple[float,float]]:
    if not v: return None
    s = v.strip()
    if s.startswith("{") or s.startswith("["):
        try:
            data = json.loads(s)
            if isinstance(data, dict) and "coordinates" in data:
                coords = data["coordinates"]
                if isinstance(coords, (list,tuple)) and len(coords)>=2:
                    lon = to_float_or_none(coords[0]); lat = to_float_or_none(coords[1])
                    if lat is not None and lon is not None: return (lat, lon)
            if isinstance(data, (list,tuple)) and len(data)>=2:
                lon = to_float_or_none(data[0]); lat = to_float_or_none(data[1])
                if lat is not None and lon is not None: return (lat, lon)
        except Exception:
            pass
    m = re.search(r"POINT\s*\(\s*(-?\d+(?:[.,]\d+)?)\s+(-?\d+(?:[.,]\d+)?)\s*\)", s, re.I)
    if m:
        lon = to_float_or_none(m.group(1)); lat = to_float_or_none(m.group(2))
        if lat is not None and lon is not None: return (lat, lon)
    parts = re.split(r"[;,]\s*|\s+", s)
    if len(parts) >= 2:
        a = to_float_or_none(parts[0]); b = to_float_or_none(parts[1])
        if a is not None and b is not None:
            if -90.0 <= a <= 90.0 and -180.0 <= b <= 180.0: return (a, b)
            if -90.0 <= b <= 90.0 and -180.0 <= a <= 180.0: return (b, a)
    return None

def extract_coords(row: dict, lat_key_pref: Optional[str], lon_key_pref: Optional[str]) -> Tuple[Optional[float], Optional[float], str]:
    if lat_key_pref and lon_key_pref:
        lat = to_float_or_none(row.get(lat_key_pref, ""))
        lon = to_float_or_none(row.get(lon_key_pref, ""))
        if lat is not None and lon is not None:
            return lat, lon, ""
        return None, None, f"explicit keys not found/parsable (lat='{lat_key_pref}', lon='{lon_key_pref}')"

    lower = {k.lower(): v for k,v in row.items()}
    lat = None; lon = None
    for k in LAT_KEYS_CANON:
        if k in lower:
            lat = to_float_or_none(lower[k]); 
            if lat is not None: break
    for k in LON_KEYS_CANON:
        if k in lower:
            lon = to_float_or_none(lower[k]); 
            if lon is not None: break
    if lat is not None and lon is not None:
        return lat, lon, ""

    for k in COMBINED_COORD_KEYS:
        if k in lower and str(lower[k]).strip():
            tpl = parse_combined_coords(str(lower[k]))
            if tpl:
                return tpl[0], tpl[1], ""
    return None, None, "no coord columns matched"

def build_feature(row: dict, lat: Optional[float], lon: Optional[float]) -> dict:
    props = {}
    for target, candidates in PROP_MAP:
        val = infer_field(row, candidates)
        if target == "nummer":
            props["nummer"] = to_int_or_none(val)
        elif target in ("completed","missions","category"):
            props[target] = to_int_or_none(val)
        elif target == "date":
            yr = to_int_or_none(val)
            props["date"] = yr if yr is not None else (val if val else None)
        elif target == "length_km":
            props["length_km"] = to_float_or_none(val)  # no /1000!
        elif target == "bg_link":
            props["bg_link"] = val or None
        else:
            props[target] = val or None

    if not props.get("title"):
        props["title"] = infer_field(row, ["title","titel","name"]) or ""
    if not props.get("picture"):
        props["picture"] = infer_field(row, list(PICTURE_KEYS)) or None

    props = {k:v for k,v in props.items() if v is not None}
    geom = {"type":"Point","coordinates":[lon, lat]} if (lat is not None and lon is not None) else None
    return {"type":"Feature","geometry": geom,"properties": props}

# --- Main ---
def main():
    parser = argparse.ArgumentParser(description="Create Markdown and GeoJSON from CSV.")
    parser.add_argument("--csv", required=True)
    parser.add_argument("--out", default="docs/banner")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--pad-width", type=int, default=6)
    parser.add_argument("--geojson-out", default="data/map.geojson")
    parser.add_argument("--lat-key", default=None, help="Explicit latitude column name")
    parser.add_argument("--lon-key", default=None, help="Explicit longitude column name")
    parser.add_argument("--include-missing-geometry", action="store_true",
                        help="Include features with geometry=null when coordinates are missing")
    parser.add_argument("--debug-geo", action="store_true", help="Print reasons for skipped geometry")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)
    os.makedirs(os.path.dirname(args.geojson_out) or ".", exist_ok=True)

    features = []
    created = skipped = overwritten = 0
    missing_geo = 0
    debug_samples = []

    with open(args.csv, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise SystemExit("CSV has no header row. Please include column names.")

        for idx, row in enumerate(reader, start=1):
            num_raw = infer_field(row, ["nummer","number","no","id"]) or str(idx)
            num_padded = format_number_for_filename(num_raw, args.pad_width)
            title = infer_field(row, ["title","titel","name"]) or f"row-{idx}"
            date_raw = infer_field(row, ["date","datum","created","when","planned_date"])
            date_norm = normalize_date(date_raw)
            slug = slugify(title)
            filename = f"{num_padded}_{slug}_{date_norm}.md"
            out_path = os.path.join(args.out, filename)

            ordered_fields = list(reader.fieldnames)
            frontmatter = {}
            for k in ordered_fields:
                val = row.get(k, "")
                if isinstance(val, str):
                    val = val.strip()
                frontmatter[k] = sanitize_value(k, val)

            if "title" not in frontmatter or not str(frontmatter.get("title","")).strip():
                if "titel" in frontmatter and str(frontmatter["titel"]).strip():
                    frontmatter["title"] = frontmatter["titel"]
                    if "title" not in ordered_fields:
                        ordered_fields.append("title")
            if date_raw and ("date" not in frontmatter or not str(frontmatter.get("date","")).strip()):
                frontmatter["date"] = date_norm
                if "date" not in ordered_fields:
                    ordered_fields.append("date")

            if os.path.exists(out_path):
                if args.overwrite:
                    write_markdown(out_path, frontmatter, ordered_fields)
                    overwritten += 1
                else:
                    skipped += 1
            else:
                write_markdown(out_path, frontmatter, ordered_fields)
                created += 1

            lat, lon, reason = extract_coords(row, args.lat_key, args.lon_key)
            if lat is None or lon is None:
                if args.include-missing-geometry:
                    features.append(build_feature(row, None, None))
                else:
                    missing_geo += 1
                    if args.debug_geo and len(debug_samples) < 10:
                        debug_samples.append({
                            "row": idx,
                            "title": title,
                            "reason": reason,
                            "available_keys": list(row.keys())
                        })
                continue
            features.append(build_feature(row, lat, lon))

    with open(args.geojson_out, "w", encoding="utf-8") as jf:
        json.dump({"type":"FeatureCollection","features": features}, jf, ensure_ascii=False, indent=4)

    print(f"✅ Markdown  -> Created: {created}, Overwritten: {overwritten}, Skipped (exists): {skipped}. Out: {os.path.abspath(args.out)}")
    print(f"🗺️ GeoJSON   -> Features: {len(features)} written to: {os.path.abspath(args.geojson_out)}")
    if missing_geo:
        print(f"ℹ️ Rows without coordinates: {missing_geo} (use --debug-geo / --lat-key/--lon-key / --include-missing-geometry)")
        if debug_samples:
            print("— Debug samples (first up to 10):")
            for s in debug_samples:
                print(f"  Row {s['row']} '{s['title']}' -> {s['reason']}")

if __name__ == "__main__":
    main()
