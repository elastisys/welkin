---
search:
  boost: 2
tags:
  #- ISO 27001:2013 A.12.1.4 Separation of Development, Testing & Operational Environments
  - HIPAA S12 - Information Access Management - Isolating Healthcare Clearinghouse Functions - § 164.308(a)(4)(ii)(A)
  - MSBFS 2020:7 3 kap. 1 §
  - MSBFS 2020:7 3 kap. 2 §
  - HSLF-FS 2016:40 3 kap. 10 § Upphandling och utveckling
  - BSI IT-Grundschutz APP.4.4.A1
  - BSI IT-Grundschutz APP.4.4.A15
  - MDR Annex VI UDI-related
  - NIST SP 800-171 3.4.4
  - ISO 27001 Annex A 8.31 Separation of Development, Test and Production Environments
---

<!-- markdownlint-disable-file first-line-h1 -->

!!! elastisys "For Elastisys Managed Services Customers"

    You can order a new Environment by filing a [service ticket](https://elastisys.atlassian.net/servicedesk/).

    If you have multiple Environments, and one or more have been clearly designated to be non-production Environments, Elastisys will apply major and minor updates to your non-production Environment(s) at least five working days before applying said update to your production Environment(s).

    For more information, please read [ToS 3.5 Updates and Upgrades](https://elastisys.com/legal/terms-of-service/#35-updates-and-upgrades).

Welkin recommends setting up at least two separate environments: one for non-production use (e.g. development and testing) and one for production use.

---

# How Many Environments?

## Definitions

For the purpose of this document we use the following distinction:

- **Application Deployment** - One instance of a customer's application. Commonly, multiple application deployments are used in the software development life cycles, such as: local, development, integration, testing, staging, and production.
- **Environment** - One instance of a Welkin Deployment. One Environment is composed of two Kubernetes Clusters, the Management Cluster and Workload Cluster.

## Levels of Isolation

Various levels of isolation between Application Deployments can be achieved while using Kubernetes:

- **Labels**: in which Application Deployments reside in the same Namespace and are separated "only" by e.g. Helm Releases or Argo CD Application labels. Network Policies can apply here, but e.g. Secrets will be accessible throughout the entire Namespace.
- **Namespace isolation**: in which Application Deployments share a Workload Cluster, but are separated logically using Namespaces. Network Policies work here, too, and Namespaces are a Kubernetes trust boundary when it comes to access to Secrets. Namespaces can also be used for resource quotas, for soft capacity allocation limitations.
- **Node isolation**: in which Application Deployments share an environment, but are deployed on different Nodes. On this level, both performance and security isolation is greater than in the previous, since the underlying virtual machines are separate. This is what Welkin does with additional services, such as PostgreSQL and RabbitMQ. Node isolation can be done both with and without Namespace isolation.
- **Cluster isolation**: in which Application Deployments share an Environment, but are deployed on separate Workload Clusters. This helps improve isolation in terms of access control, but does no such thing in the services that Welkin provides for logging, metrics, and image registry as they all are deployed in a shared Management Cluster.
- **Separate Environments**: in which Application Deployments share nothing. This level of isolation is the highest, which implies total isolation for access control, credentials, network traffic, performance, and there are no shared platform components.

## Relevant Regulations

Many regulations require strict separation between testing and production Application Deployments.
In particular, production data should not be compromised, no matter what happens in testing Application Deployments.

Similarly, some regulations -- such as Medical Devices Regulation (MDR) -- require you to take a risk-based approach to changing the tech stack.
Depending on your risk assessment, this implies **verifying** changes in a non-production Application Deployment before going into production.

Some regulations, such as [NIS2](../ciso-guide/controls/nis2.md), require that the organization takes measures related to "security in network and information systems acquisition, development and maintenance, including vulnerability handling and disclosure".
This is commonly implemented using a concept called Security Zones.
If two applications are in different Security Zones, then Cluster isolation might be required.

## Recommendations

Taking into account the relevant regulations, Welkin recommends setting up **at least two Environments**:

- non-production Environment hosting Application Deployments from development up to staging;
- production Environment hosting the production Application Deployment.

However, the exact number of Application Deployments and Environments will depend on your needs.
Please use the two figures below to reason about environments, trading developer productivity and data security:

![Ideal Developer Experience](img/environments/ideal-dx.svg)

![Ideal Promotion](img/environments/ideal-promotion.svg)

## Multi-tenancy in Welkin

Welkin does not support multi-tenancy in a way where multiple Application Teams share an environment but do not have access to each others data. Even with Cluster isolation with multiple Workload Clusters there is a shared Management Cluster within a Welkin Environment where common platform services run.

Some services such as [OpenSearch](https://opensearch.org/docs/latest/security/multi-tenancy/tenant-index/) and [Grafana](https://grafana.com/docs/loki/latest/operations/multi-tenancy/) with [Thanos](https://thanos.io/tip/operating/multi-tenancy.md/#multi-tenancy) technically support multi-tenancy even if it is not implemented in Welkin as of yet. Harbor however, with its [system administrator role](https://goharbor.io/docs/2.12.0/administration/managing-users/#assigning-the-harbor-system-administrator-role), has no concept of multi-tenancy and can not be implemented without decreasing the permissions of an Application Developer in Welkin.

This means that if multi-tenancy was implemented wherever possible, it would leave the responsibility of the trust boundary in the hands of third party services. We would have to trust that they maintain this separation as their software evolves. We have already decided in [ADR-0050](../adr/0050-use-cluster-isolation.md) that Cluster isolation between the Workload and Management Cluster is necessary to achieve regulatory compliance, and in this page that multiple environments are recommended for further security between production and non-production data.

We therefore deem that implementing software-level multi-tenancy to not be sufficient in securing necessary levels of isolation between tenants and that separate environments are needed if data isolation is required.
