#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Poste Banner-Markdowns als Telegram-Fotoposts – ausschließlich gesteuert über eine persistente Post-Liste.

Kerneigenschaften:
- Persistente Tracking-Datei: data/posted.yml
  - Struktur: posted: [ "<slug1>", "<slug2>", ... ]  (Slug = Dateiname ohne .md)
  - Banner, deren Slug bereits gelistet ist, werden NICHT erneut gepostet.
  - Nach erfolgreichem Post wird der Slug hinzugefügt und Datei sofort gespeichert.

- Frontmatter wird NICHT mehr aktualisiert (kein tg_posted etc.).
- Template aus Datei: templates/tg_caption_template.txt (override via --caption-template-file)
- Hyperlinks in Caption (HTML parse_mode), inkl. Bannergress-Link, sonst Fallback auf interne Seite.
- Limit: max. N Posts pro Lauf (--max-posts, Default 5; Env MAX_POSTS)
- 5 Sekunden Pause zwischen Posts (konfigurierbar).
- Sortierung nach 'number/nummer/num' (numerisch), dann lexikografisch.

ENV:
- TELEGRAM_BOT_TOKEN  (z. B. 1234567890:AA... )
- TELEGRAM_CHAT_ID    (z. B. -1001234567890 oder @DeinChannel)
- MAX_POSTS           (optional)
- BASE_SITE_URL       (optional, Default https://r3f1s-on-tour.github.io/banner/)

Template-Beispiel (templates/tg_caption_template.txt):
<b>{title}</b>

<b>Banner-Nr:</b> {banner}
<b>Unique Mission Completed:</b> {completed} (+{missions})
<b>Place:</b> {region},{country}

<a href="{link}">Link</a>
"""

import argparse
import glob
import os
import re
import time
from typing import Dict, Tuple, Any, List, Set
import requests
import yaml

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
TELEGRAM_CAPTION_MAX = 1024

# Fallback-Template nur wenn Datei fehlt/leer
FALLBACK_TEMPLATE = (
    "<b>{title}</b>\n\n"
    "<b>Banner-Nr:</b> {banner}\n"
    "<b>Unique Mission Completed:</b> {completed} (+{missions})\n"
    "<b>Place:</b> {region},{country}\n\n"
    "{link_html}"
).strip()


# ---------- Datei I/O ----------

def load_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def dump_text(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


# ---------- Markdown Frontmatter ----------

def parse_frontmatter(md_text: str) -> Tuple[Dict[str, Any], str, bool]:
    """
    Liefert (frontmatter, body, has_frontmatter).
    """
    m = FRONTMATTER_RE.match(md_text)
    if not m:
        return {}, md_text, False
    fm_raw = m.group(1)
    try:
        fm = yaml.safe_load(fm_raw) or {}
        if not isinstance(fm, dict):
            fm = {}
    except Exception:
        fm = {}
    body = md_text[m.end():]
    return fm, body, True


# ---------- Utilities ----------

def html_escape(s: str) -> str:
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def first_non_empty(*vals):
    for v in vals:
        if isinstance(v, str) and v.strip():
            return v.strip()
        if isinstance(v, (int, float)):
            return str(v)
        if isinstance(v, list) and v:
            for it in v:
                if isinstance(it, str) and it.strip():
                    return it.strip()
    return ""

def extract_photo_url(fm: Dict[str, Any]) -> str:
    # unterstützt: pic_url, picture, picture_url, image, img, images[0]
    return first_non_empty(
        fm.get("pic_url"),
        fm.get("picture"),
        fm.get("picture_url"),
        fm.get("image"),
        fm.get("img"),
        (fm.get("images") or [None])[0] if isinstance(fm.get("images"), list) else "",
    )

def number_from_fm(fm: Dict[str, Any]) -> int:
    for key in ("number", "nummer", "num"):
        if key in fm:
            try:
                return int(str(fm[key]).strip())
            except Exception:
                pass
    return 0

def compute_link_for_path(path: str, base_url: str) -> str:
    slug = os.path.splitext(os.path.basename(path))[0]
    if not base_url.endswith("/"):
        base_url += "/"
    return f"{base_url}{slug}/"


# ---------- Posted-Tracking ----------

def load_posted_set(posted_file: str) -> Set[str]:
    """
    Lädt data/posted.yml mit Struktur:
    posted:
      - slug1
      - slug2
    """
    if not os.path.exists(posted_file):
        return set()
    try:
        data = yaml.safe_load(load_text(posted_file)) or {}
        if isinstance(data, dict) and isinstance(data.get("posted"), list):
            return set(str(x) for x in data["posted"])
        if isinstance(data, list):
            return set(str(x) for x in data)
    except Exception:
        pass
    return set()

def save_posted_set(posted_file: str, posted_slugs: Set[str]) -> None:
    payload = {"posted": sorted(posted_slugs)}
    dump_text(posted_file, yaml.safe_dump(payload, sort_keys=False, allow_unicode=True))


# ---------- Caption-Erzeugung ----------

def build_caption(fm: Dict[str, Any], body: str, template: str, link: str) -> str:
    """
    Unterstützt im Template u.a.:
    {title}, {banner}, {completed}, {missions}, {region}, {country}, {link}
    weitere: {date}, {lengthKMeters}/{distance}, {description}, {link_html}, {body}
    """
    def get(*keys: str, default: str = "") -> str:
        for k in keys:
            v = fm.get(k)
            if isinstance(v, str) and v.strip():
                return v.strip()
            if isinstance(v, (int, float)):
                return str(v)
        return default

    title = get("title", "titel", "name")
    banner = get("banner", "nummer", "number", "num")
    region = get("region", "city")
    country = get("country", "land")
    date = get("date")
    completed = get("completed")
    missions = get("missions")
    distance = get("lengthKMeters", "distance_km", "distance")
    description = get("description")
    bg_link = get("bg-link", "link")

    # Link HTML: bevorzugt Bannergress
    if bg_link:
        link_html = f'<a href="{bg_link}">Open in Bannergress</a>'
    else:
        link_html = f'<a href="{link}">Open details</a>'

    class _SafeDict(dict):
        def __missing__(self, key): return ""

    mapping = _SafeDict({
        "title": title,
        "banner": banner,
        "completed": completed,
        "missions": missions,
        "region": region,
        "country": country,
        "link": link,
        "date": date,
        "lengthKMeters": distance,
        "distance": distance,
        "description": description,
        "bg-link": bg_link,
        "link_html": link_html,
        "body": (body or "").strip(),
    })

    raw = template.format_map(mapping)
    escaped = html_escape(raw)
    # <b>, <i>, <a> zulassen
    escaped = (escaped
               .replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>")
               .replace("&lt;i&gt;", "<i>").replace("&lt;/i&gt;", "</i>")
               .replace("&lt;a ", "<a ").replace("&lt;/a&gt;", "</a>")
               .replace("&gt;", ">").replace("&quot;", '"'))
    if len(escaped) > TELEGRAM_CAPTION_MAX:
        escaped = escaped[:TELEGRAM_CAPTION_MAX - 1] + "…"
    return escaped


# ---------- Telegram ----------

def send_telegram_photo(token: str, chat_id: str, photo_url: str, caption_html: str):
    api_url = f"https://api.telegram.org/bot{token}/sendPhoto"
    payload = {
        "chat_id": chat_id,  # numerisch oder @username
        "photo": photo_url,
        "caption": caption_html,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }
    resp = requests.post(api_url, data=payload, timeout=30)
    if resp.status_code != 200:
        raise RuntimeError(f"Telegram API error {resp.status_code}: {resp.text}")
    return resp.json()


# ---------- Verarbeiten einer Datei ----------

def process_file(path: str, slug: str, token: str, chat_id: str,
                 template: str, base_url: str, dry_run: bool=False) -> bool:
    text = load_text(path)
    fm, body, _ = parse_frontmatter(text)

    photo_url = extract_photo_url(fm)
    if not photo_url or not str(photo_url).startswith(("http://", "https://")):
        print(f"[WARN] {path}: keine gültige Bild-URL gefunden – überspringe.")
        return False

    link = compute_link_for_path(path, base_url)
    caption = build_caption(fm, body, template, link)

    if dry_run:
        print(f"[DRY] Würde posten: {os.path.basename(path)} -> {photo_url} | {link}")
    else:
        _ = send_telegram_photo(token, chat_id, photo_url, caption)
        print(f"[OK ] Gepostet: {os.path.basename(path)}")

    return True


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser(description="Poste ungepostete Banner-Markdowns zu Telegram (mit persistenter posted.yml, ohne Frontmatter-Änderungen).")
    ap.add_argument("--glob", default="docs/banner/*.md", help="Glob-Pattern der Markdown-Dateien.")
    ap.add_argument("--sleep-seconds", type=int, default=5, help="Wartezeit zwischen Posts.")
    ap.add_argument("--caption-template-file", default="templates/tg_caption_template.txt",
                    help="Pfad zur Template-Datei (Default: templates/tg_caption_template.txt).")
    ap.add_argument("--max-posts", type=int, default=int(os.getenv("MAX_POSTS", "1000")),
                    help="Maximale Anzahl an Posts pro Lauf (Default 1000; Env MAX_POSTS).")
    ap.add_argument("--base-url", default=os.getenv("BASE_SITE_URL", "https://r3f1s-on-tour.github.io/banner/"),
                    help="Basis-URL zur Seitenerzeugung (Default env BASE_SITE_URL oder feste Standard-URL).")
    ap.add_argument("--posted-file", default="data/posted.yml", help="Pfad zur Tracking-Datei (Default: data/posted.yml).")
    ap.add_argument("--dry-run", action="store_true", help="Nur anzeigen, nicht wirklich posten.")
    args = ap.parse_args()

    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        print("[ERR] TELEGRAM_BOT_TOKEN oder TELEGRAM_CHAT_ID fehlt in den Umgebungsvariablen.")
        raise SystemExit(1)

    # Template laden
    try:
        template = load_text(args.caption_template_file).strip()
        if not template:
            print(f"[WARN] Template-Datei ist leer, nutze Fallback-Template.")
            template = FALLBACK_TEMPLATE
    except Exception as e:
        print(f"[WARN] Konnte Template-Datei nicht laden ({e}), nutze Fallback-Template.")
        template = FALLBACK_TEMPLATE

    # posted.yml laden
    posted_slugs = load_posted_set(args.posted_file)

    # Kandidaten bestimmen (nur anhand posted.yml)
    paths = sorted(glob.glob(args.glob))
    candidates: List[Tuple[int, str, str]] = []  # (nummer, path, slug)

    for p in paths:
        slug = os.path.splitext(os.path.basename(p))[0]
        if slug in posted_slugs:
            continue  # schon gepostet
        try:
            fm, _, _ = parse_frontmatter(load_text(p))
        except Exception:
            fm = {}
        n = number_from_fm(fm)
        candidates.append((n, p, slug))

    if not candidates:
        print("[INFO] Nichts zu posten. Entweder keine Dateien gefunden oder alle in posted.yml enthalten.")
        return

    # Sortierung: numerisch nach Nummer, dann lexikografisch
    candidates.sort(key=lambda t: (t[0], t[1]))
    max_posts = max(0, int(args.max_posts))

    print(f"[INFO] Kandidaten: {len(candidates)} | Poste max: {max_posts}")
    posted_now = 0

    for idx, (_, path, slug) in enumerate(candidates, start=1):
        if posted_now >= max_posts:
            break
        try:
            changed = process_file(
                path=path,
                slug=slug,
                token=token,
                chat_id=chat_id,
                template=template,
                base_url=args.base_url,
                dry_run=args.dry_run
            )
            if changed and not args.dry_run:
                posted_slugs.add(slug)
                # posted.yml sofort fortschreiben (robust bei Abbrüchen)
                save_posted_set(args.posted_file, posted_slugs)
                posted_now += 1
        except Exception as e:
            print(f"[ERR] Fehler beim Posten von {path}: {e}")
        if posted_now < max_posts and idx < len(candidates):
            time.sleep(max(0, args.sleep_seconds))

    # Finale Sicherung (idempotent)
    if not args.dry_run:
        save_posted_set(args.posted_file, posted_slugs)

    print(f"[DONE] Abgeschlossen. Gepostet: {posted_now}/{len(candidates)} (Limit {max_posts}). Tracking in {args.posted_file} aktualisiert.")


if __name__ == "__main__":
    main()
