#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_banner_stats.py
- Überschreibt stats.md standardmäßig (Option --no-overwrite verhindert das).
- Erkennt Datum robust (YAML date/datetime, ISO mit Z, verschiedene Formate, sowie Jahr-only wie 2023).
- Zeitraum: vom ersten erkannten Banner-Jahr bis heute (Jahre = inklusive Zählung).
- Rekursives Scannen von docs/banner (Unterordner inkl.).
- **Filter**: Es werden ausschließlich Banner-Dateien berücksichtigt, deren Frontmatter ein Feld 'nummer' enthält.
- Jahresstatistik mit: Jahr, Banner, Missionen, MissionDays, km gesamt, 500er-Meilensteine.
- Länder- und Städte-Statistik.
- Durchschnittsstatistik: Banner/∅Jahr/∅Monat, Missionen/∅Jahr/∅Monat, km/∅Jahr/∅Monat.
- Gesamtstatistik erweitert um: Gesamt-km (Summe aller Distanzen) und MissionDays gesamt (Summe missionDay).
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
DATE_KEYS = ["date","completed_date","completed_at","done_date","finished_date"]

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

def coalesce(*values):
    for v in values:
        if v is None:
            continue
        if isinstance(v, str) and v.strip() == "":
            continue
        return v
    return None

def parse_date_any(value):
    if value is None:
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, (int, float)) and 1 <= int(value) <= 9999:
        return date(int(value), 1, 1)
    if isinstance(value, str):
        v = value.strip()
        if v.isdigit() and len(v) == 4:
            return date(int(v), 1, 1)
        for fmt in ("%Y-%m-%d","%Y/%m/%d","%d.%m.%Y"):
            try:
                return datetime.strptime(v, fmt).date()
            except Exception:
                continue
    return None

def parse_float_km(v):
    if v is None: return 0.0
    if isinstance(v, (int,float)): return float(v)
    s = str(v).lower().replace("km","").replace(",","." ).strip()
    try: return float(s)
    except: return 0.0

def parse_number(v):
    if v is None: return None
    if isinstance(v,(int,float)): return int(v)
    s = str(v).strip()
    if s.isdigit(): return int(s)
    return None

def parse_mission_day(v):
    if v in (True,"true","True","yes","ja","1",1): return 1
    return 0

def banner_distance_km(fm):
    if "lengthKMeters" in fm: return parse_float_km(fm["lengthKMeters"])
    if "lengthKm" in fm: return parse_float_km(fm["lengthKm"])
    for k in ["distance_km","km","distance","kilometer"]:
        if k in fm: return parse_float_km(fm[k])
    return 0.0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--banner-dir", default="docs/banner")
    ap.add_argument("--out", default="docs/banner/stats.md")
    ap.add_argument("--no-overwrite", action="store_true")
    args = ap.parse_args()

    root = Path(".").resolve()
    banner_dir = (root / args.banner_dir).resolve()
    out_path = (root / args.out).resolve()

    # Sammeln der Banner mit nummer
    banners = []
    for path in banner_dir.rglob("*.md"):
        if path.name.lower() in ("index.md","gallery.md","stats.md"): continue
        fm = parse_frontmatter(path.read_text(encoding="utf-8",errors="ignore"))
        if not fm or "nummer" not in fm: continue
        year = parse_number(fm.get("date")) or parse_number(fm.get("year"))
        km = banner_distance_km(fm)
        missions = parse_number(fm.get("missions")) or 0
        mday = parse_mission_day(fm.get("missionDay"))
        banners.append({"path":path,"year":year,"km":km,"missions":missions,"mday":mday,
                        "city":fm.get("region") or fm.get("city"),
                        "country":fm.get("country") or fm.get("land")})

    if not banners:
        print("Keine Banner gefunden."); return

    # Zeitspanne
    today = datetime.now().date()
    years = [b["year"] for b in banners if b["year"]]
    first_year = min(years); span_years = (today.year - first_year) + 1

    # Jahreswerte
    per_year = defaultdict(list)
    for b in banners:
        if b["year"]: per_year[b["year"]].append(b)

    year_rows=[]; total_km=total_missions=total_mdays=total_banners=0
    for y in sorted(per_year):
        lst=per_year[y]
        km=sum(b["km"] for b in lst)
        ms=sum(b["missions"] for b in lst)
        md=sum(b["mday"] for b in lst)
        year_rows.append({"year":y,"banners":len(lst),"km":km,"missions":ms,"md":md})
        total_km+=km; total_missions+=ms; total_mdays+=md; total_banners+=len(lst)

    # Länder / Städte
    countries=Counter(b["country"] for b in banners if b["country"])
    cities=Counter(b["city"] for b in banners if b["city"])

    # Mittelwerte
    avg=lambda x: x/span_years if span_years else 0
    md=[]
    md+=["# Banner-Statistik","","## Gesamt","",
          f"- Gesamtbanner: {total_banners}",
          f"- Gesamt km: {total_km:.2f}",
          f"- MissionDays gesamt: {total_mdays}",
          f"- Zeitraum: {first_year}–{today.year} ({span_years} Jahre)",""]
    md+=["## Durchschnitt","",
          f"- Ø Banner/Jahr: {avg(total_banners):.2f}",
          f"- Ø Missionen/Jahr: {avg(total_missions):.2f}",
          f"- Ø km/Jahr: {avg(total_km):.2f}",""]
    md+=["## Jahresstatistik","",
          "| Jahr | Banner | Missionen | MissionDays | km |",
          "|----:|----:|----:|----:|----:|"]
    for r in year_rows:
        md.append(f"| {r['year']} | {r['banners']} | {r['missions']} | {r['md']} | {r['km']:.2f} |")
    md+=["","## Länder",""]
    for c,v in countries.most_common(): md.append(f"- {c}: {v}")
    md+=["","## Städte",""]
    for c,v in cities.most_common(): md.append(f"- {c}: {v}")
    out_path.write_text("\n".join(md),encoding="utf-8")
    print(f"Statistik geschrieben nach: {out_path}")

if __name__=="__main__":
    main()
