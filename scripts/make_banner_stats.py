#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_banner_stats.py
- Überschreibt stats.md standardmäßig (Option --no-overwrite verhindert das).
- Erkennt Datum robust (Jahreszahl oder Datum).
- Zeitraum: vom ersten erkannten Banner-Jahr bis heute (Jahre = inklusive Zählung).
- Rekursives Scannen von docs/banner (Unterordner inkl.).
- **Filter**: Es werden ausschließlich Banner-Dateien berücksichtigt, deren Frontmatter ein Feld 'nummer' enthält.
- Jahresstatistik: Jahr, Banner, Missionen, MissionDays, km gesamt, 500er-Meilensteine (aus kumulativem 'completed').
- Länder- & Städte-Statistik: vollständige Tabellen mit Anzahl und prozentualem Anteil.
- Durchschnittsstatistik: Banner/∅Jahr/∅Monat, Missionen/∅Jahr/∅Monat, km/∅Jahr/∅Monat.
- Gesamtstatistik: Gesamtbanner, Missionen gesamt, MissionDays gesamt, Gesamt-km, Zeitraum.
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

FM_DELIM = re.compile(r'^---\s*$', re.MULTILINE)

def parse_frontmatter(md_text: str) -> dict:
    parts = FM_DELIM.split(md_text, maxsplit=2)
    if len(parts) >= 3 and md_text.strip().startswith('---'):
        yaml_text = parts[1]
        try:
            data = yaml.safe_load(yaml_text) or {}
            return data if isinstance(data, dict) else {}
        except yaml.YAMLError:
            return {}
    return {}

def parse_number(v):
    if v is None: return None
    if isinstance(v, (int,float)): return int(v)
    s = str(v).strip()
    if s.startswith(('+','-')):
        sign = -1 if s[0] == '-' else 1
        body = s[1:]
        return sign*int(body) if body.isdigit() else None
    return int(s) if s.isdigit() else None

def parse_date_any(v):
    if v is None: return None
    if isinstance(v, date): return v
    if isinstance(v, (int,float)) and 1 <= int(v) <= 9999:
        return date(int(v),1,1)
    s = str(v).strip()
    if s.isdigit() and len(s)==4:
        return date(int(s),1,1)
    for fmt in ("%Y-%m-%d","%Y/%m/%d","%d.%m.%Y"):
        try: return datetime.strptime(s, fmt).date()
        except Exception: pass
    return None

def parse_float_km(v):
    if v is None: return 0.0
    if isinstance(v,(int,float)): return float(v)
    s = str(v).lower().replace("km","").replace(",",".").strip()
    try: return float(s)
    except: return 0.0

def parse_mission_day(v):
    if v in (True,"true","True","yes","ja","1",1,"y","t"): return 1
    try: return 1 if int(str(v).strip()) != 0 else 0
    except Exception: return 0

def banner_distance_km(fm: dict) -> float:
    # interpretiert alle Felder als Kilometer
    for k in ("lengthKMeters","lengthKm","distance_km","km","distance","kilometer"):
        if k in fm and fm.get(k) not in (None, ""):
            return parse_float_km(fm.get(k))
    return 0.0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--banner-dir", default="docs/banner", help="Ordner mit Banner-Markdown")
    ap.add_argument("--out", default="docs/banner/stats.md", help="Zieldatei für Statistik")
    ap.add_argument("--no-overwrite", action="store_true", help="Vorhandene stats.md NICHT überschreiben")
    args = ap.parse_args()

    root = Path(".").resolve()
    banner_dir = (root / args.banner_dir).resolve()
    out_path = (root / args.out).resolve()

    if args.no_overwrite and out_path.exists():
        print(f"Stats existiert bereits und --no-overwrite gesetzt: {out_path}")
        return 0

    # Einlesen (nur Dateien mit 'nummer')
    banners = []
    for path in banner_dir.rglob("*.md"):
        name = path.name.lower()
        if name in ("index.md","gallery.md","stats.md") or name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(text)
        if not fm or "nummer" not in fm:  # nur echte Banner
            continue

        dt = parse_date_any(fm.get("date"))
        y = dt.year if dt else parse_number(fm.get("year"))

        km = banner_distance_km(fm)
        missions = parse_number(fm.get("missions")) or 0
        mday = parse_mission_day(fm.get("missionDay"))
        completed = parse_number(fm.get("completed"))  # kumulativ, für 500er
        city = fm.get("region") or fm.get("city") or fm.get("ort") or fm.get("stadt")
        country = fm.get("country") or fm.get("land") or fm.get("nation")

        banners.append({
            "path": path, "year": y, "date": dt,
            "km": km, "missions": missions, "mday": mday, "completed": completed,
            "city": city, "country": country
        })

    if not banners:
        print("Keine geeigneten Banner gefunden (mit 'nummer').")
        return 0

    # Zeitraum (erstes Banner-Jahr -> heute)
    today = datetime.now().date()
    years = [b["year"] for b in banners if b["year"]]
    first_year = min(years) if years else today.year
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
        if b["year"]:
            per_year[b["year"]].append(b)

    # 500er-Meilensteine aus kumulativem 'completed'
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
    countries = Counter(b["country"] for b in banners if b["country"])
    cities = Counter(b["city"] for b in banners if b["city"])

    # Durchschnittswerte (Jahr & Monat)
    avg_banners_year = total_banners / span_years if span_years else 0.0
    avg_banners_month = total_banners / months if months else 0.0
    avg_missions_year = total_missions / span_years if span_years else 0.0
    avg_missions_month = total_missions / months if months else 0.0
    avg_km_year = total_km / span_years if span_years else 0.0
    avg_km_month = total_km / months if months else 0.0

    # Markdown schreiben
    md = []
    md += ["# Banner-Statistik", ""]

    # Gesamt
    md += ["## Gesamtstatistik", ""]
    md += [
        f"- **Gesamtbanner:** {total_banners}",
        f"- **Missionen gesamt:** {total_missions}",
        f("- **Gesamt km:** {:.2f}".format(total_km)),
        f"- **MissionDays gesamt:** {total_mdays}",
        f"- **Zeitraum:** {first_year} – {today.year} ({span_years} Jahre)",
        ""
    ]

    # Durchschnitt
    md += ["## Durchschnittsstatistik", ""]
    md += [
        f"- **Ø Banner/Jahr:** {avg_banners_year:.2f}",
        f"- **Ø Banner/Monat:** {avg_banners_month:.2f}",
        f("- **Ø Missionen/Jahr:** {:.2f}".format(avg_missions_year)),
        f("- **Ø Missionen/Monat:** {:.2f}".format(avg_missions_month)),
        f("- **Ø km/Jahr:** {:.2f}".format(avg_km_year)),
        f("- **Ø km/Monat:** {:.2f}".format(avg_km_month)),
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
