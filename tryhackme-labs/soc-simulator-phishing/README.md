# 🛡️ TryHackMe SOC Simulator: Introduction to Phishing

## 📌 Executive Summary
Completed a hands-on SOC simulation focusing on L1 alert triage, email header analysis, and phishing incident response. The scenario required analyzing spoofed domains, inspecting shortened URLs (Bitly), verifying firewall block rules, and documenting incident findings.

---

## 📊 Key Performance Metrics

| Metric | Result | Target Status |
| :--- | :--- | :--- |
| **True Positive Identification Rate** | **100%** | ✅ Passed |
| **False Positive Identification Rate** | **100%** | ✅ Passed |
| **Mean Time to Resolve (MTTR)** | **4 Minutes** | ⚡ Fast |
| **Mean Dwell Time** | **7 Minutes** | ⚡ Fast |
| **Overall Result** | **Breach Prevented** | 🏆 Victory |

![Victory Screen](assets/victory.png)
![Metrics](assets/metrics.png)

---

## 🔍 Investigation Highlights & Technical Findings

* **Phishing Detection:** Identified spoofed Microsoft impersonation emails carrying malicious links shortened via Bitly.
* **Network & Firewall Validation:** Verified source/destination IP indicators and confirmed existing firewall drop rules were successfully active.
* **Triage Speed:** Successfully processed and closed 4 alerts with zero breach impact.

---

## 💡 Post-Incident Analysis & Lessons Learned

While all threats were successfully mitigated, the scenario's AI analysis highlighted key areas to improve L1 incident report quality:

1. **Complete 5 Ws Coverage:** Future tickets must explicitly include internal host IP scoping (`10.20.2.17`) alongside recipient/sender details.
2. **Behavioral Proof:** Ensure the report explicitly states whether credential entry, execution, or host compromise occurred rather than leaving impact implicit.
3. **Log Timestamp Verification:** Cross-check event times directly against SIEM/log sources rather than relying solely on email header timestamps.
4. **Actionable Remediation:** Detail decisive containment actions (endpoint isolation, IP domain blocks, user credential resets) rather than general summary statements.
