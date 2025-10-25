#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_banner_stats.py
- "Missionen gesamt" = `completed` der letzten Banner-Datei (chronologisch) mit `nummer`.
  Fallback: Summe der `missions`.
- 500er-Meilensteine/Jahr = aus rein kumulierten `missions` (chronologischer Lauf).
- Jahresstatistik: Missionen = Summe `missions` je Jahr.
- Zählt nur Dateien unter --banner-dir mit Frontmatter-Feld `nummer`.
- Distanzfelder werden als km interpretiert (lengthKMeters/lengthKm/...).
- Länder/Städte: komplette Tabellen (Anzahl + Anteil).
- Gesamtstatistik enthält zusätzlich: **Anzahl Länder (unique)** und **Anzahl Städte (unique)**.
- Überschreibt stats.md standardmäßig (Option --no-overwrite verhindert das).
Benötigt: pyyaml
"""
import argparse
import sys
import re
from pathlib import Path
from datetime import datetime, date
from collections import Counter, defaultdict

try:
    import yaml
except ImportError:
    print("Dieses Skript benötigt PyYAML. Installiere mit: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# --- Frontmatter robust parsen ---
FM_START = re.compile(r'^\ufeff?---\s*$', re.MULTILINE)  # erlaubt BOM
FM_END   = re.compile(r'^\s*(---|\.\.\.)\s*$', re.MULTILINE)

def parse_frontmatter(md_text: str) -> dict:
    m_start = FM_START.search(md_text)
    if not m_start:
        return {}
    m_end = FM_END.search(md_text, m_start.end())
    if not m_end:
        return {}
    yaml_text = md_text[m_start.end():m_end.start()]
    try:
        data = yaml.safe_load(yaml_text) or {}
        return data if isinstance(data, dict) else {}
    except yaml.YAMLError:
        return {}

def coalesce(*values):
    for v in values:
        if v is None: 
            continue
        if isinstance(v, str) and v.strip() == "":
            continue
        return v
    return None

def parse_int(v):
    if v is None: return None
    if isinstance(v, (int, float)):
        try: return int(v)
        except Exception: return None
    s = str(v).strip()
    # tolerant: 1.234, 2 000, +12
    s = re.sub(r'[^0-9+-]', '', s)
    if not s or s in ('+','-'): return None
    try: return int(s)
    except Exception: return None

def parse_float_km(v):
    if v is None: return 0.0
    if isinstance(v, (int, float)): return float(v)
    s = str(v).lower().replace("km","").replace("\u00a0"," ").replace(" ", "").replace(",", ".").strip()
    try:
        return float(s)
    except Exception:
        return 0.0

DATE_FMTS = (
    "%Y-%m-%d","%Y/%m/%d","%d.%m.%Y",
    "%Y-%m-%dT%H:%M:%S","%Y-%m-%d %H:%M",
    "%Y-%m-%dT%H:%M:%S%z","%Y-%m-%dT%H:%M:%S.%f%z",
    "%Y-%m-%dT%H:%M:%S.%f"
)
def parse_date_any(v):
    if v is None: return None
    if isinstance(v, date) and not isinstance(v, datetime): return v
    if isinstance(v, datetime): return v.date()
    if isinstance(v, (int, float)):
        iv = int(v)
        if 1 <= iv <= 9999: return date(iv,1,1)
    if isinstance(v, str):
        s = v.strip()
        if s.isdigit() and len(s)==4:
            return date(int(s),1,1)
        if s.endswith("Z"):
            s = s[:-1] + "+00:00"
        for fmt in DATE_FMTS:
            try: return datetime.strptime(s, fmt).date()
            except ValueError: pass
        m = re.search(r'(\d{4})-(\d{2})-(\d{2})', s)
        if m:
            try: return datetime.strptime(m.group(0), "%Y-%m-%d").date()
            except ValueError: pass
    return None

def parse_mission_day(v):
    if v is None: return 0
    if isinstance(v, bool): return 1 if v else 0
    if isinstance(v, (int, float)): return 1 if int(v)!=0 else 0
    s = str(v).strip().lower()
    if s in ("1","true","yes","ja","y","t"): return 1
    s = re.sub(r'[^0-9+-]', '', s) or '0'
    try: return 1 if int(s)!=0 else 0
    except Exception: return 0

# Felder
NUMMER_KEYS  = ("nummer","number","Nr","nr","id","ID")
DATE_KEYS    = ("date","completed_date","completed_at","done_date","finished_date")
YEAR_KEYS    = ("year","jahr")
CITY_KEYS    = ("region","city","ort","stadt")
COUNTRY_KEYS = ("country","land","nation","countryCode","country_code")
DIST_KEYS    = ("lengthKMeters","lengthKm","distance_km","km","distance","kilometer")

def find_first_key(d: dict, keys):
    for k in keys:
        if k in d:
            return d[k]
    return None

def banner_distance_km(fm: dict) -> float:
    for k in DIST_KEYS:
        if k in fm and fm.get(k) not in (None, ""):
            return parse_float_km(fm.get(k))
    return 0.0

def detect_year(fm: dict, path: Path):
    for k in DATE_KEYS:
        dt = parse_date_any(fm.get(k))
        if dt: return dt.year
        rv = fm.get(k)
        if isinstance(rv, (int,float)):
            iv = int(rv)
            if 1 <= iv <= 9999: return iv
        if isinstance(rv, str) and rv.strip().isdigit() and len(rv.strip())==4:
            return int(rv.strip())
    y = find_first_key(fm, YEAR_KEYS)
    if isinstance(y, (int,float)):
        iy = int(y)
        if 1 <= iy <= 9999: return iy
    if isinstance(y, str) and y.strip().isdigit() and len(y.strip())==4:
        return int(y.strip())
    m = re.search(r'(?<!\d)(\d{4})(?!\d)', str(path))
    if m:
        try:
            iy = int(m.group(1))
            if 1 <= iy <= 9999: return iy
        except Exception: pass
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--banner-dir", default="docs/banner", help="Ordner mit Banner-Markdown")
    ap.add_argument("--out", default="docs/banner/stats.md", help="Zieldatei für Statistik")
    ap.add_argument("--no-overwrite", action="store_true", help="Vorhandene stats.md NICHT überschreiben")
    ap.add_argument("--debug", action="store_true", help="Diagnose-Infos ausgeben")
    args = ap.parse_args()

    root = Path(".").resolve()
    banner_dir = (root / args.banner_dir).resolve()
    out_path = (root / args.out).resolve()

    if args.no_overwrite and out_path.exists():
        print(f"Stats existiert bereits und --no-overwrite gesetzt: {out_path}")
        return 0

    # Einlesen: nur Dateien mit 'nummer'
    all_md = list(banner_dir.rglob("*.md"))
    banners = []
    reasons_ignored = Counter()

    for path in all_md:
        name = path.name.lower()
        if name in ("index.md","gallery.md","stats.md") or name.startswith("_"):
            reasons_ignored["meta_file"] += 1
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(text)
        if not fm:
            reasons_ignored["no_frontmatter"] += 1
            continue

        nummer = find_first_key(fm, NUMMER_KEYS)
        if nummer is None or (isinstance(nummer, str) and nummer.strip()==""):
            reasons_ignored["no_nummer"] += 1
            continue

        dt = parse_date_any(find_first_key(fm, DATE_KEYS))
        year = detect_year(fm, path)

        missions = parse_int(fm.get("missions")) or 0
        completed = parse_int(fm.get("completed"))  # kann None sein
        km = banner_distance_km(fm)
        mday = parse_mission_day(fm.get("missionDay"))
        city = coalesce(*[fm.get(k) for k in CITY_KEYS])
        country = coalesce(*[fm.get(k) for k in COUNTRY_KEYS])

        banners.append({
            "path": path, "year": year, "date": dt,
            "missions": missions, "completed": completed,
            "km": km, "mday": mday, "city": city, "country": country
        })

    if args.debug:
        print("DEBUG: Dateien gesamt:", len(all_md))
        print("DEBUG: Banner berücksichtigt:", len(banners))
        if reasons_ignored:
            print("DEBUG: Ignoriert nach Grund:", dict(reasons_ignored))

    if not banners:
        md = ["# Banner-Statistik", "", "Keine geeigneten Banner gefunden (mit `nummer`)."]
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("\n".join(md), encoding="utf-8")
        print(f"Statistik geschrieben nach: {out_path}")
        return 0

    # Chronologisch sortieren
    def s_key(b):
        if b["date"]: k = b["date"]
        elif b["year"]: k = date(b["year"],1,1)
        else: k = date(2999,1,1)
        return (k, b["path"].name.lower())
    banners.sort(key=s_key)

    # Gesamt-Missionen aus 'completed' der letzten Datei (Fallback: Summe missions)
    last_completed = next((b["completed"] for b in reversed(banners) if b["completed"] is not None), None)

    # 500er-Meilensteine NUR aus kumulierten 'missions'
    milestones_per_year = Counter()
    cum_missions = 0
    prev_bucket = 0
    for b in banners:
        cum_missions += b["missions"]
        bucket = cum_missions // 500
        crossed = max(0, bucket - prev_bucket)
        if crossed and b["year"] is not None:
            milestones_per_year[b["year"]] += crossed
        prev_bucket = bucket

    # Zeitraum
    today = datetime.now().date()
    years_present = [b["year"] for b in banners if isinstance(b["year"], int)]
    first_year = min(years_present) if years_present else today.year
    span_years = (today.year - first_year) + 1
    months = span_years * 12 if span_years else 1

    # Gruppieren pro Jahr
    per_year = defaultdict(list)
    for b in banners:
        if isinstance(b["year"], int):
            per_year[b["year"]].append(b)

    # Summen
    total_banners = len(banners)
    total_km = sum(b["km"] for b in banners)
    total_mdays = sum(b["mday"] for b in banners)
    total_missions = last_completed if last_completed is not None else sum(b["missions"] for b in banners)

    # Unique Länder/Städte
    unique_countries = sorted({b["country"].strip() for b in banners if isinstance(b["country"], str) and b["country"].strip()})
    unique_cities    = sorted({b["city"].strip()    for b in banners if isinstance(b["city"], str)    and b["city"].strip()})
    total_unique_countries = len(unique_countries)
    total_unique_cities    = len(unique_cities)

    # Jahreswerte
    year_rows = []
    for y in sorted(per_year):
        lst = per_year[y]
        km_sum = sum(b["km"] for b in lst)
        ms_sum = sum(b["missions"] for b in lst)     # Jahres-Missionen = Summe missions
        md_sum = sum(b["mday"] for b in lst)
        year_rows.append({
            "year": y, "banners": len(lst), "missions": ms_sum, "md": md_sum,
            "km": km_sum, "milestones": milestones_per_year.get(y, 0)
        })

    # Durchschnittswerte auf Basis total_missions
    avg_banners_year  = total_banners / span_years if span_years else 0.0
    avg_banners_month = total_banners / months if months else 0.0
    avg_missions_year  = total_missions / span_years if span_years else 0.0
    avg_missions_month = total_missions / months if months else 0.0
    avg_km_year  = total_km / span_years if span_years else 0.0
    avg_km_month = total_km / months if months else 0.0

    # Länder / Städte (für Tabellen)
    countries = Counter(b["country"] for b in banners if isinstance(b["country"], str) and b["country"].strip())
    cities    = Counter(b["city"]    for b in banners if isinstance(b["city"], str)    and b["city"].strip())

    # Markdown schreiben
    md = []
    md += ["# Banner-Statistik", ""]

    # Gesamt
    md += ["## Gesamtstatistik", ""]
    md += [
        f"- **Gesamtbanner:** {total_banners}",
        f"- **Missionen gesamt:** {total_missions}",
        f"- **Gesamt km:** {total_km:.2f}",
        f"- **MissionDays gesamt:** {total_mdays}",
        f"- **Anzahl Länder (unique):** {total_unique_countries}",
        f"- **Anzahl Städte (unique):** {total_unique_cities}",
        f"- **Zeitraum:** {first_year} – {today.year} ({span_years} Jahre)",
        ""
    ]

    # Durchschnitt
    md += ["## Durchschnittsstatistik", ""]
    md += [
        f"- **Ø Banner/Jahr:** {avg_banners_year:.2f}",
        f"- **Ø Banner/Monat:** {avg_banners_month:.2f}",
        f"- **Ø Missionen/Jahr:** {avg_missions_year:.2f}",
        f"- **Ø Missionen/Monat:** {avg_missions_month:.2f}",
        f"- **Ø km/Jahr:** {avg_km_year:.2f}",
        f"- **Ø km/Monat:** {avg_km_month:.2f}",
        ""
    ]

    # Jahresstatistik
    md += ["## Jahresstatistik", ""]
    if year_rows:
        md += ["| Jahr | Banner | Missionen | MissionDays | km | 500er-Meilensteine |",
               "|----:|------:|----------:|-----------:|----:|--------------------:|"]
        for r in year_rows:
            md += [f"| {r['year']} | {r['banners']} | {r['missions']} | {r['md']} | {r['km']:.2f} | {r['milestones']} |"]
    else:
        md += ["_Keine Jahresdaten gefunden._"]
    md += [""]

    # Länder
    md += ["## Länder (nach Anzahl Banner)", ""]
    if countries:
        total = total_banners if total_banners else 1
        md += ["| Land | Banner | Anteil |", "|:-----|------:|------:|"]
        for c, v in sorted(countries.items(), key=lambda x: (-x[1], str(x[0]).lower())):
            pct = 100.0 * v / total
            md += [f"| {c} | {v} | {pct:.1f}% |"]
    else:
        md += ["_Keine Länder gefunden._"]
    md += [""]

    # Städte
    md += ["## Städte (nach Anzahl Banner)", ""]
    if cities:
        total = total_banners if total_banners else 1
        md += ["| Stadt | Banner | Anteil |", "|:------|------:|------:|"]
        for c, v in sorted(cities.items(), key=lambda x: (-x[1], str(x[0]).lower())):
            pct = 100.0 * v / total
            md += [f"| {c} | {v} | {pct:.1f}% |"]
    else:
        md += ["_Keine Städte gefunden._"]
    md += [""]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(md), encoding="utf-8")
    print(f"Statistik geschrieben nach: {out_path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
