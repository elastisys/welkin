# Welkin to Consist of Public Open Source Code and Proprietary Documentation

- Status: Accepted
- Deciders: Management Team
- Date: 2025-01-20

## Context and Problem Statement

Welkin’s current policy, as defined in ADR-0055, is to maintain a mix of public and private open-source components for its product. This approach aimed to balance openness with control over sensitive intellectual property.

However, a critical challenge has emerged. Infrastructure operators, who are key stakeholders, require access to the codebase to understand, troubleshoot, and maintain critical systems. Restricting access to portions of the code limits their ability to operate effectively and creates friction in their workflows.

Additionally, by maintaining a private portion of the open-source code, we introduce unnecessary complexity into our development and operational processes. Ensuring parity between public and private repositories adds overhead and detracts from our goals of transparency and ease of use.

Given these factors, should Welkin move to a model of fully public open-source code while keeping documentation proprietary.

## Decision Drivers

- Elastisys wants to protect Welkin users' open source freedom
- Elastisys wants to offer product support customers good value for their money, and incentivise these to keep paying Elastisys, not only for support but also for access to future Welkin development, security patches, etc.
- Product support customers should have ability to adapt Welkin if needed
- Elastisys was founded on a bedrock on knowledge sharing and openness, and wants that to be reflected in the products and services it develops
- Elastisys needs to protect its intellectual property

## Considered Options

1. Yes, move to a model of fully public open-source code while keeping documentation proprietary.
1. No, keep decision made in ADR0055

## Decision Outcome

Option 1: Move to a model of fully public open-source code while keeping documentation proprietary.

This reflects Welkin's commitment to supporting its users, especially critical infrastructure operators, while continuing to provide value through proprietary offerings.

### Positive Consequences

- Good, because Welkin can stay true to its open source commitment, and thus also preserves user freedoms.
- Good, because critical infrastructure operators will have direct access to the codebase, enabling easier troubleshooting, customization, and maintenance.
- Good, because with a fully open-source codebase, Welkin is better positioned to attract contributors and benefit from external expertise.

### Negative Consequences

- Bad, because the move to a fully public codebase reduces the exclusivity of Welkin's software.
- Bad, because supporting a larger community and addressing external contributions can introduce additional workload for Welkin’s developers.
- Bad, because public code increases the likelihood of forks, which can fragment the user base and dilute the impact of Welkin’s primary offering.
- Bad, because with code available for free, some potential customers may choose to self-host rather than purchase Welkin's proprietary documentation or services.
