#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import sys, re, unicodedata

try:
    from ruamel.yaml import YAML
except ImportError:
    print("Please install ruamel.yaml (pip install ruamel.yaml)", file=sys.stderr)
    sys.exit(1)

DOCS_DIR = Path("docs")
ROOT_INDEX = DOCS_DIR / "index.md"
BANNER_DIR = DOCS_DIR / "banner"
BANNER_INDEX = BANNER_DIR / "index.md"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
COMPLETED_PATTERN = re.compile(r"^\s*(\d+)\s*(?:/\s*\d+\s*)?$")  # "12" or "12/24"

# Markers for the stats block in docs/index.md
STATS_START = "<!-- BANNER-STATS:START -->"
STATS_END   = "<!-- BANNER-STATS:END -->"

yaml = YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=2, offset=2)

UMLAUT_MAP = str.maketrans({"Ä":"A","ä":"a","Ö":"O","ö":"o","Ü":"U","ü":"u","ß":"s"})

# ---------- helpers ----------
def load_text(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""

def save_text(p: Path, s: str):
    p.write_text(s, encoding="utf-8", newline="\n")

def read_frontmatter_and_body(text: str):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text, False
    fm = yaml.load(m.group(1)) or {}
    body = text[m.end():]
    return fm, body, True

def write_frontmatter_and_body(frontmatter: dict, body: str) -> str:
    from io import StringIO
    buf = StringIO()
    yaml.dump(frontmatter, buf)
    fm_dump = buf.getvalue().rstrip() + "\n"
    return f"---\n{fm_dump}---\n{body}"

def parse_completed(v):
    if v is None or isinstance(v, bool): return None
    if isinstance(v, (int, float)):
        try: return int(v)
        except: return None
    if isinstance(v, str):
        m = COMPLETED_PATTERN.match(v)
        if m:
            try: return int(m.group(1))
            except: return None
    return None

def next_milestone(total: int, step: int = 500) -> int:
    if total < 0: total = 0
    return ((total // step) + 1) * step

def display_title(fm: dict, slug: str) -> str:
    t = fm.get("title")
    return t.strip() if isinstance(t, str) and t.strip() else slug.replace("-", " ").title()

def group_letter(title: str) -> str:
    s = title.strip()
    i = 0
    while i < len(s) and not s[i].isalpha():
        i += 1
    s = s[i:] if i < len(s) else s
    if not s: return "#"
    s = unicodedata.normalize("NFKD", s.translate(UMLAUT_MAP))
    ch = s[0].upper()
    return ch if "A" <= ch <= "Z" else "#"

def build_banner_directory(entries):
    """entries = [(title, slug)] -> English A–Z body for docs/banner/index.md"""
    letters = [chr(c) for c in range(ord("A"), ord("Z")+1)]
    groups = {L: [] for L in letters}; groups["#"] = []
    for title, slug in entries:
        L = group_letter(title)
        groups[L].append((title, slug))
    for L in groups:
        groups[L].sort(key=lambda x: x[0].casefold())

    nav = " | ".join([f"[{L}](#{L.lower()})" for L in letters])

    out = []
    out.append("# Banner Directory\n")
    out.append(nav + "\n")
    out.append("\n---\n")
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
    """Insert/replace stats block in docs/index.md between markers."""
    if STATS_START in body and STATS_END in body:
        pre = body.split(STATS_START)[0]
        post = body.split(STATS_END)[-1]
        return f"{pre}{STATS_START}\n{stats_md}\n{STATS_END}{post}"
    if body and not body.endswith("\n\n"): body += "\n"
    return f"{body}\n{STATS_START}\n{stats_md}\n{STATS_END}\n"

# ---------- main ----------
def main():
    if not BANNER_DIR.exists():
        print(f"Directory not found: {BANNER_DIR}", file=sys.stderr)
        sys.exit(0)

    # collect banner files (exclude index.md & gallery.md)
    banner_files = sorted([
        p for p in BANNER_DIR.glob("*.md")
        if p.name.lower() not in {"index.md", "gallery.md"}
    ])
    banner_count = len(banner_files)

    # compute titles, max completed + tiebreak by mtime
    entries = []
    max_completed = 0
    max_candidates = []

    for md in banner_files:
        txt = load_text(md)
        fm, _, _ = read_frontmatter_and_body(txt)
        slug = md.stem
        title = display_title(fm, slug)
        entries.append((title, slug))

        c = parse_completed(fm.get("completed"))
        if c is not None:
            if c > max_completed:
                max_completed = c
                max_candidates = [md]
            elif c == max_completed and c != 0:
                max_candidates.append(md)

    max_slug = ""
    max_title = ""
    if max_candidates:
        latest = max(max_candidates, key=lambda p: p.stat().st_mtime)
        fm_latest, _, _ = read_frontmatter_and_body(load_text(latest))
        max_slug = latest.stem
        max_title = display_title(fm_latest, max_slug)

    # ---------- write docs/index.md (stats block) ----------
    root_text = load_text(ROOT_INDEX)
    root_fm, root_body, has_fm = read_frontmatter_and_body(root_text) if root_text else ({}, "", False)

    # derive stats
    next_ = int(next_milestone(max_completed, 500))
    remaining = int(max(0, next_ - max_completed))
    progress_pct = round(100 * (max_completed % 500) / 500, 2)
    milestones_reached = max_completed // 500  # NEW: how many 500-steps already reached

    # frontmatter values (kept up to date for templates if needed)
    root_fm["banner_count"] = banner_count
    root_fm["completed_current"] = int(max_completed)
    root_fm["completed_from_banner_slug"] = max_slug
    root_fm["completed_from_banner_title"] = max_title
    root_fm["next_milestone"] = next_
    root_fm["remaining_to_next"] = remaining
    root_fm["progress_pct_to_next"] = progress_pct
    root_fm["milestones_reached_500"] = int(milestones_reached)  # NEW
    root_fm["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # exact formatting block (code block to match your example precisely)
    stats_lines = [
        "```text",
        f"Total banners: {banner_count}",
        f"Current progress: {max_completed} missions",
        f"Milestones reached (×500): {milestones_reached}",
        f"Next milestone (×500): {next_} (remaining: {remaining}, progress: {progress_pct}%)",
        f"Latest banner at this progress: {max_title or '-'}",
        f"Last updated: {root_fm['last_updated']}",
        "```",
    ]
    stats_md = "\n".join(stats_lines) + "\n"

    if not root_body.strip():
        root_body = "# Welcome\n\n"
    new_root_body = upsert_stats_block(root_body, stats_md)
    new_root_content = write_frontmatter_and_body(root_fm, new_root_body)
    if new_root_content != root_text:
        save_text(ROOT_INDEX, new_root_content)
        print(f"Updated: {ROOT_INDEX}")
    else:
        print("No changes in docs/index.md.")

    # ---------- write docs/banner/index.md (directory only) ----------
    banner_text = load_text(BANNER_INDEX)
    banner_fm, _, _ = read_frontmatter_and_body(banner_text) if banner_text else ({}, "", False)
    banner_body = build_banner_directory(entries)  # only directory
    new_banner_content = write_frontmatter_and_body(banner_fm, banner_body)
    if new_banner_content != banner_text:
        save_text(BANNER_INDEX, new_banner_content)
        print(f"Updated: {BANNER_INDEX}")
    else:
        print("No changes in docs/banner/index.md.")

if __name__ == "__main__":
    main()
