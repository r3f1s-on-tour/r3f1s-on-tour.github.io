#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import sys
import re
import unicodedata

try:
    from ruamel.yaml import YAML
except ImportError:
    print("Please install ruamel.yaml (pip install ruamel.yaml)", file=sys.stderr)
    sys.exit(1)

DOCS_DIR = Path("docs")
BANNER_DIR = DOCS_DIR / "banner"
INDEX_MD = BANNER_DIR / "index.md"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
COMPLETED_PATTERN = re.compile(r"^\s*(\d+)\s*(?:/\s*\d+\s*)?$")  # "12" oder "12/24"

yaml = YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=2, offset=2)

UMLAUT_MAP = str.maketrans({
    "Ä": "A", "ä": "a",
    "Ö": "O", "ö": "o",
    "Ü": "U", "ü": "u",
    "ß": "s",
})

def read_frontmatter_and_body(text: str):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text, False
    fm_text = m.group(1)
    body = text[m.end():]
    data = yaml.load(fm_text) or {}
    return data, body, True

def write_frontmatter_and_body(frontmatter: dict, body: str) -> str:
    from io import StringIO
    buf = StringIO()
    yaml.dump(frontmatter, buf)
    fm_dump = buf.getvalue().rstrip() + "\n"
    return f"---\n{fm_dump}---\n{body}"

def load_file(p: Path) -> str:
    return p.read_text(encoding="utf-8")

def save_file(p: Path, content: str):
    p.write_text(content, encoding="utf-8", newline="\n")

def parse_completed(value):
    """int, '12', '12/24' -> 12; sonst None; bool ignorieren."""
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        try:
            return int(value)
        except Exception:
            return None
    if isinstance(value, str):
        m = COMPLETED_PATTERN.match(value)
        if m:
            try:
                return int(m.group(1))
            except Exception:
                return None
    return None

def next_milestone(total: int, step: int = 500) -> int:
    """Nächstes STRICT größeres 500er-Milestone (500, 1000, …)."""
    if total < 0:
        total = 0
    return ((total // step) + 1) * step

def display_title_from(fm: dict, slug: str) -> str:
    t = fm.get("title")
    if isinstance(t, str) and t.strip():
        return t.strip()
    return slug.replace("-", " ").strip().title()

def group_letter(title: str) -> str:
    s = title.strip()
    i = 0
    while i < len(s) and not s[i].isalpha():
        i += 1
    s = s[i:] if i < len(s) else title.strip()
    if not s:
        return "#"
    s = s.translate(UMLAUT_MAP)
    s_norm = unicodedata.normalize("NFKD", s)
    first = s_norm[0].upper()
    return first if "A" <= first <= "Z" else "#"

def build_alphabetical_index(entries):
    letters = [chr(c) for c in range(ord("A"), ord("Z")+1)]
    groups = {L: [] for L in letters}
    groups["#"] = []
    for title, slug in entries:
        L = group_letter(title)
        groups.setdefault(L, [])
        groups[L].append((title, slug))
    for L in groups:
        groups[L].sort(key=lambda x: x[0].casefold())

    nav = " | ".join([f"[{L}](#{L.lower()})" for L in letters])
    out = []
    out.append("# Banner Übersicht\n")
    out.append(nav + "\n")
    out.append("\n---\n")
    for L in letters:
        out.append(f"## {L}\n")
        if groups[L]:
            for title, slug in groups[L]:
                out.append(f"- [{title}](./{slug}/)")
        else:
            out.append("_(keine Einträge)_")
        out.append("")
    if groups["#"]:
        out.append("## #\n")
        for title, slug in groups["#"]:
            out.append(f"- [{title}](./{slug}/)")
        out.append("")
    return "\n".join(out).rstrip() + "\n"

def main():
    if not BANNER_DIR.exists():
        print(f"Verzeichnis nicht gefunden: {BANNER_DIR}", file=sys.stderr)
        sys.exit(0)

    # Alle Banner außer index.md & gallery.md
    banner_files = sorted([
        p for p in BANNER_DIR.glob("*.md")
        if p.name.lower() not in {"index.md", "gallery.md"}
    ])
    banner_count = len(banner_files)

    # Alphabet-Einträge & Completed-Tracking
    toc_entries = []  # (title, slug)
    max_completed = 0
    max_files = []  # Kandidaten mit gleichem Max (für Tiebreak)

    for md in banner_files:
        text = load_file(md)
        fm, _, _ = read_frontmatter_and_body(text)
        slug = md.stem
        title = display_title_from(fm, slug)
        toc_entries.append((title, slug))

        c = parse_completed(fm.get("completed"))
        if c is not None:
            if c > max_completed:
                max_completed = c
                max_files = [md]
            elif c == max_completed and c != 0:
                max_files.append(md)

    # Falls mehrere Banner den gleichen Max haben: nimm das zuletzt geänderte
    max_banner_slug = None
    max_banner_title = None
    if max_files:
        latest_file = max(max_files, key=lambda p: p.stat().st_mtime)
        latest_text = load_file(latest_file)
        latest_fm, _, _ = read_frontmatter_and_body(latest_text)
        max_banner_slug = latest_file.stem
        max_banner_title = display_title_from(latest_fm, max_banner_slug)

    # index.md Frontmatter laden/erzeugen
    if INDEX_MD.exists():
        idx_text = load_file(INDEX_MD)
        fm, _, has_fm = read_frontmatter_and_body(idx_text)
        if not has_fm:
            fm = {}
    else:
        fm = {}

    # Frontmatter setzen: aktueller Stand = MAX completed
    fm["banner_count"] = banner_count
    fm["completed_current"] = int(max_completed)                # << dein gewünschter Max-Stand
    fm["completed_from_banner_slug"] = max_banner_slug or ""    # Referenz
    fm["completed_from_banner_title"] = max_banner_title or ""  # hübscher Name
    fm["next_milestone"] = int(next_milestone(max_completed, 500))
    fm["remaining_to_next"] = int(max(0, fm["next_milestone"] - max_completed))
    fm["progress_pct_to_next"] = round(100 * (max_completed % 500) / 500, 2)
    fm["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Body = alphabetisches Inhaltsverzeichnis
    new_body = build_alphabetical_index(toc_entries)
    new_content = write_frontmatter_and_body(fm, new_body)

    prev_content = load_file(INDEX_MD) if INDEX_MD.exists() else ""
    if not INDEX_MD.exists() or new_content != prev_content:
        save_file(INDEX_MD, new_content)
        print(f"Aktualisiert: {INDEX_MD}")
    else:
        print("Keine Änderung erforderlich.")

if __name__ == "__main__":
    main()
