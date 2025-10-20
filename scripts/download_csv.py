#!/usr/bin/env python3
"""
Lädt ein öffentlich freigegebenes Google Sheet als CSV herunter.
"""

import os
import sys
import requests

def getenv_strict(name: str) -> str:
    v = os.getenv(name)
    if not v:
        print(f"[ERROR] Env-Variable {name} fehlt.", file=sys.stderr)
        sys.exit(2)
    return v

def main():
    sheet_id = getenv_strict("SHEET_ID")
    gid = getenv_strict("SHEET_GID")
    output_csv = os.getenv("OUTPUT_CSV", "banner.csv")

    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()

    os.makedirs(os.path.dirname(output_csv) or ".", exist_ok=True)
    with open(output_csv, "wb") as f:
        f.write(resp.content)

    print(f"Fertig: {output_csv}")

if __name__ == "__main__":
    main()
