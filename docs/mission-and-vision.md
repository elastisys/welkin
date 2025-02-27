# Mission and Vision

## Purpose

The Welkin Mission and Vision statements support [Elastisys' Mission and Vision](https://elastisys.com/about/).
They provide a "northern star" to orient development.

## Statements

- **Mission**: The best application developer and administrator experience in and of a cloud-native platform that cost-effectively ensures security and regulatory compliance.

- **Vision**: Securing Europe’s digital future for services critical to society.

## What does the vision and mission mean?

Below we explain what we mean with each word in the mission and vision.

### Best application developer experience

- **Closes the DevOps loop**:
    - It should be easy for application developer to deploy their code.
    - It should be easy for application developers to observe their code via the three pillars of observability: logs, metrics and traces.
- **As self-service as possible**:
    - Application developers should be able to reach their goals with as little platform administrator involvement as possible.
    - This should not be interpreted as “click to deploy”, rather "as a platform administrator, I can point application developers to documentation to quickly achieve their goals".
    - "Click to deploy" **can** be part of the solution, but it doesn't **have to** be.
- **Good documentation**:
    - Documentation should help application developers throughout their journey of getting started and making the best use of the platform.
    - Documentation should be searchable, for example, application developers should be able to copy-paste an error message to quickly recover from it.
- **Makes security and compliance easy**:
    - The platform should make it hard for application developers to do the wrong thing by employing guardrails and secure defaults.

### Best administrator experience

- **Good documentation**:
    - It should be easy for the platform administrator to get an overview of the platform, its components and the interaction between its components.
    - The platform administrator should be provided with:
        - checklists, for rare and hard-to-automate tasks;
        - runbooks;
        - scripts.
- **Good scalability**:
    - A team of platform administrators should be able to administer many environments.
    - Cognitive load on platform administrators should be limited, for example, by:
        - limiting the scope (tech stack) of the platform;
        - limiting divergence between environments.
- **Minimise number of tickets from application developers**:
    - Ideally, the platform administrator should be able to point application developers to documentation which enables the latter to reach their goals by themselves.
- **Minimise amount of manual actions, "thinking" and troubleshooting**
    - The platform should perform frequent actions by itself, such as related to patching, updates and capacity management.
    - The platform should obey configuration-by-code. Note that, 100% GitOps -- i.e., performing all operations via `git commit` -- is a non-goal.
- **Minimise likelihood and impact of incidents**:
    - The platform should alert when an environment needs human attention.
- **Minimise number of alerts, especially off-hours ones**:
    - All alerts should be actionable.
    - The platform should reduce the priority of alerts via resilience and automation.
- **Minimize time spent on billing**:
    - It should be easy to understand how to bill for the services provided by the platform.
- **Minimize time spent on verifying environment specification**:
    - It should be easy for platform administrators to retrieve and verify the configuration of a large number of environments to ensure that important details, such as backup retention, log retention, are configured as expected by application developers.

### Security

Welkin should be built and should make it easy for the application to be built with the following security principles in mind.

- **Security-By-Design**:
    - The entire system and its individual components are designed from the ground up with security in mind.
    - Deliberate attacks and unauthorized actions are explicitly considered, and the impact of security incidents is minimized through system design.
- **Security-By-Default**:
    - Security is enabled by default, requiring no additional configuration to ensure a secure state.
    - Security features _may_ be disabled only if:
        - their benefits strongly outweighs the limitations they impose;
        - there are sufficient compensatory measures;
        - the residual risk is clearly understood and documented.
- **Minimal-Need-To-Know Principle**:
    - Each component and user is granted only the permissions necessary to perform a specific action.
- **Defence-In-Depth Principle**:
    - Security risks are not addressed by individual protective measures alone but are mitigated through the implementation of layered, multi-level, and complementary security measures.
- **Redundancy Principle**:
    - The overall system is designed in such a way that the failure of individual components does not compromise security-relevant functions.
    - The system design reduces both the likelihood and impact of issues arising from unrestricted resource consumption, such as memory or network bandwidth, which could lead to resource exhaustion or denial-of-service (DoS) attacks.
- **Free From Known Vulnerabilities**:
    - The system is built using components that are free from known security vulnerabilities.
    - The platform makes it easy to detect vulnerabilities and apply security patches, both at the level of the application and the platform itself.

The platform should support an organization's information security certification efforts, e.g., with ISO 27001:2022.

### Regulatory compliance

The platform should help an organization comply with various regulatory requirements, such as:

- EU GDPR
- EU NIS2
- EU Critical Entities Resilience Directive (CER)
- EU Medical Device Regulation (MDR)
- Swedish Patientdatalagen (PDL)

### Cost effectively

- The platform should leave headroom, as required for stability and security, but not waste resources.
- Application developers should be able to understand what they get for every CPU, GB and Gbps.
- The platform should help close the FinOps loop.

## Supporting Pillars

In order to support the mission and vision, Welkin needs the following supporting pillars.

### Quality Assurance

It should be easy to release a new version of Welkin which meets the target quality standards.

### Contributor Experience

It should be easy to contribute improvements and new features to Welkin.
