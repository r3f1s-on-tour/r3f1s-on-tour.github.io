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
COMPLETED_PATTERN = re.compile(r"^\s*(\d+)\s*(?:/\s*\d+\s*)?$")

STATS_START = "<!-- BANNER-STATS:START -->"
STATS_END   = "<!-- BANNER-STATS:END -->"

yaml = YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=2, offset=2)
UMLAUT_MAP = str.maketrans({"Ä":"A","ä":"a","Ö":"O","ö":"o","Ü":"U","ü":"u","ß":"s"})

# ---------- helpers ----------
def load_text(p): return p.read_text(encoding="utf-8") if p.exists() else ""
def save_text(p, s): p.write_text(s, encoding="utf-8", newline="\n")

def read_frontmatter_and_body(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text, False
    fm = yaml.load(m.group(1)) or {}
    return fm, text[m.end():], True

def write_frontmatter_and_body(fm, body):
    from io import StringIO
    buf = StringIO()
    yaml.dump(fm, buf)
    return f"---\n{buf.getvalue().rstrip()}\n---\n{body}"

def parse_completed(v):
    if v is None or isinstance(v, bool): return None
    if isinstance(v, (int, float)): return int(v)
    if isinstance(v, str):
        m = COMPLETED_PATTERN.match(v)
        if m: return int(m.group(1))
    return None

def next_milestone(total, step=500):
    return ((max(total,0)//step)+1)*step

def display_title(fm, slug):
    t = fm.get("title")
    return t.strip() if isinstance(t, str) and t.strip() else slug.replace("-", " ").title()

def group_letter(title):
    s = title.strip().translate(UMLAUT_MAP)
    if not s: return "#"
    s_norm = unicodedata.normalize("NFKD", s)
    first = s_norm[0].upper()
    return first if "A" <= first <= "Z" else "#"

def build_banner_directory(entries):
    letters = [chr(c) for c in range(ord("A"), ord("Z")+1)]
    groups = {L: [] for L in letters}; groups["#"]=[]
    for title, slug in entries:
        L = group_letter(title)
        groups[L].append((title, slug))
    for L in groups: groups[L].sort(key=lambda x:x[0].casefold())
    nav = " | ".join([f"[{L}](#{L.lower()})" for L in letters])
    out=["# Banner Directory", nav, "\n---\n"]
    for L in letters:
        out.append(f"## {L}")
        if groups[L]:
            out += [f"- [{t}](./{s}/)" for t,s in groups[L]]
        else: out.append("_(no entries)_")
        out.append("")
    if groups["#"]:
        out.append("## #")
        out += [f"- [{t}](./{s}/)" for t,s in groups["#"]]
    return "\n".join(out).rstrip()+"\n"

def upsert_stats_block(body, stats_md):
    if STATS_START in body and STATS_END in body:
        pre = body.split(STATS_START)[0]
        post = body.split(STATS_END)[-1]
        return f"{pre}{STATS_START}\n{stats_md}\n{STATS_END}{post}"
    if body and not body.endswith("\n\n"): body += "\n"
    return f"{body}\n{STATS_START}\n{stats_md}\n{STATS_END}\n"

# ---------- main ----------
def main():
    if not BANNER_DIR.exists():
        print("Missing docs/banner directory", file=sys.stderr)
        sys.exit(1)

    banner_files = sorted([p for p in BANNER_DIR.glob("*.md")
                           if p.name.lower() not in {"index.md","gallery.md","stats.md"}])
    banner_count=len(banner_files)
    entries=[]; max_completed=0; max_candidates=[]

    for md in banner_files:
        txt=load_text(md)
        fm,_,_=read_frontmatter_and_body(txt)
        slug=md.stem; title=display_title(fm,slug)
        entries.append((title,slug))
        c=parse_completed(fm.get("completed"))
        if c is not None:
            if c>max_completed: max_completed,candidates=c,[md]
            elif c==max_completed and c!=0: max_candidates.append(md)

    max_slug=max_title=""
    if max_candidates:
        latest=max(max_candidates,key=lambda p:p.stat().st_mtime)
        fm_latest,_,_=read_frontmatter_and_body(load_text(latest))
        max_slug=latest.stem; max_title=display_title(fm_latest,max_slug)

    # ---- stats for docs/index.md ----
    root_txt=load_text(ROOT_INDEX)
    root_fm,root_body,_=read_frontmatter_and_body(root_txt) if root_txt else ({}, "", False)

    next_=next_milestone(max_completed,500)
    remaining=max(0,next_-max_completed)
    progress=round(100*(max_completed%500)/500,2)
    reached=max_completed//500
    now=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    root_fm.update({
        "banner_count":banner_count,
        "completed_current":max_completed,
        "completed_from_banner_slug":max_slug,
        "completed_from_banner_title":max_title,
        "next_milestone":next_,
        "remaining_to_next":remaining,
        "progress_pct_to_next":progress,
        "milestones_reached_500":reached,
        "last_updated":now
    })

    # pretty formatted Markdown section
    stats_md=(
        f"**Total banners:** {banner_count}  \n"
        f"**Current progress:** {max_completed} missions  \n"
        f"**Milestones reached (×500):** {reached}  \n"
        f"**Next milestone (×500):** {next_} (remaining: {remaining}, progress: {progress}%)  \n"
        f"**Latest banner at this progress:** {max_title or '-'}  \n"
        f"**Last updated:** {now}"
    )

    if not root_body.strip(): root_body="# Welcome\n\n"
    new_root_body=upsert_stats_block(root_body,stats_md)
    new_root=write_frontmatter_and_body(root_fm,new_root_body)
    if new_root!=root_txt:
        save_text(ROOT_INDEX,new_root)
        print(f"Updated: {ROOT_INDEX}")
    else: print("No changes in docs/index.md.")

    # ---- docs/banner/index.md ----
    banner_txt=load_text(BANNER_INDEX)
    banner_fm,_,_=read_frontmatter_and_body(banner_txt) if banner_txt else ({}, "", False)
    banner_body=build_banner_directory(entries)
    new_banner=write_frontmatter_and_body(banner_fm,banner_body)
    if new_banner!=banner_txt:
        save_text(BANNER_INDEX,new_banner)
        print(f"Updated: {BANNER_INDEX}")
    else: print("No changes in docs/banner/index.md.")

if __name__=="__main__":
    main()
