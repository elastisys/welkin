---
tags:
  #- ISO 27001 A.14.1.1 Information Security Requirements Analysis & Specification
  #- ISO 27001:2013 A.14.2.4 Restrictions on Changes to Software Packages
  - NIST SP 800-171 3.13.2
  - NIST SP 800-171 3.13.3
  - ISO 27001 Annex A 8.27 Secure System Architecture and Engineering Principles
---
# Architectural Decision Log

## Mapping to ISO 27001 Controls

- A.14.1.1 "Information security requirements analysis and specification"
- A.14.2.4 "Restrictions on Changes to Software Packages"

## What are architectural decisions?

Architectural decisions are high-level technical decisions that affect most stakeholders, in particular Welkin developers, administrators and users.
A non-exhaustive list of architectural decisions is as follows:

- adding or removing tools;
- adding or removing components;
- changing what component talks to what other component;
- major (in the [SemVer](https://semver.org/) sense) component upgrades.

Architectural decisions should be taken as directions to follow for future development and not issues to be fixed immediately.

## What triggers an architectural decision?

An architectural decision generally starts with one of the following:

- A new features was requested by product management.
- An improvement was requested by engineering management.
- A new risk was discovered, usually by the architect, but also by any stakeholder.
- A new technology was discovered, that may help with a new feature, an improvement or to mitigate a risk.

## How are architectural decisions captured?

Architectural decisions are captured via [Architectural Decision Records](#adrs) or the [tech radar](../tech-radar/index.html).
Both are stored in Git, hence a decision log is also captured as part of the Git commit messages.

## How are architectural decisions taken?

Architectural decisions need to mitigate the following information security risks:

- a component might not fulfill advertised expectations;
- a component might be abandoned;
- a component might change direction and deviate from expectations;
- a component might require a lot of (initial or ongoing) training;
- a component might not take security seriously;
- a component might change its license, prohibiting its reuse or making its use expensive.

The Welkin architect is overall responsible for this risk.

## How are these risks mitigated?

Before taking in any new component to Welkin, we investigate and evaluate them. We prefer components that are:

- **community-driven open-source projects**, to reduce the risk of a component becoming abandoned, changing its license or changing direction in the interest of a single entity; as far as possible, we choose [CNCF projects](https://landscape.cncf.io/?project=hosted) (preferably graduated ones) or projects which are governed by at least 3 different entities;
- **projects with a good security track record**, to avoid unexpected security vulnerabilities or delays in fixing security vulnerabilities; as far as possible, we choose projects with a clear security disclosure process and a clear security announcement process;
- **projects that are popular**, both from a usage and contribution perspective; as far as possible, we choose projects featuring well-known users and many Maintainers;
- **projects that rely on technologies that our team is already trained on**, to reduce the risk of requiring a lot of (initial or ongoing) training; as far as possible, we choose projects that overlap with the projects already on our [tech radar](../tech-radar/index.html);
- **projects that are simple to install and manage**, to reduce required training and burden on administrators.

Often, it is not possible to fulfill the above criteria. In that case, we take the following mitigations:

- Architectural Decision Records include recommendations on training to be taken by administrators.
- Closed-source or "as-a-Service" alternatives are used, if they are easy to replace thanks to broad API compatibility or standardization.

These mitigations may be relaxed for components that are part of alpha or beta features, as these features -- and required components -- can be removed at our discretion.

## ADRs

This log lists the architectural decisions for Welkin.

<!-- adrlog -- Regenerate the content by using "adr-log -i". You can install it via "npm install -g adr-log" -->

- [ADR-0000](0000-use-markdown-architectural-decision-records.md) - Use Markdown Architectural Decision Records
- [ADR-0001](0001-use-rook-storage-orchestrator.md) - Use Rook for Storage Orchestrator
- [ADR-0002](0002-use-kubespray-for-cluster-lifecycle.md) - Use Kubespray for Cluster Life-cycle
- [ADR-0003](0003-push-metrics-via-influxdb.md) - [Superseded by [ADR-0019](0019-push-metrics-via-thanos.md)] Push Metrics via InfluxDB
- [ADR-0004](0004-plan-for-usage-without-wrapper-scripts.md) - Plan for Usage without Wrapper Scripts
- [ADR-0005](0005-use-individual-ssh-keys.md) - Use Individual SSH Keys
- [ADR-0006](0006-use-standard-kubeconfig-mechanisms.md) - Use Standard Kubeconfig Mechanisms
- [ADR-0007](0007-make-monitoring-forwarders-storage-independent.md) - Make Monitoring Forwarders Storage Independent
- [ADR-0008](0008-use-hostnetwork-or-loadbalancer-for-ingress.md) - Use HostNetwork or LoadBalancer for Ingress
- [ADR-0009](0009-use-cluster-issuers-for-letsencrypt.md) - Use ClusterIssuers for Let's Encrypt
- [ADR-0010](0010-run-managed-services-in-workload-cluster.md) - Run managed services in Workload Cluster
- [ADR-0011](0011-let-upstream-projects-handle-crds.md) - [Superseded by [ADR-0046](0046-handle-crds.md)] Let upstream projects handle CRDs
- [ADR-0012](0012-do-not-persist-dex.md) - [Superseded by [ADR-0017](0017-persist-dex.md)] Do not persist Dex
- [ADR-0013](0013-configure-alerts-in-omt.md) - Configure Alerts in On-call Management Tool (e.g., Opsgenie)
- [ADR-0014](0014-use-bats-for-testing-bash-wrappers.md) - Use bats for testing bash wrappers
- [ADR-0015](0015-we-believe-in-community-driven-open-source.md) - We believe in community-driven open source
- [ADR-0016](0016-gid-0-is-okey-but-not-by-default.md) - [Superseded by [ADR-0040](0040-allow-group-id-0.md)] gid=0 is okay, but not by default
- [ADR-0017](0017-persist-dex.md) - Persist Dex
- [ADR-0018](0018-use-probe-to-measure-internal-uptime.md) - Use Probe to Measure Uptime of Internal Welkin Services
- [ADR-0019](0019-push-metrics-via-thanos.md) - Push Metrics via Thanos
- [ADR-0020](0020-filter-by-cluster-label-then-data-source.md) - Filter by Cluster label then data source
- [ADR-0021](0021-tls-for-additional-services.md) - Default to TLS for performance-insensitive additional services
- [ADR-0022](0022-use-dedicated-nodes-for-additional-services.md) - Use Dedicated Nodes for Additional Services
- [ADR-0023](0023-allow-snippets-annotations.md) - [Superseded by [ADR-0056](0056-allow-snippets-annotations-after-risk-acceptance.md)] Only allow Ingress Configuration Snippet Annotations after Proper Risk Acceptance
- [ADR-0024](0024-allow-Harbor-robot-account.md) - Allow a Harbor robot account that can create other robot accounts with full privileges
- [ADR-0025](0025-local-storage.md) - Use local-volume-provisioner for Managed Services that requires high-speed disks
- [ADR-0026](0026-hnc.md) - Use `environment-name` as the default root of Hierarchical Namespace Controller (HNC)
- [ADR-0027](0027-postgresql-external-replication.md) - PostgreSQL - Enable external replication
- [ADR-0028](0028-harder-pod-eviction-when-node-goes-OOM.md) - Harder Pod eviction when Nodes are going OOM
- [ADR-0029](0029-expose-jaeger-ui.md) - Expose Jaeger UI in WC
- [ADR-0030](0030-run-argocd-on-elastisys-nodes.md) - Run ArgoCD on the Elastisys Nodes
- [ADR-0031](0031-run-csi-cinder-controllerplugin-on-elastisys-nodes.md) - Run csi-cinder-controllerplugin on the Elastisys Nodes
- [ADR-0032](0032-boot-disk-size.md) - Boot disk size on Nodes
- [ADR-0033](0033-run-cluster-api-controllers-on-service-cluster.md) - Run Cluster API controllers on Management Cluster
- [ADR-0034](0034-how-to-run-multiple-ams-packages-of-the-same-type.md) - How to run multiple AMS packages of the same type in the same environment
- [ADR-0035](0035-run-tekton-on-service-cluster.md) - Run Tekton on Management Cluster
- [ADR-0036](0036-run-ingress-nginx-as-daemonset.md) - Run Ingress-NGINX as a DaemonSet
- [ADR-0037](0037-enforce-ttl-on-jobs.md) - Enforce TTL on Jobs
- [ADR-0038](0038-replace-starboard-operator-with-trivy-operator.md) - Replace the starboard-operator with the trivy-operator
- [ADR-0039](0039-application-dev-permissions.md) - Application developer privilege elevation
- [ADR-0040](0040-allow-group-id-0.md) - Allow running containers with primary and supplementary group id 0
- [ADR-0041](0041-encryption-at-rest.md) - Rely on Infrastructure Provider for encryption-at-rest
- [ADR-0042](0042-argocd-dynamic-hnc-namespaces.md) - ArgoCD with dynamic HNC namespaces
- [ADR-0043](0043-rclone-and-encryption-adhere-cryptography-policy.md) - Rclone and Encryption adheres Cryptography Policy
- [ADR-0044](0044-argocd-managing-its-own-namespace.md) - ArgoCD is not allowed to manage its own namespace
- [ADR-0045](0045-use-specialised-prebuilt-images.md) - Use specialised prebuilt images
- [ADR-0046](0046-handle-crds.md) - Handle all CRDs with the standard Helm CRD management
- [ADR-0047](0047-kubernetes-versions.md) - When to upgrade to new Kubernetes versions
- [ADR-0048](0048-access-management-for-AMS-with-network-policies.md) - Access Management for Additional Managed Services (AMS-es)
- [ADR-0049](0049-run-ingress-nginx-in-chroot.md) - Running NGINX with Chroot Option
- [ADR-0050](0050-use-cluster-isolation.md) - Use Cluster Isolation to separate the application and its traces from its logs and metrics
- [ADR-0051](0051-open-cert-manager-netpols.md) - Open cert-manager Network Policies
- [ADR-0052](0052-azure-encryption-at-rest.md) - Azure Encryption-at-Rest for Object Storage and Block Storage
- [ADR-0053](0053-do-not-expose-platform-observability-services-to-end-users.md) - Do not expose platform observability services to end-users
- [ADR-0054](0054-allow-write-access-to-endpoints-and-endpointslices-after-risk-acceptance.md) - Allow Application Developer write access to Endpoints and EndpointSlices after Proper Risk Acceptance
- [ADR-0055](0055-welkin-to-consist-of-both-public-and-private-open-source.md) - [Superseded by [ADR-0059](0059-welkin-to-consist-public-open-source-code-and-proprietary-documentation.md)]Welkin to consist of both public and private open source
- [ADR-0056](0056-allow-snippets-annotations-after-risk-acceptance.md) - Only allow Ingress Snippet Annotations after Proper Risk Acceptance
- [ADR-0057](0057-why-we-do-not-use-cloud-managed-kubernetes-services.md) - Do Not Use Managed Kubernetes Services
- [ADR-0058](0058-boot-disk-sizes.md) - Boot disk size on Nodes
- [ADR-0059](0059-welkin-to-consist-public-open-source-code-and-proprietary-documentation.md) - Welkin to Consist of Public Open Source Code and Proprietary Documentation

<!-- adrlogstop -->

For new ADRs, please use [template.md](template.md) as basis.
More information on MADR is available at <https://adr.github.io/madr/>.
General information about architectural decision records is available at <https://adr.github.io/>.

## Index Regeneration

Pre-requisites:

- Install [`npm`](https://www.npmjs.com/)
- Install [`adr-log`](https://github.com/adr/adr-log#install)
- Install [`make`](https://packages.ubuntu.com/search?keywords=make)

Run `make -C docs/adr`, then run `pre-commit run --all-files`.
