#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import sys, re, unicodedata, os

try:
    from ruamel.yaml import YAML
except ImportError:
    print("Please install ruamel.yaml (pip install ruamel.yaml)", file=sys.stderr)
    sys.exit(1)

# --- Paths ---
DOCS_DIR = Path("docs")
ROOT_INDEX = DOCS_DIR / "index.md"
BANNER_DIR = DOCS_DIR / "banner"
BANNER_INDEX = BANNER_DIR / "index.md"

# --- Regex ---
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
COMPLETED_PATTERN = re.compile(r"^\s*(\d+)\s*(?:/\s*\d+\s*)?$")

# Nur Dateien wie 001_Title_2024.md
VALID_FILENAME_RE = re.compile(r"^\d+_.+_20\d{2}\.md$", re.IGNORECASE)

# --- Markers ---
STATS_START = "<!-- BANNER-STATS:START -->"
STATS_END   = "<!-- BANNER-STATS:END -->"

# --- YAML setup ---
yaml = YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=2, offset=2)

UMLAUT_MAP = str.maketrans({"Ä": "A", "ä": "a", "Ö": "O", "ö": "o", "Ü": "U", "ü": "u", "ß": "s"})
DEBUG = os.getenv("DEBUG_BANNER", "0") == "1"

# ---------- Helpers ----------
def load_text(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""

def save_text(p: Path, s: str):
    p.write_text(s, encoding="utf-8", newline="\n")

def read_frontmatter_and_body(text: str):
    m = re.match(FRONTMATTER_RE, text)
    if not m:
        return {}, text, False
    fm = yaml.load(m.group(1)) or {}
    return fm, text[m.end():], True

def write_frontmatter_and_body(fm: dict, body: str) -> str:
    from io import StringIO
    buf = StringIO()
    yaml.dump(fm, buf)
    fm_dump = buf.getvalue().rstrip() + "\n"
    return f"---\n{fm_dump}---\n{body}"

def parse_completed(v):
    if v is None or isinstance(v, bool): return None
    if isinstance(v, (int, float)): return int(v)
    if isinstance(v, str):
        m = COMPLETED_PATTERN.match(v)
        if m: return int(m.group(1))
    return None

def next_milestone(total: int, step: int = 500) -> int:
    return ((max(total, 0) // step) + 1) * step

def display_title(fm: dict, slug: str) -> str:
    t = fm.get("title")
    return t.strip() if isinstance(t, str) and t.strip() else slug.replace("-", " ").title()

def group_letter(title: str) -> str:
    s = title.strip().translate(UMLAUT_MAP)
    if not s:
        return "#"
    s = unicodedata.normalize("NFKD", s)
    first = s[0].upper()
    return first if "A" <= first <= "Z" else "#"

def build_banner_directory(entries):
    """entries = [(title, slug)] -> English A–Z body for docs/banner/index.md"""
    letters = [chr(c) for c in range(ord("A"), ord("Z")+1)]
    groups = {L: [] for L in letters}
    groups["#"] = []

    for title, slug in entries:
        L = group_letter(title)
        groups[L].append((title, slug))
    for L in groups:
        groups[L].sort(key=lambda x: x[0].casefold())

    nav = " | ".join([f"[{L}](#{L.lower()})" for L in letters])

    out = [f"# Banner Directory\n", nav, "\n---\n"]
    for L in letters:
        out.append(f"## {L}\n")
        if groups[L]:
            for title, slug in groups[L]:
                out.append(f"- [{title}](./{slug}/)")
        else:
            out.append("_(no entries)_")
        out.append("")
    if groups["#"]:
        out.append("## #\n")
        for title, slug in groups["#"]:
            out.append(f"- [{title}](./{slug}/)")
        out.append("")
    return "\n".join(out).rstrip() + "\n"

def upsert_stats_block(body: str, stats_md: str) -> str:
    """Replace or append stats section."""
    if STATS_START in body and STATS_END in body:
        pre = body.split(STATS_START)[0]
        post = body.split(STATS_END)[-1]
        return f"{pre}{STATS_START}\n{stats_md}\n{STATS_END}{post}"
    if body and not body.endswith("\n\n"):
        body += "\n"
    return f"{body}\n{STATS_START}\n{stats_md}\n{STATS_END}\n"

# ---------- Main ----------
def main():
    if not BANNER_DIR.exists():
        print(f"Missing directory: {BANNER_DIR}", file=sys.stderr)
        sys.exit(1)

    # Filter nur Dateien, die dem Schema 001_Title_2024.md entsprechen
    banner_files = sorted([
        p for p in BANNER_DIR.glob("*.md")
        if VALID_FILENAME_RE.match(p.name)
    ])

    if DEBUG:
        print("Banner candidates:", [p.name for p in banner_files])

    banner_count = len(banner_files)

    entries = []
    max_completed = 0
    max_candidates = []

    for p in banner_files:
        text = load_text(p)
        fm, _, _ = read_frontmatter_and_body(text)
        slug = p.stem
        title = display_title(fm, slug)
        entries.append((title, slug))

        c = parse_completed(fm.get("completed"))
        if c is not None:
            if c > max_completed:
                max_completed = c
                max_candidates = [p]
            elif c == max_completed and c != 0:
                max_candidates.append(p)

    # Determine "latest banner"
    max_slug = ""
    max_title = ""
    if max_candidates:
        latest = max(max_candidates, key=lambda x: x.stat().st_mtime)
        fm_latest, _, _ = read_frontmatter_and_body(load_text(latest))
        max_slug = latest.stem
        max_title = display_title(fm_latest, max_slug)
    elif banner_files:
        latest_any = max(banner_files, key=lambda x: x.stat().st_mtime)
        fm_latest_any, _, _ = read_frontmatter_and_body(load_text(latest_any))
        max_slug = latest_any.stem
        max_title = display_title(fm_latest_any, max_slug)

    # --- Update docs/index.md ---
    root_txt = load_text(ROOT_INDEX)
    root_fm, root_body, _ = read_frontmatter_and_body(root_txt) if root_txt else ({}, "", False)

    next_ = next_milestone(max_completed, 500)
    remaining = max(0, next_ - max_completed)
    progress_pct = round(100 * (max_completed % 500) / 500, 2)
    milestones_reached = max_completed // 500
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    root_fm.update({
        "banner_count": banner_count,
        "completed_current": int(max_completed),
        "completed_from_banner_slug": max_slug,
        "completed_from_banner_title": max_title,
        "next_milestone": int(next_),
        "remaining_to_next": int(remaining),
        "progress_pct_to_next": progress_pct,
        "milestones_reached_500": int(milestones_reached),
        "last_updated": now_iso,
    })

    latest_banner_line = (
        f"**Latest banner at this progress:** "
        f"[{max_title}](./banner/{max_slug}/)" if max_title else "**Latest banner at this progress:** -"
    )

    stats_md = (
        f"**Total banners:** {banner_count}  \n"
        f"**Current progress:** {max_completed} missions  \n"
        f"**Milestones reached (×500):** {milestones_reached}  \n"
        f"**Next milestone (×500):** {next_} (remaining: {remaining}, progress: {progress_pct}%)  \n"
        f"{latest_banner_line}  \n"
        f"**Last updated:** {now_iso}"
    )

    if not root_body.strip():
        root_body = "# Welcome\n\n"
    new_root_body = upsert_stats_block(root_body, stats_md)
    new_root = write_frontmatter_and_body(root_fm, new_root_body)
    save_text(ROOT_INDEX, new_root)
    print(f"Overwritten: {ROOT_INDEX}")

    # --- Update docs/banner/index.md ---
    banner_fm = {}
    entries.sort(key=lambda x: x[0].casefold())
    banner_body = build_banner_directory(entries)
    new_banner = write_frontmatter_and_body(banner_fm, banner_body)
    save_text(BANNER_INDEX, new_banner)
    print(f"Overwritten: {BANNER_INDEX}")

if __name__ == "__main__":
    main()
