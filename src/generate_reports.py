import argparse
import csv
from datetime import date, timedelta
from pathlib import Path

from parse_scan import load_findings
from risk_score import load_known_exploited, calculate_risk_score
from sla_assign import assign_sla_days, severity_label


def load_assets(assets_csv_path: str) -> dict[str, dict]:
    assets = {}
    with open(assets_csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            key = (row.get("hostname") or "").strip()
            if key:
                assets[key] = row
    return assets


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--findings", required=True)
    ap.add_argument("--assets", required=True)
    ap.add_argument("--known-exploited", default="sample_data/known_exploited_cves.txt")
    ap.add_argument("--outdir", default="outputs")
    ap.add_argument("--reportdir", default="reports")
    args = ap.parse_args()

    findings = load_findings(args.findings)
    assets = load_assets(args.assets)
    known_exploited = load_known_exploited(args.known_exploited)

    enriched = []
    today = date.today()

    for f in findings:
        hostname = (f.get("hostname") or "").strip()
        asset = assets.get(hostname)

        risk = calculate_risk_score(f, asset, known_exploited)
        sla_days = assign_sla_days(risk)
        due_date = today + timedelta(days=sla_days)

        enriched.append(
            {
                "severity": severity_label(risk),
                "risk_score": risk,
                "sla_days": sla_days,
                "due_date": due_date.isoformat(),
                "hostname": hostname,
                "ip": f.get("ip"),
                "port": f.get("port"),
                "protocol": f.get("protocol"),
