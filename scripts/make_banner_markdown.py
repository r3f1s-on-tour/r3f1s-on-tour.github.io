#!/usr/bin/env python3
"""
Create Markdown files from a CSV.
- Each row -> docs/banner/<number>_<slugified-title>_<date>.md
- Writes all CSV columns into YAML front matter.
- If target file already exists, the row is skipped (unless --overwrite).
- Body only shows fields present in frontmatter and references them via {{ page.meta.<key> }},
  styled into sections (no big generic table).
- Picture-like columns are embedded as images using their {{ page.meta.<key> }} values.

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

URL_HINT_KEYS = set(PICTURE_KEYS)

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
            or "'" in s
        ):
            need = True
    if need:
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

def is_urlish(value: str) -> bool:
    return isinstance(value, str) and value.strip().startswith(("http://", "https://"))

def write_markdown(out_path: str, frontmatter: dict, ordered_fields: list[str]):
    lines = ["---"]
    for k in ordered_fields:
        v = frontmatter.get(k, "")
        lines.append(f"{k}: {yaml_escape(v)}")
    lines.append("---")
    lines.append("")

    # Titel
    title_key = None
    for cand in ("title", "name", "titel"):
        if cand in frontmatter and str(frontmatter[cand]).strip():
            title_key = cand
            break
    if title_key:
        lines.append(f"# {{ {{ page.meta.{title_key} }} }}".replace(" { ", "{").replace(" }", "}"))
    else:
        lines.append("# {{ page.meta.title | default('Untitled') }}")

    # Meta-Zeile (nur vorhandene Felder)
    meta_line = []
    if "date" in frontmatter and str(frontmatter["date"]).strip():
        meta_line.append("**Datum:** {{ page.meta.date }}")
    elif "datum" in frontmatter and str(frontmatter["datum"]).strip():
        meta_line.append("**Datum:** {{ page.meta.datum }}")

    for loc_key in ("city","stadt","ort","location","place","country","land"):
        if loc_key in frontmatter and str(frontmatter[loc_key]).strip():
            meta_line.append(f"**{loc_key.capitalize()}:** {{ {{ page.meta.{loc_key} }} }}".replace(" { ", "{").replace(" }", "}"))

    if meta_line:
        lines.append("_" + " • ".join(meta_line) + "_")
        lines.append("")

    # Bilder (nur Felder, die wirklich existieren)
    pic_keys_present = [k for k in ordered_fields if k.lower() in PICTURE_KEYS and str(frontmatter.get(k, "")).strip()]
    if pic_keys_present:
        lines.append("## Bild" if len(pic_keys_present)==1 else "## Bilder")
        for k in pic_keys_present:
            lines.append(f"![{{ {{ page.meta.title | default('Bild') }} }}]({{ {{ page.meta.{k} }} }})".replace(" { ", "{").replace(" }", "}"))
        lines.append("")

    # Links (andere URL-Felder)
    link_lines = []
    for k in ordered_fields:
        if k.lower() in URL_HINT_KEYS:
            continue
        val = frontmatter.get(k, "")
        if is_urlish(val):
            link_lines.append(f"- **{k}**: {{% raw %}}[{{{{ page.meta.{k} }}}}]({{{{ page.meta.{k} }}}}){{% endraw %}}")
    if link_lines:
        lines.append("## Links")
        lines.extend(link_lines)
        lines.append("")

    # Infos (schöne Liste statt Tabelle)
    info_lines = []
    for k in ordered_fields:
        if k.lower() in PICTURE_KEYS:
            continue
        val = str(frontmatter.get(k, "")).strip()
        if not val:
            continue
        if is_urlish(val):
            continue
        if k in ("title","name","titel","date","datum"):
            continue
        info_lines.append(f"- **{k}**: {{ {{ page.meta.{k} }} }}".replace(" { ", "{").replace(" }", "}"))
    if info_lines:
        lines.append("## Infos")
        lines.extend(info_lines)
        lines.append("")

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

            ordered_fields = list(reader.fieldnames)
            frontmatter = {}
            for k in ordered_fields:
                val = row.get(k, "")
                if isinstance(val, str):
                    val = val.strip()
                frontmatter[k] = val

            # Komfortfelder titel->title, datum->date (falls sinnvoll)
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
                continue

            write_markdown(out_path, frontmatter, ordered_fields)
            created += 1

    print(f"Done. Created: {created}, Overwritten: {overwritten}, Skipped (exists): {skipped}. Output: {os.path.abspath(out_dir)}")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Create Markdown files from a CSV.
- Each row -> docs/banner/<number>_<slugified-title>_<date>.md
- Writes all CSV columns into YAML front matter.
- If target file already exists, the row is skipped (unless --overwrite).
- Body only shows fields present in frontmatter and references them via {{ page.meta.<key> }},
  styled into sections (no big generic table).
- Picture-like columns are embedded as images using their {{ page.meta.<key> }} values.
- Replace ":" with "-" in all frontmatter values EXCEPT for keys "bg-link" and "picture".
- Ensure 'description' is always quoted with "..." and newlines are encoded as "\n" for multiline interpretation.

Usage:
  python make_banner_markdown.py --csv path/to/banner.csv --out docs/banner [--overwrite]
"""
import argparse
import csv
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
    """Safely escape YAML values (except we special-case 'description' elsewhere)."""
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
            re.search(r"[\\:#{}\[\],&*!|>@`?-]", s)
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

def is_urlish(value: str) -> bool:
    return isinstance(value, str) and value.strip().startswith(("http://", "https://"))

def sanitize_value(key: str, val: str) -> str:
    """
    Replace ":" with "-" in values to avoid YAML issues,
    EXCEPT for keys in EXCLUDED_SANITIZE_KEYS (case-insensitive).
    """
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
            # Special handling:
            # - keep content as-is except global sanitize (already applied)
            # - escape backslashes and double quotes
            # - convert real newlines to literal "\n" so YAML parses a quoted string containing line breaks
            esc = v.replace("\\", "\\\\").replace('"', '\\"')
            esc = esc.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "\\n")
            lines.append(f'{k}: "{esc}"')
        else:
            lines.append(f"{k}: {yaml_escape(v)}")
    lines.append("---")
    lines.append("")

    # Title
    title_key = None
    for cand in ("title", "name", "titel"):
        if cand in frontmatter and str(frontmatter[cand]).strip():
            title_key = cand
            break
    if title_key:
        lines.append(f"# {{ {{ page.meta.{title_key} }} }}".replace(" { ", "{").replace(" }", "}"))
    else:
        lines.append("# {{ page.meta.title | default('Untitled') }}")

    # Meta line
    meta_line = []
    if "date" in frontmatter and str(frontmatter["date"]).strip():
        meta_line.append("**Datum:** {{ page.meta.date }}")
    elif "datum" in frontmatter and str(frontmatter["datum"]).strip():
        meta_line.append("**Datum:** {{ page.meta.datum }}")

    for loc_key in ("city","stadt","ort","location","place","country","land"):
        if loc_key in frontmatter and str(frontmatter[loc_key]).strip():
            meta_line.append(f"**{loc_key.capitalize()}:** {{ {{ page.meta.{loc_key} }} }}".replace(" { ", "{").replace(" }", "}"))

    if meta_line:
        lines.append("_" + " • ".join(meta_line) + "_")
        lines.append("")

    # Bilder
    pic_keys_present = [k for k in ordered_fields if k.lower() in PICTURE_KEYS and str(frontmatter.get(k, "")).strip()]
    if pic_keys_present:
        lines.append("## Bild" if len(pic_keys_present)==1 else "## Bilder")
        for k in pic_keys_present:
            lines.append(f"![{{ {{ page.meta.title | default('Bild') }} }}]({{ {{ page.meta.{k} }} }})".replace(" { ", "{").replace(" }", "}"))
        lines.append("")

    # Links
    link_lines = []
    for k in ordered_fields:
        if k.lower() in URL_HINT_KEYS:
            continue
        val = frontmatter.get(k, "")
        if is_urlish(val):
            link_lines.append(f"- **{k}**: {{% raw %}}[{{{{ page.meta.{k} }}}}]({{{{ page.meta.{k} }}}}){{% endraw %}}")
    if link_lines:
        lines.append("## Links")
        lines.extend(link_lines)
        lines.append("")

    # Infos
    info_lines = []
    for k in ordered_fields:
        if k.lower() in PICTURE_KEYS:
            continue
        val = str(frontmatter.get(k, "")).strip()
        if not val:
            continue
        if is_urlish(val):
            continue
        if k in ("title","name","titel","date","datum"):
            continue
        info_lines.append(f"- **{k}**: {{ {{ page.meta.{k} }} }}".replace(" { ", "{").replace(" }", "}"))
    if info_lines:
        lines.append("## Infos")
        lines.extend(info_lines)
        lines.append("")

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

            ordered_fields = list(reader.fieldnames)
            frontmatter = {}
            for k in ordered_fields:
                val = row.get(k, "")
                if isinstance(val, str):
                    val = val.strip()
                # per-key sanitize (colons removed except bg-link & picture)
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

            if os.path.exists(out_path):
                if args.overwrite:
                    write_markdown(out_path, frontmatter, ordered_fields)
                    overwritten += 1
                else:
                    skipped += 1
                continue

            write_markdown(out_path, frontmatter, ordered_fields)
            created += 1

    print(f"Done. Created: {created}, Overwritten: {overwritten}, Skipped (exists): {skipped}. Output: {os.path.abspath(out_dir)}")

if __name__ == "__main__":
    main()
