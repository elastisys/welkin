---
tags:
  #- ISO 27001:2013 A.12.4.1 Event Logging
  #- ISO 27001:2013 A.12.4.3 Administrator & Operator Logs
  - HIPAA S5 - Security Management Process - Information System Activity Review - § 164.308(a)(1)(ii)(D)
  - HIPAA S18 - Security Awareness, Training, and Tools - Log-in Monitoring - § 164.308(a)(5)(ii)(C)
  - MSBFS 2020:7 4 kap. 17 §
  - HSLF-FS 2016:40 4 kap. 9 § Kontroll av åtkomst till uppgifter
  - NIST SP 800-171 3.3.3
  - NIST SP 800-171 3.3.5
  - NIST SP 800-171 3.3.6
---

# Log Review

This document highlights the risks that can be mitigated by regularly reviewing logs and makes concrete recommendations on how to do log review.

## Relevant Regulations

### GDPR

[GDPR Article 32](https://gdpr.fan/a32):

> Taking into account the state of the art, the costs of implementation and the nature, scope, context and purposes of processing as well as the risk of varying likelihood and severity for the rights and freedoms of natural persons, the controller and the processor shall implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk, including inter alia as appropriate:
> [...]
> a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing.

### Swedish Patient Data Law

!!!note

    This regulation is only available in Swedish. To avoid confusion, we decided not to produce an unofficial translation.

[HSLF-FS 2016:40](https://www.socialstyrelsen.se/kunskapsstod-och-regler/regler-och-riktlinjer/foreskrifter-och-allmanna-rad/konsoliderade-foreskrifter/201640-om-journalforing-och-behandling-av-personuppgifter-i-halso--och-sjukvarden/)

<!-- prettier-ignore-start -->
<!-- vale off -->
> 2 § Vårdgivaren ska genom ledningssystemet säkerställa att
> [...]
> 4. åtgärder kan härledas till en användare (spårbarhet) i informationssystem som är helt eller delvis automatiserade.
<!-- vale on -->
<!-- prettier-ignore-end -->

## Mapping to ISO 27001 Controls

- A.12.4.1 "Event Logging"
- A.12.4.3 "Administrator and Operator Logs"

## Purpose

Welkin captures application logs and audit logs in a tamper-proof logging environment, which we call the Management Cluster. By "tamper-proof", we mean that even a complete compromise of production infrastructure does not allow an attacker to erase or change existing log entries, as would be required to hide their activity and avoid suspicion.

!!!note

    Attackers can, however, inject new "weird" logs entries. However, that wouldn't remove their tracks and would only trigger more suspicion.

However, said logs only help with information security if they are **regularly reviewed** for suspicious activity. Prefer to use logs for catching "unknown unknowns". For known bad failures -- e.g., a Fluentd Pod restarting -- prefer alerts.

## Risks

Periodically reviewing logs can mitigate the following information security risks:

- **Information disclosure**: Regularly reviewing logs can reveal an attack attempt or an ongoing attack.
- **Downtime**: Regularly reviewing logs can reveal misbehaving components (e.g., Pod restarts, various errors) and inform fixes before it leads to downtime.
- **Silent corruption**: Regularly reviewing logs can reveal data corruption.

## How to do log review

By _review period_, we mean the time elapsed since the last review of the logs, e.g., 30 days.

Aim for a review which is both **wide** and **deep**. By wide we mean that you should vary the time interval, time point, filters, etc., when reviewing log entries. By deep we mean that you should actually read and try to understand a sample of logs.

1. Open up a browser and open the Welkin [logs](../user-guide/logs.md) of the Cluster you are reviewing. This functionality is currently offered by OpenSearch.
1. Search for the following keywords on all indices -- i.e., search over each index pattern -- over the last review period: `error`, `failed`, `failure`, `deny`, `denied`, `blocked`, `invalid`, `expired`, `unable`, `unauthorized`, `bad`, `401`, `403`, `500`, `unknown`. Sample a few keywords you recently encountered during your work, e.g., `already installed` or `not found`; be creative and unpredictable.
1. Vary the time point, the time interval, filters, etc.
1. Include the total amount of logs in each log category in your review (set the time interval bigger than retention). Is it the same, significantly less or significantly more logs compared to the last check? If there is a major difference, it could be worth investigating further to figure out why that is.
1. Go _wide_: For each query (index pattern, keyword, timepoint, time interval and filter combination), look at the timeline and see if there is an unexpected increase or decrease in the count of log lines. If you find any, focus your attention on those.
1. Go _deep_: For each query, sample at least 10 log entries, read them and make sure you understand what they mean. Think about the following:
    - What are potential causes?
    - What are potential implications?
    - Time: Do the entries appear periodically or randomly?
    - Space: Does a specific component trigger them? Is the entry generated by the platform or the application?
1. If anything catches your attention vary the time point, time interval and various filters to understand if the log entry is a risk indicator or not. Look for **unknown unknowns**. Any failures, especially authentication failures, which feature a significant increase are risk indicators.
1. Contact the person owning the component, e.g., the Application Developer or Welkin architect, to better understand if the entry is suspicious or not. Perhaps it is due to a recent change -- as indicated by an operator log -- and indicates no risk.

## Log review dashboard

There is a [dashboard](../ciso-guide/audit-logs.md) made to get a overview of the log landscape.

## Possible resolutions

1. If you found a suspicious activity, escalate.
1. If the log entry is due to a bug in Welkin, file an issue.
