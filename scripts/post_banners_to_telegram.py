#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Poste Banner-Markdowns als Telegram-Fotoposts, wenn die Frontmatter-Variable (z.B. 'tg_posted')
nicht vorhanden oder nicht True ist. Nach erfolgreichem Posten wird das Flag auf True gesetzt.

Features:
- Unterstützt deutsche Felder (z.B. 'nummer', 'titel', 'region', 'country', 'missions', 'completed').
- Erzeugt 'link' = BASE_URL + <filename-ohne-endung> + '/' für Template.
- Optionales 'link_html' mit <a href="…">…</a> (Bannergress, sonst Fallback auf 'link').
- Template aus Datei: templates/tg_caption_template.txt (override via --caption-template-file).
- Limit: max. N Posts pro Lauf (--max-posts, Default 5; override per Env MAX_POSTS).
- 5 Sekunden Pause zwischen Posts (konfigurierbar).
- Sortierung nach 'number/nummer/num' (numerisch), dann lexikografisch nach Dateiname.

Erforderliche ENV:
- TELEGRAM_BOT_TOKEN  (z.B. 1234567890:AA... )
- TELEGRAM_CHAT_ID    (z.B. -1001234567890 ODER @deinchannel)

Optionale ENV:
- MAX_POSTS           (Default 5)
- BASE_SITE_URL       (Default https://r3f1s-on-tour.github.io/banner/)

Beispiel-Template (templates/tg_caption_template.txt):
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
from typing import Dict, Tuple, Any, List
import requests
import yaml

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
TELEGRAM_CAPTION_MAX = 1024

# Fallback-Template nur für den absoluten Notfall (Datei fehlt/leer)
FALLBACK_TEMPLATE = (
    "<b>{title}</b>\n\n"
    "<b>Banner-Nr:</b> {banner}\n"
    "<b>Unique Mission Completed:</b> {completed} (+{missions})\n"
    "<b>Place:</b> {region},{country}\n\n"
    "{link_html}"
).strip()


# ---------- I/O Hilfsfunktionen ----------

def load_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def dump_text(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

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

def serialize_frontmatter(fm: Dict[str, Any]) -> str:
    text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{text}\n---\n"

def replace_frontmatter(md_text: str, new_fm: Dict[str, Any]) -> str:
    m = FRONTMATTER_RE.match(md_text)
    header = serialize_frontmatter(new_fm)
    if not m:
        return header + md_text
    return header + md_text[m.end():]

def html_escape(s: str) -> str:
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---------- Frontmatter-Utilities ----------

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

def safe_bool(v: Any) -> bool:
    if isinstance(v, bool):
        return v
    if isinstance(v, (int, float)):
        return bool(v)
    if isinstance(v, str):
        return v.strip().lower() in ("1", "true", "yes", "y", "on")
    return False

def compute_link_for_path(path: str, base_url: str) -> str:
    slug = os.path.splitext(os.path.basename(path))[0]
    if not base_url.endswith("/"):
        base_url += "/"
    return f"{base_url}{slug}/"


# ---------- Caption-Erzeugung ----------

def build_caption(fm: Dict[str, Any], body: str, template: str, link: str) -> str:
    """
    Baut die Caption anhand des Templates.
    Unterstützt genau die vom Nutzer gewünschten Keys:
      {title}, {banner}, {completed}, {missions}, {region}, {country}, {link}
    sowie zusätzliche: {date}, {lengthKMeters}/{distance}, {link_html}, {body}
    """
    def get(*keys: str, default: str = "") -> str:
        for k in keys:
            v = fm.get(k)
            if isinstance(v, str) and v.strip():
                return v.strip()
            if isinstance(v, (int, float)):
                return str(v)
        return default

    # Titel (de/en)
    title = get("title", "titel", "name")
    # Nummer/Banner
    banner = get("banner", "nummer", "number", "num")
    # Ort
    region = get("region", "city")
    country = get("country", "land")
    # Zusatz
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
        # exakt für dein Template
        "title": title,
        "banner": banner,
        "completed": completed,
        "missions": missions,
        "region": region,
        "country": country,
        "link": link,

        # optional weiter nutzbar
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
    # <b>, <i>, <a> wieder erlauben
    escaped = (escaped
               .replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>")
               .replace("&lt;i&gt;", "<i>").replace("&lt;/i&gt;", "</i>")
               .replace("&lt;a ", "<a ").replace("&lt;/a&gt;", "</a>")
               .replace("&gt;", ">").replace("&quot;", '"'))
    # Telegram Caption Limit
    if len(escaped) > TELEGRAM_CAPTION_MAX:
        escaped = escaped[:TELEGRAM_CAPTION_MAX - 1] + "…"
    return escaped


# ---------- Telegram Senden ----------

def send_telegram_photo(token: str, chat_id: str, photo_url: str, caption_html: str):
    api_url = f"https://api.telegram.org/bot{token}/sendPhoto"
    payload = {
        "chat_id": chat_id,          # kann numerisch ODER @username sein
        "photo": photo_url,
        "caption": caption_html,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }
    resp = requests.post(api_url, data=payload, timeout=30)
    if resp.status_code != 200:
        raise RuntimeError(f"Telegram API error {resp.status_code}: {resp.text}")
    return resp.json()


# ---------- Datei-Workflow ----------

def process_file(path: str, flag_key: str, token: str, chat_id: str,
                 template: str, base_url: str, dry_run: bool=False) -> bool:
    text = load_text(path)
    fm, body, _ = parse_frontmatter(text)

    # Schon gepostet?
    if safe_bool(fm.get(flag_key)):
        return False

    # Bild ermitteln
    photo_url = extract_photo_url(fm)
    if not photo_url or not str(photo_url).startswith(("http://", "https://")):
        print(f"[WARN] {path}: keine gültige Bild-URL gefunden – überspringe.")
        return False

    # Link berechnen und Caption bauen
    link = compute_link_for_path(path, base_url)
    caption = build_caption(fm, body, template, link)

    # Senden
    if dry_run:
        print(f"[DRY] Würde posten: {os.path.basename(path)} -> {photo_url} | {link}")
    else:
        _ = send_telegram_photo(token, chat_id, photo_url, caption)
        print(f"[OK ] Gepostet: {os.path.basename(path)}")

    # Flag setzen
    fm[flag_key] = True
    new_text = replace_frontmatter(text, fm)
    dump_text(path, new_text)
    return True


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser(description="Poste ungepostete Banner-Markdowns zu Telegram.")
    ap.add_argument("--glob", default="docs/banner/*.md",
                    help="Glob-Pattern der Markdown-Dateien.")
    ap.add_argument("--flag-key", default="tg_posted",
                    help="Frontmatter-Flag-Name (als True markiert nach Post).")
    ap.add_argument("--sleep-seconds", type=int, default=5,
                    help="Wartezeit zwischen Posts.")
    ap.add_argument("--caption-template-file", default="templates/tg_caption_template.txt",
                    help="Pfad zur Template-Datei (Default: templates/tg_caption_template.txt).")
    ap.add_argument("--max-posts", type=int, default=int(os.getenv("MAX_POSTS", "5")),
                    help="Maximale Anzahl an Posts pro Lauf (Default 5; Env MAX_POSTS).")
    ap.add_argument("--base-url", default=os.getenv("BASE_SITE_URL", "https://r3f1s-on-tour.github.io/banner/"),
                    help="Basis-URL zur Seitenerzeugung (Default env BASE_SITE_URL oder feste Standard-URL).")
    ap.add_argument("--dry-run", action="store_true",
                    help="Nur anzeigen, nicht wirklich posten.")
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

    paths = sorted(glob.glob(args.glob))

    # Kandidaten (Flag fehlt oder ist false)
    candidates: List[Tuple[int, str]] = []
    for p in paths:
        try:
            fm, _, _ = parse_frontmatter(load_text(p))
        except Exception:
            fm = {}
        if not safe_bool(fm.get(args.flag_key)):
            n = number_from_fm(fm)  # natürliche Sortierung nach Nummer
            candidates.append((n, p))

    if not candidates:
        print("[INFO] Nichts zu posten. Alle Einträge sind bereits markiert.")
        return

    # Sortieren: numerisch nach Nummer, bei Gleichstand lexikografisch
    candidates.sort(key=lambda t: (t[0], t[1]))
    max_posts = max(0, int(args.max_posts))

    print(f"[INFO] Kandidaten: {len(candidates)} | Poste max: {max_posts}")
    posted = 0

    for idx, (_, path) in enumerate(candidates, start=1):
        if posted >= max_posts:
            break
        try:
            changed = process_file(
                path=path,
                flag_key=args.flag_key,
                token=token,
                chat_id=chat_id,
                template=template,
                base_url=args.base_url,
                dry_run=args.dry_run
            )
            if changed:
                posted += 1
        except Exception as e:
            print(f"[ERR] Fehler beim Posten von {path}: {e}")
        # Pause zwischen Posts (außer ggf. nach dem letzten/Limit erreicht)
        if posted < max_posts and idx < len(candidates):
            time.sleep(max(0, args.sleep_seconds))

    print(f"[DONE] Abgeschlossen. Gepostet/gekennzeichnet: {posted}/{len(candidates)} (Limit {max_posts}).")


if __name__ == "__main__":
    main()
