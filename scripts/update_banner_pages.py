#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import sys, re, unicodedata

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
COMPLETED_RE   = re.compile(r"^\s*(\d+)\s*(?:/\s*\d+\s*)?$")  # "12" or "12/24"

# --- YAML setup ---
yaml = YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=2, offset=2)

# Letters / grouping
UMLAUT_MAP = str.maketrans({"Ä":"A","ä":"a","Ö":"O","ö":"o","Ü":"U","ü":"u","ß":"s"})

# --- Utilities ---
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

def write_frontmatter_and_body(fm: dict, body: str) -> str:
    from io import StringIO
    buf = StringIO()
    yaml.dump(fm, buf)
    fm_dump = buf.getvalue().rstrip() + "\n"
    return f"---\n{fm_dump}---\n{body}"

def to_int_or_none(v):
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        try:
            return int(v)
        except Exception:
            return None
    if isinstance(v, str):
        s = v.strip()
        if s.isdigit():
            try:
                return int(s)
            except Exception:
                return None
    return None

def parse_completed(v):
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return int(v)
    if isinstance(v, str):
        m = COMPLETED_RE.match(v)
        if m:
            return int(m.group(1))
    return None

def next_milestone(total: int, step: int = 500) -> int:
    return ((max(total, 0) // step) + 1) * step

def display_title(fm: dict, slug: str) -> str:
    t = fm.get("title")
    return t.strip() if isinstance(t, str) and t.strip() else slug.replace("-", " ").title()

def group_letter(title: str) -> str:
    s = title.strip()
    if not s:
        return "#"
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
    START = "<!-- BANNER-STATS:START -->"
    END   = "<!-- BANNER-STATS:END -->"
    if START in body and END in body:
        pre = body.split(START)[0]
        post = body.split(END)[-1]
        return f"{pre}{START}\n{stats_md}\n{END}{post}"
    if body and not body.endswith("\n\n"):
        body += "\n"
    return f"{body}\n{START}\n{stats_md}\n{END}\n"

# --- Main logic ---
def main():
    if not BANNER_DIR.exists():
        print(f"Missing directory: {BANNER_DIR}", file=sys.stderr)
        sys.exit(1)

    # Consider every *.md in docs/banner except well-known meta pages
    excluded = {"index.md", "gallery.md", "stats.md", "readme.md"}
    candidates = sorted(p for p in BANNER_DIR.glob("*.md") if p.name.lower() not in excluded)

    # Filter to "real banners" = files that HAVE frontmatter with a valid 'nummer'
    banners = []  # list of tuples: (path, fm)
    for p in candidates:
        text = load_text(p)
        fm, _, has_fm = read_frontmatter_and_body(text)
        if not has_fm:
            continue
        n = to_int_or_none(fm.get("nummer"))
        if n is None:
            continue
        banners.append((p, fm))

    # TOTAL BANNERS = max 'nummer'
    max_nummer = 0
    for _, fm in banners:
        n = to_int_or_none(fm.get("nummer"))
        if n is not None and n > max_nummer:
            max_nummer = n

    # Build entries (for directory) and compute completed_current
    entries = []
    completed_max = 0
    completed_candidates = []
    for p, fm in banners:
        slug = p.stem
        title = display_title(fm, slug)
        entries.append((title, slug))

        c = parse_completed(fm.get("completed"))
        if c is not None:
            if c > completed_max:
                completed_max = c
                completed_candidates = [p]
            elif c == completed_max and c != 0:
                completed_candidates.append(p)

    # Decide "latest banner at this progress" (link)
    max_slug = ""
    max_title = ""
    if completed_candidates:
        latest = max(completed_candidates, key=lambda x: x.stat().st_mtime)
        fm_latest, _, _ = read_frontmatter_and_body(load_text(latest))
        max_slug = latest.stem
        max_title = display_title(fm_latest, max_slug)
    elif banners:
        latest_any = max((p for p, _ in banners), key=lambda x: x.stat().st_mtime)
        fm_latest_any, _, _ = read_frontmatter_and_body(load_text(latest_any))
        max_slug = latest_any.stem
        max_title = display_title(fm_latest_any, max_slug)

    # ----- Write docs/index.md (always overwrite) -----
    root_text = load_text(ROOT_INDEX)
    root_fm, root_body, _ = read_frontmatter_and_body(root_text) if root_text else ({}, "", False)

    next_ = next_milestone(completed_max, 500)
    remaining = max(0, next_ - completed_max)
    progress_pct = round(100 * (completed_max % 500) / 500, 2)
    milestones_reached = completed_max // 500
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Update frontmatter (helpful if you use these in templates)
    root_fm.update({
        "banner_count": int(max_nummer),                  # <-- total banners = max 'nummer'
        "completed_current": int(completed_max),
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
        f"**Total banners:** {max_nummer}  \n"
        f"**Current progress:** {completed_max} missions  \n"
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

    # ----- Write docs/banner/index.md (A–Z from filtered banners; always overwrite) -----
    entries.sort(key=lambda x: x[0].casefold())
    banner_fm = {}  # keep it simple; directory page doesn't need stats
    banner_body = build_banner_directory(entries)
    new_banner = write_frontmatter_and_body(banner_fm, banner_body)
    save_text(BANNER_INDEX, new_banner)
    print(f"Overwritten: {BANNER_INDEX}")

if __name__ == "__main__":
    main()
