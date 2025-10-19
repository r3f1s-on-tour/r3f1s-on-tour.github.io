#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_banner_stats.py (final with year-only 'date' support + overwrite control)
- Überschreibt stats.md standardmäßig (Option --no-overwrite verhindert das).
- Erkennt Datum robust (YAML date/datetime, ISO mit Z, verschiedene Formate, sowie Jahr-only wie 2023).
- Zeitraum: vom ersten erkannten Banner-Jahr bis heute (Jahre = inklusive Zählung).
- Rekursives Scannen von docs/banner (Unterordner inkl.).
- Jahresstatistik mit: Jahr, Banner, Missionen, km gesamt, 500er-Meilensteine.
- Länder- und Städte-Statistik.
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

# ------------------------------ helpers ------------------------------

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
    """Accepts datetime.date/datetime/int/year-string or full date-string. Returns date or None.
       Special: If only a year is provided (e.g., 2023 or "2023"), return Jan 1 of that year.
    """
    if value is None:
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, int):
        try:
            if 1 <= value <= 9999:
                return date(int(value), 1, 1)
        except Exception:
            return None
        return None
    if isinstance(value, float):
        try:
            iv = int(value)
            if float(iv) == value and 1 <= iv <= 9999:
                return date(iv, 1, 1)
        except Exception:
            pass
    if isinstance(value, str):
        v = value.strip()
        if v.isdigit() and len(v) == 4:
            try:
                y = int(v)
                if 1 <= y <= 9999:
                    return date(y, 1, 1)
            except Exception:
                return None
        if v.endswith("Z"):
            v = v[:-1] + "+00:00"
        for fmt in ("%Y-%m-%d","%Y/%m/%d","%d.%m.%Y",
                    "%Y-%m-%dT%H:%M:%S","%Y-%m-%d %H:%M",
                    "%Y-%m-%dT%H:%M:%S%z","%Y-%m-%dT%H:%M:%S.%f%z",
                    "%Y-%m-%dT%H:%M:%S.%f"):
            try:
                return datetime.strptime(v, fmt).date()
            except ValueError:
                continue
        m = re.search(r'(\d{4})-(\d{2})-(\d{2})', v)
        if m:
            try:
                return datetime.strptime(m.group(0), "%Y-%m-%d").date()
            except ValueError:
                pass
    return None

def parse_number(value):
    """Parse int from str or number; returns None if not possible."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        try:
            return int(value)
        except Exception:
            return None
    if isinstance(value, str):
        s = value.strip()
        if s == "":
            return None
        s = s.replace(".", "").replace(" ", "")
        m = re.match(r'^-?\d+', s)
        if m:
            try:
                return int(m.group(0))
            except Exception:
                return None
    return None

def parse_float_km(value):
    """Parse float km from str/number. Accepts '12,3', '12.3 km' etc."""
    if value is None:
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        s = value.strip().lower().replace("km", "").strip()
        s = s.replace(" ", "").replace("\u00a0", "")
        s = s.replace(",", ".")
        try:
            return float(s)
        except Exception:
            return 0.0
    return 0.0

def load_banner_files(banner_dir: Path):
    if not banner_dir.exists():
        raise FileNotFoundError(f"Banner-Ordner nicht gefunden: {banner_dir}")
    for path in sorted(banner_dir.rglob("*.md")):  # REKURSIV
        name = path.name.lower()
        if name in ("index.md","gallery.md","stats.md") or name.startswith("_"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = path.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(text)
        if fm:
            yield path, fm

def extract_city_country(fm: dict):
    city = coalesce(fm.get("city"), fm.get("ort"), fm.get("stadt"), fm.get("region"))
    country = coalesce(fm.get("country"), fm.get("land"), fm.get("nation"))
    if isinstance(city, str): city = city.strip()
    if isinstance(country, str): country = country.strip()
    return city, country

def extract_year_and_date(fm: dict):
    for k in DATE_KEYS:
        raw = fm.get(k)
        dd = parse_date_any(raw)
        if dd:
            return dd.year, dd
        # explicit year-only fallback
        if isinstance(raw, str) and raw.strip().isdigit() and len(raw.strip()) == 4:
            y = int(raw.strip())
            return y, date(y, 1, 1)
        if isinstance(raw, int) and 1 <= raw <= 9999:
            return int(raw), date(int(raw), 1, 1)
    y = fm.get("year") or fm.get("jahr")
    if isinstance(y, int):
        return y, date(int(y), 1, 1)
    if isinstance(y, str) and y.isdigit():
        return int(y), date(int(y), 1, 1)
    return None, None



def banner_distance_km(fm: dict) -> float:
    """
    Extract distance for a banner in KM.
    Interprets the following frontmatter keys as *kilometers* (with decimals allowed):
      - lengthKMeters  (despite the name, treated as KM per user info)
      - distance_km, km, distance, kilometer
    """
    
    # Primary source: lengthKMeters is already in KM
    if "lengthKMeters" in fm and fm.get("lengthKMeters") not in (None, ""):
        return parse_float_km(fm.get("lengthKMeters"))
    # Fallbacks (already km)
    return parse_float_km(coalesce(
        fm.get("distance_km"),
        fm.get("km"),
        fm.get("distance"),
        fm.get("kilometer"),
    ))

    # Fallback to generic distance fields (already in km)
    return parse_float_km(coalesce(
        fm.get("distance_km"),
        fm.get("km"),
        fm.get("distance"),
        fm.get("kilometer"),
    ))

def banner_missions_per_item(fm: dict):
    val = coalesce(fm.get("missions"), fm.get("banner_missions"), fm.get("mission_count"))
    n = parse_number(val)
    return n

def banner_completed_cumulative(fm: dict):
    n = parse_number(fm.get("completed"))
    return n

# ------------------------------ rendering ------------------------------

def make_stats_md(summary, year_rows, country_counts, city_counts):
    lines = []
    lines.append("# Banner-Statistiken")
    lines.append("")
    # Gesamt
    lines.append("## Gesamtstatistik")
    lines.append("")
    lines.append(f"- **Gesamtzahl Banner:** {summary['total_banners']}")
    lines.append(f"- **Zeitraum:** {summary['first_date']} – {summary['last_date']} ({summary['span_days']} Tage)")
    lines.append(f"- **Jahre:** {summary['years_count']}")
    lines.append(f"- **Anzahl Städte:** {summary['unique_cities']}")
    lines.append(f"- **Anzahl Länder:** {summary['unique_countries']}")
    lines.append("")
    # Durchschnitt
    lines.append("## Durchschnittsstatistik")
    lines.append("")
    lines.append(f"- **Ø Banner pro Jahr (über Zeitraum):** {summary['avg_per_year']:.2f}")
    lines.append(f"- **Ø Banner pro Monat (über Zeitraum):** {summary['avg_per_month']:.2f}")
    lines.append("")
    # Jahresstatistik
    lines.append("## Jahresstatistik")
    lines.append("")
    if year_rows:
        lines.append("| Jahr | Banner | Missionen | km gesamt | 500er-Meilensteine |")
        lines.append("|-----:|------:|----------:|----------:|--------------------:|")
        for r in year_rows:
            lines.append(f"| {r['year']} | {r['banners']} | {r['missions']} | {r['km_sum']:.2f} | {r['milestones_500']} |")
    else:
        lines.append("_Keine Jahresdaten gefunden._")
    lines.append("")
    # Länder
    lines.append("## Länder (nach Anzahl Banner)")
    lines.append("")
    if country_counts:
        lines.append("| Land | Banner |")
        lines.append("|:-----|------:|")
        for name, c in country_counts:
            lines.append(f"| {name} | {c} |")
    else:
        lines.append("_Keine Länder gefunden._")
    lines.append("")
    # Städte
    lines.append("## Städte (nach Anzahl Banner)")
    lines.append("")
    if city_counts:
        lines.append("| Stadt | Banner |")
        lines.append("|:------|------:|")
        for name, c in city_counts:
            lines.append(f"| {name} | {c} |")
    else:
        lines.append("_Keine Städte gefunden._")
    lines.append("")
    return "\n".join(lines)

# ------------------------------ main ------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Repo-Wurzel (für relative Pfade)")
    ap.add_argument("--banner-dir", default="docs/banner", help="Ordner mit Banner-Markdown")
    ap.add_argument("--out", default="docs/banner/stats.md", help="Zieldatei für Statistik")
    ap.add_argument("--no-overwrite", action="store_true", help="Vorhandene stats.md NICHT überschreiben")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    banner_dir = (root / args.banner_dir).resolve()
    out_path = (root / args.out).resolve()

    # Overwrite-Check
    if args.no_overwrite and out_path.exists():
        print(f"Stats existiert bereits und --no-overwrite gesetzt: {out_path}")
        return 0

    # Sammle Rohdaten je Banner
    banners = []
    countries_all = []
    cities_all = []

    for path, fm in load_banner_files(banner_dir):
        city, country = extract_city_country(fm)
        y, d = extract_year_and_date(fm)
        km = banner_distance_km(fm)
        per_item_missions = banner_missions_per_item(fm)
        cum_completed = banner_completed_cumulative(fm)
        banners.append({
            "path": path,
            "fm": fm,
            "year": y,
            "date": d,
            "city": city,
            "country": country,
            "km": km,
            "missions_per_item": per_item_missions,
            "completed_cum": cum_completed,
        })
        if city: cities_all.append(city)
        if country: countries_all.append(country)

    # sort chronologisch (nach date, fallback year, dann filename)
    def sort_key(b):
        if b["date"]:
            kdate = b["date"]
        elif b["year"]:
            kdate = date(b["year"], 1, 1)
        else:
            kdate = date(2999, 1, 1)
        return (kdate, b["path"].name.lower())

    banners.sort(key=sort_key)

    # Zeitraum: erstes vorhandenes Jahr bis heute
    today = datetime.now().date()
    years_present = [b["year"] for b in banners if b["year"] is not None]
    if years_present:
        first_year = min(years_present)
        first_date = f"{first_year}-01-01"
        last_date = today.isoformat()
        span_years = (today.year - first_year) + 1
        span_days = (today - date(first_year, 1, 1)).days + 1
    else:
        first_date = last_date = "–"
        span_years = 1
        span_days = 0

    # Jahresgruppen + Missionen & km berechnen
    per_year = defaultdict(list)
    for b in banners:
        if b["year"] is not None:
            per_year[b["year"]].append(b)

    if not per_year:
        print("WARNUNG: Keine Jahresdaten erkannt. Prüfe bitte deine Frontmatter: 'date' kann auch nur die Jahreszahl sein (nun unterstützt).")

    # kumulative completed über die Zeit (für Deltas & 500er-Meilensteine)
    prev_cum = None
    for b in banners:
        if b["missions_per_item"] is None:
            if b["completed_cum"] is not None:
                if prev_cum is None:
                    delta = b["completed_cum"]
                else:
                    delta = max(0, b["completed_cum"] - prev_cum)
                b["missions_per_item"] = delta
            else:
                b["missions_per_item"] = 0
        if b["completed_cum"] is not None:
            prev_cum = b["completed_cum"]

    milestones_per_year = {}
    last_known_cum = 0
    for y in sorted(per_year.keys()):
        max_cum_this_year = last_known_cum
        for b in per_year[y]:
            if b["completed_cum"] is not None:
                max_cum_this_year = max(max_cum_this_year, b["completed_cum"])
        milestones = (max_cum_this_year // 500) - (last_known_cum // 500)
        milestones_per_year[y] = max(0, milestones)
        last_known_cum = max_cum_this_year

    # Jahreszeilen
    year_rows = []
    total_banners = 0
    total_km = 0.0
    total_missions = 0

    for y in sorted(per_year.keys()):
        lst = per_year[y]
        banners_count = len(lst)
        km_sum = sum(b["km"] for b in lst)
        missions_sum = sum(b["missions_per_item"] or 0 for b in lst)
        year_rows.append({
            "year": y,
            "banners": banners_count,
            "km_sum": km_sum,
            "missions": missions_sum,
            "milestones_500": milestones_per_year.get(y, 0),
        })
        total_banners += banners_count
        total_km += km_sum
        total_missions += missions_sum

    # Länder/Städte
    country_counter = Counter([c for c in countries_all if isinstance(c, str) and c.strip() != ""])
    city_counter = Counter([c for c in cities_all if isinstance(c, str) and c.strip() != ""])
    country_counts_sorted = sorted(country_counter.items(), key=lambda x: (-x[1], x[0].lower()))
    city_counts_sorted = sorted(city_counter.items(), key=lambda x: (-x[1], x[0].lower()))

    # Durchschnitt über Zeitraum
    avg_per_year = total_banners / span_years if span_years else float(total_banners)
    avg_per_month = total_banners / (span_years * 12) if span_years else float(total_banners)

    summary = {
        "total_banners": total_banners,
        "first_date": first_date,
        "last_date": last_date,
        "span_days": span_days,
        "years_count": span_years,
        "unique_cities": len(city_counter),
        "unique_countries": len(country_counter),
        "avg_per_year": avg_per_year,
        "avg_per_month": avg_per_month,
    }

    md = make_stats_md(summary, year_rows, country_counts_sorted, city_counts_sorted)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")
    print(f"Statistik geschrieben nach: {out_path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
