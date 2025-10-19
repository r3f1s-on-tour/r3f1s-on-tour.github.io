#!/usr/bin/env python3
"""
Erzeugt docs/banner/gallery.md aus vorhandenen Banner-Seiten.

- durchsucht docs/banner/*.md (ohne index.md & gallery.md)
- liest YAML-Frontmatter:
    - nummer  (Sortierschlüssel, numerisch; absteigend)
    - title/titel/name (Beschriftung)
    - picture (Bild-URL; Pflicht)
- erzeugt eine **einspaltige** Galerie (ein Bild pro Zeile)
  Klick auf das Bild öffnet die Banner-Seite: /banner/<stem>/
- Bilder werden lazy geladen

Aufruf:
  python scripts/make_banner_gallery.py --root docs --banner_dir banner --outfile gallery.md
"""

import re
import sys
import argparse
from pathlib import Path

try:
    import yaml  # PyYAML
except ImportError:
    print("ERROR: PyYAML not installed. Run:  pip install pyyaml", file=sys.stderr)
    sys.exit(1)

PICTURE_KEYS = ["picture"]  # ggf. erweitern: ["picture", "image", "pic_url", "picture_url"]


def read_frontmatter(md_path: Path) -> dict:
    """Liest YAML-Frontmatter (--- ... ---) aus einer Markdown-Datei."""
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("\n", 1)[1]
    if "---" not in parts:
        return {}
    yaml_block, _rest = parts.split("---", 1)
    try:
        data = yaml.safe_load(yaml_block) or {}
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def first_non_empty(d: dict, keys: list[str], default="") -> str:
    for k in keys:
        v = d.get(k)
        if v is None:
            continue
        s = str(v).strip()
        if s:
            return s
    return default


def to_int(value, default=0) -> int:
    try:
        s = str(value).strip()
        m = re.match(r"^-?\d+", s)
        if m:
            return int(m.group(0))
        return int(s)
    except Exception:
        return default


def collect_items(banner_dir: Path) -> list[dict]:
    items = []
    for md in sorted(banner_dir.glob("*.md")):
        base = md.name.lower()
        if base in ("index.md", "gallery.md"):
            continue

        fm = read_frontmatter(md)
        if not fm:
            continue

        nummer = to_int(fm.get("nummer", 0), 0)
        title = first_non_empty(fm, ["title", "titel", "name"], md.stem)
        picture = first_non_empty(fm, PICTURE_KEYS, "")

        if not picture:
            continue

        # Link zur Seite (Clean URLs)
        link = f"/banner/{md.stem}/"

        items.append({
            "nummer": nummer,
            "title": title,
            "picture": picture,
            "link": link,
            "file": md.name,
        })

    # nach nummer DESC sortieren (größte oben)
    items.sort(key=lambda x: x["nummer"], reverse=True)
    return items


def render_single_column_md(items: list[dict]) -> str:
    """
    Rendert eine **einspaltige** Galerie.
    Nutzt Inline-Styles, um Theme-Grids/Flex zu übersteuern.
    """
    lines = []
    lines.append("---")
    lines.append('title: "Banner Galerie"')
    lines.append("---")
    lines.append("")
    lines.append("# Banner Galerie")
    lines.append("")

    # Container explizit block-level, volle Breite
    lines.append('<div class="banner-gallery-onecol" style="display:block;width:100%;max-width:1000px;margin:0 auto;">')

    for it in items:
        alt = f"#{it['nummer']} — {it['title']}"
        # Jede Karte ist block-level und räumt Floats/Flex
        lines.append(
            '<div class="banner-item" '
            'style="display:block;width:100%;clear:both;margin:0 0 20px 0;">'
        )
        lines.append(
            f'  <a href="{it["link"]}" '
            'style="display:block;width:100%;text-decoration:none;border:0;outline:0;">'
        )
        # Figure ebenfalls block-level
        lines.append('    <figure style="display:block;width:100%;margin:0;">')
        # Bild: block, 100% Breite, lazy + async
        lines.append(
            '      <img src="{src}" alt="{alt}" loading="lazy" decoding="async" '
            'style="display:block;width:100%;height:auto;border-radius:10px;"/>'
            .format(src=it["picture"], alt=alt.replace('"', "&quot;"))
        )
        lines.append(
            '      <figcaption style="display:block;width:100%;margin-top:8px;'
            'font-size:1rem;opacity:0.9;">'
        )
        lines.append('        <strong>#{nummer}</strong> — {title}'.format(
            nummer=it["nummer"], title=it["title"])
        )
        lines.append('      </figcaption>')
        lines.append('    </figure>')
        lines.append('  </a>')
        lines.append('</div>')

    lines.append("</div>")
    lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="docs", help="Docs root (default: docs)")
    ap.add_argument("--banner_dir", default="banner", help="Banner-Unterordner (default: banner -> docs/banner)")
    ap.add_argument("--outfile", default="gallery.md", help="Zieldatei in banner_dir (default: gallery.md)")
    args = ap.parse_args()

    root = Path(args.root)
    banner_dir = root / args.banner_dir
    if not banner_dir.exists():
        print(f"ERROR: {banner_dir} not found.", file=sys.stderr)
        sys.exit(2)

    items = collect_items(banner_dir)
    out_path = banner_dir / args.outfile
    out_path.write_text(render_single_column_md(items), encoding="utf-8")

    print(f"Gallery generated: {out_path} (items: {len(items)})")


if __name__ == "__main__":
    main()
