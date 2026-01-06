import csv
from pathlib import Path

def load_findings(findings_csv_path: str) -> list[dict]:
    path = Path(findings_csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Findings file not found: {findings_csv_path}")

    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
