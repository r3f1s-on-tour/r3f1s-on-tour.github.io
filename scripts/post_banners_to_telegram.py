#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Poste Banner-Markdowns als Telegram-Fotoposts – gesteuert über data/posted.yml.

Highlights:
- Persistente Tracking-Datei: data/posted.yml (posted: [ "<slug>", ... ])
- Keine Frontmatter-Updates.
- Template: template/tg_caption_template.txt (override via --caption-template-file)
- Klickbare Links:
  * Template enthält z. B. <a href="{link}">Link</a>
  * {link} wird HTML-ATTRIBUT-sicher eingesetzt (href-konform: & -> &amp;, " -> &quot;, <, >, ')
  * Keine globale Escapes -> <a> bleibt erhalten
  * Nur {description} wird ggf. gekürzt (Tags bleiben unberührt)
- Sortierung: number/nummer/num (numerisch), dann lexikografisch
- Limit: --max-posts (Default 5), Sleep: --sleep-seconds (Default 5)
- Optional: --prefer-bannergress (Standard False -> deine Website hat Vorrang)

ENV:
- TELEGRAM_BOT_TOKEN
- TELEGRAM_CHAT_ID
- MAX_POSTS (optional)
- BASE_SITE_URL (optional, Default https://r3f1s-on-tour.github.io/banner/)
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
TELEGRAM_CAPTION_MAX = 1024  # konservativ

FALLBACK_TEMPLATE = (
    "<b>{title}</b>\n\n"
    "<b>Banner-Nr:</b> {banner}\n"
    "<b>Unique Mission Completed:</b> {completed} (+{missions})\n"
    "<b>Place:</b> {region},{country}\n\n"
    '<a href="{link}">Link</a>'
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

def html_text_escape(s: str) -> str:
    """Escape für Textknoten (sichtbarer Text)."""
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def html_attr_escape(s: str) -> str:
    """Escape für HTML-Attribute (z. B. href="...")."""
    s = s or ""
    s = s.replace("&", "&amp;")
    s = s.replace('"', "&quot;")
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    s = s.replace("'", "&#39;")
    return s

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


# ---------- Caption-Erzeugung (Hyperlink sicher & klickbar) ----------

def build_caption(fm: Dict[str, Any], body: str, template: str, link: str, prefer_bannergress: bool) -> str:
    """
    - Template bleibt unverändert (enthält <a href="{link}">…</a>).
    - Text-Platzhalter einzeln escapen (html_text_escape).
    - {link} für href-Attribut escapen (html_attr_escape), damit Telegram ihn akzeptiert.
    - Länge wird ausschließlich über Kürzen von {description} eingehalten.
    """
    def get(*keys: str, default: str = "") -> str:
        for k in keys:
            v = fm.get(k)
            if isinstance(v, str) and v.strip():
                return v.strip()
            if isinstance(v, (int, float)):
                return str(v)
        return default

    # Rohwerte
    title_raw   = get("title", "titel", "name")
    banner_raw  = get("banner", "nummer", "number", "num")
    region_raw  = get("region", "city")
    country_raw = get("country", "land")
    date_raw    = get("date")
    completed_raw = get("completed")
    missions_raw  = get("missions")
    distance_raw  = get("lengthKMeters", "distance_km", "distance")
    desc_raw      = get("description")
    bg_link_raw   = get("bg-link", "link")

    # Linkziel (Standard: interne Seite)
    link_target = bg_link_raw if (prefer_bannergress and bg_link_raw) else link
    if not (link_target.startswith("http://") or link_target.startswith("https://")):
        link_target = "https://" + link_target.lstrip("/")

    # Escaping
    T = html_text_escape
    mapping_base = {
        "title": T(title_raw),
        "banner": T(banner_raw),
        "completed": T(completed_raw),
        "missions": T(missions_raw),
        "region": T(region_raw),
        "country": T(country_raw),
        "date": T(date_raw),
        "lengthKMeters": T(distance_raw),
        "distance": T(distance_raw),
        "description": T(desc_raw),
        "bg-link": T(bg_link_raw),
        "body": T((body or "").strip()),
        # WICHTIG: href-Attribut-sicher
        "link": html_attr_escape(link_target),
    }

    class _SafeDict(dict):
        def __missing__(self, key): return ""

    # Fit-Schleife: kürze nur description, niemals hart am Ende abschneiden
    description = mapping_base["description"]
    while True:
        mapping = dict(mapping_base)
        mapping["description"] = description
        rendered = template.format_map(_SafeDict(mapping))
        if len(rendered) <= TELEGRAM_CAPTION_MAX:
            return rendered
        if not description:
            # keine Beschreibung mehr -> fertig
            return template.format_map(_SafeDict({**mapping, "description": ""}))
        # heuristisch: 10% kürzen (min. 8 Zeichen)
        cut = max(8, int(len(description) * 0.10))
        description = description[:-cut]


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
                 template: str, base_url: str, prefer_bannergress: bool,
                 dry_run: bool=False) -> bool:
    text = load_text(path)
    fm, body, _ = parse_frontmatter(text)

    photo_url = extract_photo_url(fm)
    if not photo_url or not str(photo_url).startswith(("http://", "https://")):
        print(f"[WARN] {path}: keine gültige Bild-URL gefunden – überspringe.")
        return False

    link = compute_link_for_path(path, base_url)
    caption = build_caption(fm, body, template, link, prefer_bannergress)

    if dry_run:
        print(f"[DRY] Würde posten: {os.path.basename(path)}")
        print(f"      Photo: {photo_url}")
        print(f"      Link : {link}")
        print("------ Caption (HTML) ------")
        print(caption)
        print("----------------------------")
    else:
        _ = send_telegram_photo(token, chat_id, photo_url, caption)
        print(f"[OK ] Gepostet: {os.path.basename(path)}")

    return True


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser(
        description="Poste Banner-Markdowns zu Telegram (posted.yml, kein Frontmatter).",
        allow_abbrev=False
    )
    ap.add_argument("--glob", default="docs/banner/*.md", help="Glob-Pattern der Markdown-Dateien.")
    ap.add_argument("--sleep-seconds", type=int, default=5, help="Wartezeit zwischen Posts.")
    ap.add_argument("--caption-template-file", default="template/tg_caption_template.txt",
                    help="Pfad zur Template-Datei (Default: template/tg_caption_template.txt).")
    ap.add_argument("--max-posts", type=int, default=int(os.getenv("MAX_POSTS", "5")),
                    help="Maximale Anzahl an Posts pro Lauf (Default 5; Env MAX_POSTS).")
    ap.add_argument("--base-url", default=os.getenv("BASE_SITE_URL", "https://r3f1s-on-tour.github.io/banner/"),
                    help="Basis-URL zur Seitenerzeugung (Default env BASE_SITE_URL oder feste Standard-URL).")
    ap.add_argument("--posted-file", default="data/posted.yml", help="Pfad zur Tracking-Datei (Default: data/posted.yml).")
    ap.add_argument("--prefer-bannergress", action="store_true",
                    help="Wenn gesetzt, bevorzugt {link} den bg-link der Frontmatter (falls vorhanden).")
    ap.add_argument("--dry-run", action="store_true", help="Nur anzeigen, nicht wirklich posten.")
    # Rückwärtskompatibel: altes Flag akzeptieren & ignorieren
    ap.add_argument("--flag-key", default=None, help="(deprecated) Wird ignoriert – Tracking erfolgt über data/posted.yml.")
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
            print("[WARN] Template-Datei ist leer, nutze Fallback-Template.")
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
                prefer_bannergress=args.prefer_bannergress,
                dry_run=args.dry_run
            )
            if changed and not args.dry_run:
                posted_slugs.add(slug)
                save_posted_set(args.posted_file, posted_slugs)
                posted_now += 1
        except Exception as e:
            print(f"[ERR] Fehler beim Posten von {path}: {e}")
        if posted_now < max_posts and idx < len(candidates):
            time.sleep(max(0, args.sleep_seconds))

    if not args.dry_run:
        save_posted_set(args.posted_file, posted_slugs)

    print(f"[DONE] Abgeschlossen. Gepostet: {posted_now}/{len(candidates)} (Limit {max_posts}). Tracking in {args.posted_file} aktualisiert.")


if __name__ == "__main__":
    main()
