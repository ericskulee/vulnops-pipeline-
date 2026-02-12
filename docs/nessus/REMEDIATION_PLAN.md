# Remediation Plan — Nessus Credentialed Scan (Ubuntu TargetJuice)

## Goal
Reduce Critical/High findings first, validate fixes, and document measurable improvement.

## Priority order
1) **Critical** → fix within 7 days (lab SLA)
2) **High** → fix within 14 days
3) **Medium** → fix within 30 days
4) **Low** → fix within 60 days

## Top actions (based on report)
### 1) Patch critical libraries / packages
- **FFmpeg vulnerabilities (USN-6803-1)**  
  - Action: Update affected packages to fixed versions (may require Ubuntu Pro/ESM `+esm` packages)
- **GStreamer bad plugins vulnerabilities (USN-7558-1)**  
  - Action: Update affected packages per Ubuntu advisory

### 2) Patch high findings (examples)
- **cJSON (USN-6784-1)** → update packages
- **7-Zip (USN-7438-1)** → update packages
- **zvbi (USN-7367-1)** → update packages

### 3) Reduce exposure (low finding)
- **ICMP Timestamp Disclosure**
  - Action: Filter ICMP timestamp request (type 13) and reply (type 14)

## Verification (how I prove it’s fixed)
1) Apply patches / configuration change
2) Re-run Nessus scan against the same target
3) Capture evidence:
   - new PDF report saved as `docs/nessus/reports/nessus-post-remediation.pdf`
   - screenshot showing reduced Critical/High counts
4) Document the delta in `docs/nessus/README.md`:
   - Before vs After severity totals
