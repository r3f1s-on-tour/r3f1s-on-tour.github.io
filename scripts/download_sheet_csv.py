#!/usr/bin/env python3
import os, sys, re, requests

PRIMARY_FMT = "https://docs.google.com/spreadsheets/d/{id}/export?format=csv&gid={gid}"
FALLBACK_FMT = "https://docs.google.com/spreadsheets/d/{id}/gviz/tq?tqx=out:csv&gid={gid}"

UA_HEADERS = {
    # einige Sites geben ohne „echten“ UA 400 zurück
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/123.0 Safari/537.36",
    "Accept": "*/*",
    "Connection": "keep-alive",
}

def getenv_strict(name: str) -> str:
    v = os.getenv(name)
    if not v:
        print(f"[ERROR] Env-Variable {name} fehlt.", file=sys.stderr)
        sys.exit(2)
    return v.strip()

def validate_sheet_id(sheet_id: str):
    if not re.fullmatch(r"[A-Za-z0-9-_]{20,}", sheet_id):
        print("[ERROR] SHEET_ID ist nicht die reine ID (nur der Teil zwischen /d/ und /edit).", file=sys.stderr)
        sys.exit(2)

def validate_gid(gid: str):
    if not re.fullmatch(r"\d+", gid):
        print("[ERROR] SHEET_GID muss numerisch sein (z.B. 0).", file=sys.stderr)
        sys.exit(2)

def fetch_csv(url: str) -> bytes:
    r = requests.get(url, headers=UA_HEADERS, timeout=45, allow_redirects=True)
    if r.status_code == 200 and r.content:
        return r.content
    # kurze Diagnose
    snippet = (r.text or "")[:300].replace("\n", " ")
    print(f"[WARN] {r.status_code} bei {url}\nBody (Auszug): {snippet}", file=sys.stderr)
    return b""

def main():
    sheet_id   = getenv_strict("SHEET_ID")
    gid        = getenv_strict("SHEET_GID")
    output_csv = os.getenv("OUTPUT_CSV", "scripts/banner.csv")

    validate_sheet_id(sheet_id)
    validate_gid(gid)

    primary = PRIMARY_FMT.format(id=sheet_id, gid=gid)
    data = fetch_csv(primary)

    if not data:
        # Fallback: gviz/tq CSV
        fallback = FALLBACK_FMT.format(id=sheet_id, gid=gid)
        print("[INFO] Versuche Fallback-Endpoint (gviz/tq)…", file=sys.stderr)
        data = fetch_csv(fallback)

    if not data:
        print("[ERROR] Konnte CSV nicht herunterladen. Prüfe SHEET_ID/GID und Freigabe (Link-Öffentlich).", file=sys.stderr)
        sys.exit(1)

    os.makedirs(os.path.dirname(output_csv) or ".", exist_ok=True)
    with open(output_csv, "wb") as f:
        f.write(data)
    print(f"Fertig: {output_csv}")

if __name__ == "__main__":
    main()
    
