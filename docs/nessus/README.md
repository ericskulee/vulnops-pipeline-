# Nessus GUI Lab — Credentialed Vulnerability Scan (Ubuntu TargetJuice)

This lab demonstrates a practical vulnerability assessment workflow using **Nessus (GUI)**: configure a scan, run a **credentialed** assessment, review evidence, and translate results into an actionable remediation plan — with artifacts published to GitHub.

---

## Goals

- Show proficiency with a GUI vulnerability scanner (**Nessus**)  
- Demonstrate **credentialed** scanning to improve detection accuracy  
- Summarize results for both technical and non-technical audiences  
- Document clear remediation actions and how to verify fixes

---

## Lab Environment

- **Platform:** VMware Fusion lab (Apple Silicon host)
- **Scanner:** Nessus (Education / Plus license)
- **Target:** Ubuntu “TargetJuice” VM (authorized lab target)
- **Scan Type:** Credentialed scan (SSH-based)

> All scanning performed only in a controlled lab environment on systems I own or am authorized to test.

---

## Evidence in this repository

- **PDF Report:** `docs/nessus/reports/nessus-ubuntu-targetjuice-credentialed-scan_qizp96.pdf`
- **Screenshots:** `docs/nessus/screenshots/`
- **Summary:** `docs/nessus/NESSUS_SUMMARY.md`

---

## How the workflow works (end-to-end)

1. **Prepare scan scope**
   - Confirm target IP/host is reachable in the lab network
2. **Configure Nessus scan**
   - Select scan template, set targets, enable credentialed checks (SSH)
3. **Run scan**
   - Launch and monitor progress
4. **Review results**
   - Validate evidence (plugin output), confirm affected host/port, identify remediation steps
5. **Document + publish**
   - Generate the PDF report and capture key screenshots
   - Store artifacts in GitHub for portfolio review

---

## Results at a glance

A credentialed scan typically yields:
- More accurate findings (package versions, missing patches, configuration issues)
- Better remediation guidance than unauthenticated-only scans

> See the PDF report for full details and severity breakdown.

---

## Top Findings (portfolio-ready table)

Fill in your top 5–10 from the report (start with Critical/High).  
Use screenshot filenames as evidence links.

| Priority | Severity | Finding (Plugin) | Evidence | Why it matters (plain English) | Recommended fix | Verify fix |
|---:|---|---|---|---|---|---|
| 1 | Critical | _[Finding name]_ | `docs/nessus/screenshots/04-plugin-detail-remediation.png` | Could allow attackers to… | Patch/upgrade… | Re-scan + confirm resolved |
| 2 | High | _[Finding name]_ | `docs/nessus/screenshots/03-vuln-list-sorted.png` | Increases risk of… | Apply update / harden config | Re-scan + validate service |
| 3 | High | _[Finding name]_ | `docs/nessus/screenshots/05-...png` | … | … | … |
| 4 | Medium | _[Finding name]_ | `docs/nessus/screenshots/..png` | … | … | … |
| 5 | Medium | _[Finding name]_ | `docs/nessus/screenshots/..png` | … | … | … |

---

## Remediation plan (what I would do next)

**Phase 1 — Critical/High first**
- Patch missing security updates and vulnerable packages
- Remove/disable unnecessary exposed services
- Apply configuration hardening based on Nessus recommendations

**Phase 2 — Validation**
- Re-run the scan after patching
- Compare severity counts and confirm top findings are resolved

**Phase 3 — Operationalize (VulnOps)**
- Track SLAs for remediation timelines
- Record exceptions with business justification + expiry date
- Generate executive + technical summaries for stakeholders

---

## Optional enhancement: integrate results into my VulnOps pipeline

If CSV exports are available, scan results can be normalized and processed through the pipeline in this repo to generate:
- prioritized findings (`outputs/prioritized_findings.csv`)
- executive summary (`reports/executive-summary.md`)
- technical remediation report (`reports/technical-remediation.md`)

This turns raw scanner output into repeatable reporting and prioritization.

---

## Screenshots checklist (what’s included)

Recommended portfolio screenshots:
- Scan configuration (targets + credentialed settings)
- Scan completion status
- Results summary (severity totals)
- Vulnerability list (sorted)
- 1–2 critical/high details with **plugin output + remediation**
- Report generation screen (PDF created)

See: `docs/nessus/screenshots/`
