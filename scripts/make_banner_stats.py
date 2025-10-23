#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_banner_stats.py
- Überschreibt stats.md standardmäßig (Option --no-overwrite verhindert das).
- Erkennt Datum robust (ISO, d.m.Y, nur Jahreszahl, mit/ohne Zeitzone).
- Zeitraum: vom ersten erkannten Banner-Jahr bis heute (Jahre = inklusive Zählung).
- Rekursives Scannen von docs/banner (Unterordner inkl.).
- **Filter**: Es werden ausschließlich Banner-Dateien berücksichtigt, deren Frontmatter ein Feld 'nummer' besitzt
  (mit Fallbacks für gängige Variationen; siehe code).
- Jahresstatistik: Jahr, Banner, Missionen, MissionDays, km gesamt, 500er-Meilensteine (aus kumulativem 'completed').
- Länder- & Städte-Statistik: vollständige Tabellen mit Anzahl und prozentualem Anteil (bezogen auf Gesamtbanner).
- Durchschnittsstatistik: Banner/∅Jahr/∅Monat, Missionen/∅Jahr/∅Monat, km/∅Jahr/∅Monat.
- Gesamtstatistik: Gesamtbanner, Missionen gesamt, MissionDays gesamt, Gesamt-km, Zeitraum.
Benötigt: pyyaml
"""
import argparse
import sys
import re
import json
from pathlib import Path
from datetime import datetime, date
from collections import Counter, defaultdict

try:
    import yaml
except ImportError:
    print("Dieses Skript benötigt PyYAML. Installiere mit: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# --- Robustes Frontmatter-Parsing (--- ... --- ODER --- ... ...; auch CRLF) ---
FM_START = re.compile(r'^\ufeff?---\s*$', re.MULTILINE)  # erlaubt BOM
FM_END   = re.compile(r'^\s*(---|\.\.\.)\s*$', re.MULTILINE)

def parse_frontmatter(md_text: str) -> dict:
    # Finde Start
    m_start = FM_START.search(md_text)
    if not m_start: 
        return {}
    # Finde nächstes End
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

def parse_number(v):
    if v is None: return None
    if isinstance(v, (int, float)):
        try: return int(v)
        except Exception: return None
    s = str(v).strip()
    # +/- erlauben
    sign = 1
    if s.startswith(('+','-')):
        sign = -1 if s[0] == '-' else 1
        s = s[1:].strip()
    return sign*int(s) if s.isdigit() else None

def parse_float_km(v):
    if v is None: return 0.0
    if isinstance(v, (int, float)): return float(v)
    s = str(v).lower()
    s = s.replace("km","").replace("\u00a0"," ").replace(" ", "").replace(",", ".").strip()
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
    """Akzeptiert echtes date/datetime, Jahreszahl (int/str 'YYYY'), ISO/Local Strings."""
    if v is None:
        return None
    if isinstance(v, date) and not isinstance(v, datetime):
        return v
    if isinstance(v, datetime):
        return v.date()
    if isinstance(v, (int, float)):
        iv = int(v)
        if 1 <= iv <= 9999:
            return date(iv, 1, 1)
    if isinstance(v, str):
        s = v.strip()
        if s.isdigit() and len(s) == 4:
            # reine Jahreszahl als String
            y = int(s)
            if 1 <= y <= 9999:
                return date(y, 1, 1)
        # 'Z' → offset
        if s.endswith("Z"):
            s = s[:-1] + "+00:00"
        for fmt in DATE_FMTS:
            try:
                return datetime.strptime(s, fmt).date()
            except ValueError:
                continue
        # Fallback: YYYY-mm-dd im String
        m = re.search(r'(\d{4})-(\d{2})-(\d{2})', s)
        if m:
            try:
                return datetime.strptime(m.group(0), "%Y-%m-%d").date()
            except ValueError:
                pass
    return None

def parse_mission_day(v):
    if v is None: return 0
    if isinstance(v, bool): return 1 if v else 0
    if isinstance(v, (int, float)): return 1 if int(v) != 0 else 0
    s = str(v).strip().lower()
    if s in ("1","true","yes","ja","y","t"): return 1
    try:
        return 1 if int(s) != 0 else 0
    except Exception:
        return 0

# Distanzfelder (alle als KM interpretieren)
DIST_KEYS = ("lengthKMeters","lengthKm","distance_km","km","distance","kilometer")

def banner_distance_km(fm: dict) -> float:
    for k in DIST_KEYS:
        if k in fm and fm.get(k) not in (None, ""):
            return parse_float_km(fm.get(k))
    return 0.0

# Feldvarianten
NUMMER_KEYS = ("nummer","number","Nr","nr","id","ID")
YEAR_KEYS   = ("year","jahr")
DATE_KEYS   = ("date","completed_date","completed_at","done_date","finished_date")
CITY_KEYS   = ("region","city","ort","stadt")
COUNTRY_KEYS= ("country","land","nation","countryCode","country_code")

MISSION_KEYS = ("missions","mission_count","banner_missions")
MISSIONDAY_KEYS = ("missionDay","missionday","mission_day","missiondays")
COMPLETED_KEYS = ("completed","missions_completed_cum","completed_total")

def find_first_key(d: dict, keys):
    for k in keys:
        if k in d:
            return d[k]
    return None

def detect_year(fm: dict, path: Path):
    # 1) date-like keys
    for k in DATE_KEYS:
        dt = parse_date_any(fm.get(k))
        if dt: return dt.year
        rv = fm.get(k)
        if isinstance(rv, (int, float)):
            iv = int(rv)
            if 1 <= iv <= 9999:
                return iv
        if isinstance(rv, str) and rv.strip().isdigit() and len(rv.strip()) == 4:
            return int(rv.strip())
    # 2) explicit year keys
    y = find_first_key(fm, YEAR_KEYS)
    if isinstance(y, (int,float)):
        iy = int(y)
        if 1 <= iy <= 9999:
            return iy
    if isinstance(y, str) and y.strip().isdigit() and len(y.strip()) == 4:
        return int(y.strip())
    # 3) fallback: Jahr aus Dateiname/Pfad
    m = re.search(r'(?<!\d)(\d{4})(?!\d)', str(path))
    if m:
        try:
            iy = int(m.group(1))
            if 1 <= iy <= 9999:
                return iy
        except Exception:
            pass
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--banner-dir", default="docs/banner", help="Ordner mit Banner-Markdown")
    ap.add_argument("--out", default="docs/banner/stats.md", help="Zieldatei für Statistik")
    ap.add_argument("--no-overwrite", action="store_true", help="Vorhandene stats.md NICHT überschreiben")
    ap.add_argument("--debug", action="store_true", help="Diagnose-Infos auf STDOUT ausgeben")
    args = ap.parse_args()

    root = Path(".").resolve()
    banner_dir = (root / args.banner_dir).resolve()
    out_path = (root / args.out).resolve()

    if args.no_overwrite and out_path.exists():
        print(f"Stats existiert bereits und --no-overwrite gesetzt: {out_path}")
        return 0

    all_md = list(banner_dir.rglob("*.md"))
    fm_ok = 0
    with_nummer = 0
    included = 0
    reasons_ignored = Counter()
    sample_ignored = []

    banners = []
    for path in all_md:
        name = path.name.lower()
        if name in ("index.md","gallery.md","stats.md") or name.startswith("_"):
            reasons_ignored["meta_file"] += 1
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = path.read_text(encoding="utf-8", errors="ignore")

        fm = parse_frontmatter(text)
        if not fm:
            reasons_ignored["no_frontmatter"] += 1
            if len(sample_ignored) < 10: sample_ignored.append((str(path), "no_frontmatter"))
            continue
        fm_ok += 1

        # nummer vorhanden?
        nummer = find_first_key(fm, NUMMER_KEYS)
        if nummer is None or (isinstance(nummer, str) and nummer.strip() == ""):
            reasons_ignored["no_nummer"] += 1
            if len(sample_ignored) < 10: sample_ignored.append((str(path), "no_nummer"))
            continue
        with_nummer += 1

        # Jahr ermitteln
        year = detect_year(fm, path)
        if year is None:
            reasons_ignored["no_year"] += 1
            if len(sample_ignored) < 10: sample_ignored.append((str(path), "no_year"))
            # wir nehmen trotzdem auf, aber Jahresstatistik kann diesen nicht zählen
        # Datum (voll) optional
        dt = parse_date_any(find_first_key(fm, DATE_KEYS))

        km = banner_distance_km(fm)
        missions = parse_number(find_first_key(fm, MISSION_KEYS)) or 0
        mday = parse_mission_day(find_first_key(fm, MISSIONDAY_KEYS))
        completed = parse_number(find_first_key(fm, COMPLETED_KEYS))

        city = coalesce(*[fm.get(k) for k in CITY_KEYS])
        country = coalesce(*[fm.get(k) for k in COUNTRY_KEYS])

        banners.append({
            "path": path, "year": year, "date": dt,
            "km": km, "missions": missions, "mday": mday, "completed": completed,
            "city": city, "country": country
        })
        included += 1

    if args.debug:
        print("=== DEBUG / Diagnose ===")
        print(f"*.md gefunden:              {len(all_md)}")
        print(f"mit Frontmatter:            {fm_ok}")
        print(f"mit 'nummer' (inkl. Fallbacks): {with_nummer}")
        print(f"insgesamt einbezogen:       {included}")
        if reasons_ignored:
            print("Ignoriert (Grund → Anzahl):")
            for k, v in reasons_ignored.most_common():
                print(f"  - {k}: {v}")
        if sample_ignored:
            print("Beispiele ignorierter Dateien:")
            for p, r in sample_ignored:
                print(f"  - {p}  ({r})")
        print("=========================\n")

    # Falls nichts inkludiert wurde → früh raus + leere Tabellen
    if not banners:
        md = [
            "# Banner-Statistik", "",
            "Keine geeigneten Banner gefunden (mit `nummer`)."
        ]
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("\n".join(md), encoding="utf-8")
        print(f"Statistik geschrieben nach: {out_path}")
        return 0

    # Zeitraum
    today = datetime.now().date()
    years_present = [b["year"] for b in banners if isinstance(b["year"], int)]
    if years_present:
        first_year = min(years_present)
    else:
        # wenn gar kein Jahr erkannt wurde, nimm aktuelles Jahr
        first_year = today.year
    span_years = (today.year - first_year) + 1
    months = span_years * 12 if span_years else 1

    # Chronologisch sortieren
    def s_key(b):
        if b["date"]: k = b["date"]
        elif b["year"]: k = date(b["year"],1,1)
        else: k = date(2999,1,1)
        return (k, b["path"].name.lower())
    banners.sort(key=s_key)

    # Gruppieren nach Jahr
    per_year = defaultdict(list)
    for b in banners:
        if isinstance(b["year"], int):
            per_year[b["year"]].append(b)

    # 500er-Meilensteine
    milestones_per_year = {}
    last_cum = 0
    for y in sorted(per_year):
        max_cum_this_year = last_cum
        for b in per_year[y]:
            if b["completed"] is not None:
                max_cum_this_year = max(max_cum_this_year, b["completed"])
        milestones = (max_cum_this_year // 500) - (last_cum // 500)
        milestones_per_year[y] = max(0, milestones)
        last_cum = max_cum_this_year

    # Jahreswerte + Totale
    year_rows = []
    total_banners = 0
    total_km = 0.0
    total_missions = 0
    total_mdays = 0

    for y in sorted(per_year):
        lst = per_year[y]
        km_sum = sum(b["km"] for b in lst)
        ms_sum = sum(b["missions"] for b in lst)
        md_sum = sum(b["mday"] for b in lst)
        year_rows.append({
            "year": y, "banners": len(lst), "missions": ms_sum, "md": md_sum,
            "km": km_sum, "milestones": milestones_per_year.get(y, 0)
        })
        total_banners += len(lst)
        total_km += km_sum
        total_missions += ms_sum
        total_mdays += md_sum

    # Länder / Städte
    countries = Counter(b["country"] for b in banners if isinstance(b["country"], str) and b["country"].strip() != "")
    cities    = Counter(b["city"]    for b in banners if isinstance(b["city"], str)    and b["city"].strip()    != "")

    # Durchschnittswerte
    avg_banners_year  = total_banners / span_years if span_years else 0.0
    avg_banners_month = total_banners / months if months else 0.0
    avg_missions_year  = total_missions / span_years if span_years else 0.0
    avg_missions_month = total_missions / months if months else 0.0
    avg_km_year  = total_km / span_years if span_years else 0.0
    avg_km_month = total_km / months if months else 0.0

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

    # Länder – vollständige Tabelle
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

    # Städte – vollständige Tabelle
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
