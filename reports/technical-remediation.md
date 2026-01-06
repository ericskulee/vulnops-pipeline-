# Technical Remediation Report (v1)

**Date:** 2026-01-05

## How to use this
1. Validate exposure (reachable service, version confirmation, false positive check)
2. Patch or mitigate (vendor fix / config / compensating control)
3. Verify remediation (re-scan or targeted validation)
4. Document exceptions (risk acceptance + expiration)

## Findings (Prioritized)
| Severity | Risk | Host | IP | Port | CVE | Title | SLA Days | Due |
|---|---:|---|---|---:|---|---|---:|---|
| Critical | 10.0 | web-portal-1 | 10.10.10.10 | 443 | CVE-2021-44228 | Log4Shell | 7 | 2026-01-12 |
| Critical | 10.0 | db-payments-1 | 10.10.20.20 | 1433 | CVE-2022-26925 | Windows LSA Spoofing | 7 | 2026-01-12 |
| Critical | 10.0 | dev-api-1 | 10.10.40.40 | 80 | CVE-2019-0708 | BlueKeep | 7 | 2026-01-12 |
| Critical | 9.6 | workstation-22 | 10.10.50.50 | 445 | CVE-2017-0144 | EternalBlue | 7 | 2026-01-12 |
| High | 8.5 | hr-app-1 | 10.10.30.30 | 8080 | CVE-2021-41773 | Apache Path Traversal | 14 | 2026-01-19 |
