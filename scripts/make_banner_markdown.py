#!/usr/bin/env python3
"""
Create Markdown files from a CSV.
- Each row -> docs/banner/<number>_<slugified-title>_<date>.md
- Writes all CSV columns into YAML front matter.
- If target file already exists, the row is skipped (unless --overwrite).
- If a column named like "picture"/"image"/"pic_url" contains http(s) links,
  they are embedded directly as images in the Markdown body.

Usage:
  python make_banner_markdown.py --csv path/to/banner.csv --out docs/banner [--overwrite]
"""
import argparse
import csv
import os
import re
from datetime import datetime

PICTURE_KEYS = [
    "picture", "pictures", "image", "images", "img", "pic", "pic_url",
    "picture_url", "image_url", "bild", "bilder", "pictureurl", "imageurl"
]

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
            val = str(lower_map[k.lower()]).strip()
            if val:
                return val
    return ""

def yaml_escape(value: str) -> str:
    """Quote value if needed for YAML safety."""
    if value is None:
        return '""'
    s = str(value)

    # Heuristik: Werte quoten, die YAML heikel findet
    # 1) bool/null/zahl-ähnlich
    if re.fullmatch(r"(true|false|null)", s, flags=re.IGNORECASE):
        need = True
    elif re.fullmatch(r"-?\d+(\.\d+)?", s):
        need = True
    else:
        need = False
        # 2) Sonderzeichen laut YAML + führende/abschließende Spaces + Newlines
        #    WICHTIG: In der Zeichenklasse das Backslash zuerst platzieren,
        #    damit keine Range wie '\-?' entsteht.
        if (
            re.search(r"[\\:#{}\[\],&*!|>@`?-]", s)  # enthält Backslash, Doppelpkt., #, {}, [], usw. oder '-' oder '?'
            or s.startswith(" ")
            or s.endswith(" ")
            or "\n" in s
            or '"' in s
            or "'" in s
        ):
            need = True

    if need:
        # Doppelte Anführungszeichen verwenden und sicher escapen
        s = s.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{s}"'
    return s

def split_urls(val: str) -> list[str]:
    if not val:
        return []
    parts = re.split(r"[\s,;|]+", val.strip())
    urls = [p for p in parts if p.startswith(("http://", "https://"))]
    seen = set()
    unique = []
    for u in urls:
        if u not in seen:
            unique.append(u)
            seen.add(u)
    return unique

def extract_picture_urls(frontmatter: dict) -> list[str]:
    urls = []
    for k, v in frontmatter.items():
        if k.lower() in PICTURE_KEYS and isinstance(v, str):
            urls.extend(split_urls(v))
    # de-dupe
    seen = set()
    ret = []
    for u in urls:
        if u not in seen:
            ret.append(u)
            seen.add(u)
    return ret

def write_markdown(out_path: str, frontmatter: dict):
    # YAML
    lines = ["---"]
    for k, v in frontmatter.items():
        lines.append(f"{k}: {yaml_escape(v)}")
    lines.append("---")
    lines.append("")

    # Body
    title = frontmatter.get("title") or frontmatter.get("name") or frontmatter.get("titel") or "Untitled"
    date_val = frontmatter.get("date") or frontmatter.get("datum") or ""
    lines.append(f"# {title}")
    if date_val:
        lines.append(f"_Date:_ {date_val}")
        lines.append("")

    # Bilder einbetten
    pic_urls = extract_picture_urls(frontmatter)
    if pic_urls:
        lines.append("## Bild" if len(pic_urls) == 1 else "## Bilder")
        for u in pic_urls:
            lines.append(f"![{title}]({u})")
        lines.append("")

    # Weitere Links (aus anderen URL-Feldern, die nicht Bilder sind)
    links = []
    embedded = set(pic_urls)
    for k, v in frontmatter.items():
        if isinstance(v, str):
            for u in split_urls(v):
                if u not in embedded:
                    links.append(f"- **{k}**: [{u}]({u})")
    if links:
        lines.append("## Links")
        lines.extend(links)
        lines.append("")

    # Details-Tabelle
    if frontmatter:
        lines.append("## Details")
        lines.append("| Field | Value |")
        lines.append("|---|---|")
        for k, v in frontmatter.items():
            sv = str(v).replace("\n", " ").strip()
            if len(sv) > 200:
                sv = sv[:197] + "..."
            lines.append(f"| {k} | {sv} |")

    content = "\n".join(lines) + "\n"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    parser = argparse.ArgumentParser(description="Create Markdown files from CSV rows.")
    parser.add_argument("--csv", required=True, help="Path to input CSV file")
    parser.add_argument("--out", default="docs/banner", help="Output directory (default: docs/banner)")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing Markdown files")
    args = parser.parse_args()

    in_csv = args.csv
    out_dir = args.out
    os.makedirs(out_dir, exist_ok=True)

    with open(in_csv, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise SystemExit("CSV has no header row. Please include column names.")
        created, skipped, overwritten = 0, 0, 0
        for idx, row in enumerate(reader, start=1):
            num = infer_field(row, ["nummer", "number", "no", "id"]) or str(idx)
            title = infer_field(row, ["title", "titel", "name"]) or f"row-{idx}"
            date_raw = infer_field(row, ["date", "datum", "created", "when", "planned_date"])
            date_norm = normalize_date(date_raw)
            slug = slugify(title)
            filename = f"{num}_{slug}_{date_norm}.md"
            out_path = os.path.join(out_dir, filename)

            # Frontmatter in Original-Spaltenreihenfolge aufbauen
            frontmatter = {}
            for k in reader.fieldnames:
                val = row.get(k, "")
                if isinstance(val, str):
                    val = val.strip()
                frontmatter[k] = val
            if "title" not in frontmatter and "titel" in frontmatter and frontmatter["titel"]:
                frontmatter["title"] = frontmatter["titel"]
            if "date" not in frontmatter and date_raw:
                frontmatter["date"] = date_norm

            if os.path.exists(out_path):
                if args.overwrite:
                    write_markdown(out_path, frontmatter)
                    overwritten += 1
                else:
                    skipped += 1
                continue

            write_markdown(out_path, frontmatter)
            created += 1

    msg = f"Done. Created: {created}, Overwritten: {overwritten}, Skipped (exists): {skipped}. Output: {os.path.abspath(out_dir)}"
    print(msg)

if __name__ == "__main__":
    main()
