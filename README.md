![VulnOps Pipeline](https://github.com/ericskulee/vulnops-pipeline/actions/workflows/vulnops.yml/badge.svg)

# VulnOps Pipeline — Scan → Normalize → Prioritize → Track → Report

A practical vulnerability operations workflow that turns raw scan output into **risk-based remediation priorities**, **SLA tracking**, and **executive + technical reports** — with evidence you can show in GitHub.

---

## What this demonstrates

- **Vulnerability intake + normalization** (scan results → structured findings)
- **Risk-based prioritization** (CVSS + asset context + known-exploited signal)
- **Remediation SLAs + due dates** (clear timelines for fixing)
- **Executive + technical reporting** (two audiences, two deliverables)
- **Proof via GitHub Actions** (pipeline can run automatically in CI)

---

## Outputs (what gets generated)

This pipeline generates:

- `outputs/prioritized_findings.csv`
- `reports/executive-summary.md`
- `reports/technical-remediation.md`

If GitHub Actions is enabled, the workflow can also publish downloadable artifacts.

---

## Lab setup (my test environment)

Built and validated inside an isolated VMware Fusion lab:

- **Ubuntu VM** — main workstation (runs the Python pipeline + Git pushes)
- **Kali VM** — scanner (runs Nmap and exports results)
- **Internal / NAT networking** — safe test network between VMs

---

## Architecture diagram

```mermaid
flowchart LR
  K[Kali VM (Scanner)] -->|Nmap scan| X[scan.xml]
  K -->|SCP over SSH| U[Ubuntu VM (Workstation)]
  U -->|Parse XML to CSV| F[scan_findings.csv]
  U -->|Prioritize findings| P[prioritized_findings.csv]
  U -->|Generate reports| R[Reports (Markdown)]
  U -->|Git push (SSH)| G[GitHub Repo]

