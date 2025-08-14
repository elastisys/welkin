# BSI IT-Grundschutz Controls

The **BSI IT-Grundschutz** framework, developed by Germany’s Federal Office for Information Security (BSI), provides a structured, modular approach to implementing information security management.
<!-- vale off -->
Its "building blocks" (_Bausteine_) address specific components, processes, and technologies, offering concrete safeguards that can be tailored to different protection needs.
<!-- vale on -->
These modules are grouped into thematic layers—such as Applications (APP), Systems (SYS), and Networks (NET)—and link security objectives with implementation guidance and verification steps, forming a cohesive, auditable framework.

Within the Applications layer, **APP.4.4 – Kubernetes** focuses on securing container orchestration environments.
Introduced in the 2022 edition of the IT-Grundschutz Compendium, this module addresses risks specific to Kubernetes Clusters, from configuration management and access control to backup and recovery.
APP.4.4 complements SYS.1.6 (Containerisation) by translating general container security principles into Kubernetes-specific measures, ensuring that both operational practices and technical configurations meet robust, verifiable security standards.

> [!IMPORTANT]
> Many requirements in APP.4.4 **cannot be fulfilled by an application platform alone**, because they depend on factors outside the product's scope—such as how Welkin is deployed, integrated, and operated in a specific environment, as well as how the application on top is developed and deployed.
> While a platform can provide features and guardrails (e.g., RBAC, audit logs) to support these controls, full compliance depends on correct configuration, secure surrounding infrastructure, and disciplined operational processes.
>
> That is why this documentation does not present an "all green checkboxes" compliance table for APP.4.4.
> Instead, it maps each relevant requirement to the parts of the product documentation that explain how Welkin can support or enable it.
> This approach allows platform administrators to combine Welkin's capabilities with their own environment-specific configurations, policies, and processes, ensuring a realistic and verifiable assessment rather than a misleading implication of complete, out-of-the-box compliance.

Click on the links below to navigate the documentation by control.

[TAGS]

## Other IT-Grundschutz Controls

<!-- vale off -->
### APP.4.4.A17 Attestierung von Nodes (H)
<!-- vale on -->

The Kubespray layer in Welkin ensures that Data Plane Nodes and Control Plane Nodes are mutually authenticated via mutual TLS.

## BSI IT-Grundschutz Controls outside the scope of Welkin

Pending official translation into English, the controls are written in German.

<!-- vale off -->
### APP.4.4.A6 Initialisierung von Pods (S)
<!-- vale on -->

Application Developers must make sure that initialization happens in [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/).

<!-- vale off -->
### APP.4.4.A11 Überwachung der Container (S)
<!-- vale on -->

Application Developers must ensure that their application has a liveliness and readiness probe, which are configured in the Deployment. This is illustrated by our [user demo](https://github.com/elastisys/welkin/blob/main/user-demo/deploy/welkin-user-demo/templates/deployment.yaml).

<!-- vale off -->
### APP.4.4.A12 Absicherung der Infrastruktur-Anwendungen (S)
<!-- vale on -->

This requirement essentially states that the Welkin environments are only as secure as the infrastructure around them. Make sure you have a proper IT policy in place. Regularly review the systems where you store backups and configuration of Welkin.

<!-- vale off -->
### APP.4.4.A20 Verschlüsselte Datenhaltung bei Pods (H)
<!-- vale on -->

Welkin recommends disk encryption to be provided at the infrastructure level. If you have this requirement, check for full-disk encryption via the [provider audit](../../operator-manual/provider-audit.md).
