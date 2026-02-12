                   nano docs/nessus/NESSUS_SUMMARY.md
# Nessus Credentialed Scan — Ubuntu TargetJuice

## Evidence
- Report (PDF): `docs/nessus/reports/nessus-ubuntu-targetjuice-credentialed-scan_qizp96.pdf`
- Screenshots: `docs/nessus/screenshots/`

## Scan details
- Scan name: **Nessus - Ubuntu TargetJuice - Credentialed**
- Target: **172.16.135.130**
- Start: **Sun Jan 25 00:05:56 2026**
- End: **Sun Jan 25 00:18:15 2026**
- Report generated: **Sun, 25 Jan 2026 00:18:15 EST**

## Results summary (by severity)
- Critical: **2**
- High: **10**
- Medium: **2**
- Low: **1**
- Info: **84**

## Notes
- Exporting “findings” may be restricted in some Nessus editions, but **PDF reports are valid lab evidence** for GitHub/portfolio use.
- If exports become available later (CSV/Nessus), we can add them under `docs/nessus/exports/`.
# Nessus Credentialed Scan — Ubuntu TargetJuice

## Evidence
- **Report (PDF):** `docs/nessus/reports/nessus-ubuntu-targetjuice-credentialed-scan_qizp96.pdf`
- **Screenshots:** `docs/nessus/screenshots/`

## Scan details
- **Scan name:** Nessus - Ubuntu TargetJuice - Credentialed  
- **Target:** `172.16.135.130`  
- **Start:** Sun Jan 25 00:05:56 2026  
- **End:** Sun Jan 25 00:18:15 2026  
- **Report generated:** Sun, 25 Jan 2026 00:18:15 EST  

## Results summary (by severity)
- **Critical:** 2  
- **High:** 10  
- **Medium:** 2  
- **Low:** 1  
- **Info:** 84  

## Key findings (from report)
### Critical (2)
1) **FFmpeg vulnerabilities (USN-6803-1)** — Critical  
   - Impact: DoS / potential arbitrary code execution  
   - Note: Fix may require Ubuntu Pro/ESM packages (`+esm` versions)

2) **GStreamer bad plugins vulnerabilities (USN-7558-1)** — Critical  
   - Action: Update affected packages per Ubuntu advisory

### High (examples)
- **cJSON vulnerabilities (USN-6784-1)** — High (update packages)
- **7-Zip vulnerabilities (USN-7438-1)** — High (update packages)
- **zvbi vulnerabilities (USN-7367-1)** — High (update packages)

### Low (example)
- **ICMP Timestamp Request Remote Date Disclosure**  
  - Action: Filter inbound ICMP timestamp requests (type 13) and outbound replies (type 14)

## Notes
- Exporting raw “findings” (CSV/.nessus) can be restricted depending on the Nessus edition/license.
- For portfolio/lab purposes, **a PDF report + supporting screenshots** are valid evidence and are commonly used.
- If exports become available later, store them here: `docs/nessus/exports/`
