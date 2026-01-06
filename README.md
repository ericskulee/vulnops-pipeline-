# VulnOps Pipeline — Scan → Normalize → Prioritize → Track → Report

## What this is
A practical vulnerability operations workflow that turns scan findings into:
- normalized results
- risk-based prioritization
- remediation SLAs
- executive + technical reports

## Project structure
- `sample_data/` — sample assets + scan findings (sanitized/demo)
- `src/` — parsing, scoring, SLA assignment, report generation
- `outputs/` — prioritized CSV outputs
- `reports/` — executive and technical markdown reports
- `docs/` — triage workflow, false-positive handling, verification notes

## Run it locally (optional)
```bash
python src/generate_reports.py \
  --findings sample_data/scans/scan_findings.csv \
  --assets sample_data/assets.csv \
  --outdir outputs \
  --reportdir reports
