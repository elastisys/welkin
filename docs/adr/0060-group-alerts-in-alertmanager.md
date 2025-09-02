# Group alerts in Alertmanager

- Status: Accepted
- Deciders: Product Team
- Supersedes: 0013-configure-alerts-in-omt
- Date: 2025-04-29

## Context and Problem Statement

As a Welkin administrator, I experience frustration when receiving multiple alerts from the same component for the same underlying problem.
This is particularly noticeable when identical alerts are fired for each Pod, such as when a Fluentd issue triggers multiple alerts from every Fluentd Pod.

[ADR-0013](0013-configure-alerts-in-omt.md) previously decided to configure alerting within the on-call management tool (OMT).
However, given that our current OMT (OpsGenie) lacks robust support for alert grouping, and considering a probable future transition away from OpsGenie, we aim to leverage Alertmanager's native grouping capabilities to mitigate this issue.

Should we begin utilizing the grouping feature in Alertmanager?

## Decision Drivers

- We want to find a solution which is scalable and minimizes the platform administrator burden.
- We want to make the operator life easier.
- Minimize the volume of multiple identical alerts originating from the same component for the same problem.

## Considered Options

1. Option 1: Yes, use grouping in Alertmanager. Leverage Alertmanager's built-in functionality to aggregate related alerts before sending them to the OMT.
1. Option 2: No, look at other on-call management tools that provide this feature. Seek out and potentially migrate to a different OMT that offers more sophisticated native alert grouping capabilities.
1. Option 3: No, look at implementing this in OpsGenie. Investigate and potentially develop custom solutions or integrations within OpsGenie to achieve alert grouping.

## Decision Outcome

Chosen Option 1: Yes, use grouping in Alertmanager.
    - Generic prioritization, grouping, inhibition, and silencing of alerts will primarily be handled within Alertmanager.
    - Environment-specific silencing (e.g., for infrastructure provider maintenance windows) and differentiation between 24/7 and 6-22 customer support will continue to be managed in the On-Call Management Tool (OMT).
    - Alertmanager's default settings for `group_wait` and `group_interval` are considered sufficient for the current needs, but are subject to tuning based on operational feedback.

### Positive Consequences

- Reduced Alert Fatigue: It would significantly make the administrator's life easier by reducing the sheer volume of redundant alerts to handle, leading to a more scalable alert management process.
- Tool Agnostic: It would help Welkin OS users (administrators) since the grouping logic is not dependent on a specific on-call management tool or its intricate configuration, ensuring consistency regardless of the OMT in use.

### Negative Consequences

- Potential Grouping Limitations: There may be some limitations to configuration with Alertmanager grouping that could be solved by a more advanced on-call management tool. For example, Alertmanager might not inherently be able to group alerts from entirely different components that are firing for the same root cause without complex rule definitions. Further investigation into these specifics is needed

## Recommendation to Platform Administrators

- Configuration: Refer to the Alertmanager configuration documentation for detailed options.
- Implementation Details and Tuning: The initial implementation of grouping will likely result in a mix of "over-grouping" (too many disparate alerts grouped together) and "under-grouping" (related alerts not being grouped). This will require continuous tuning based on operational experience to achieve the ideal state where alerts having the same underlying cause are grouped effectively.
- While Alertmanager's inhibition feature is powerful for suppressing notifications, it carries a risk of missing critical alerts if not configured carefully. This feature will be revisited and considered for implementation at a later stage.
