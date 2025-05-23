# Release Notes

## Welkin RabbitMQ

<!-- BEGIN TOC -->

- [v4.0.6-ck8s3](#v406-ck8s3) - 2025-05-20
- [v4.0.6-ck8s2](#v406-ck8s2) - 2025-04-25
- [v4.0.6-ck8s1](#v406-ck8s1) - 2025-02-28
- [v3.13.7-ck8s1](#v3137-ck8s1) - 2024-12-09
- [v3.12.6-ck8s1](#v3126-ck8s1) - 2024-01-17
- [v3.11.18-ck8s1](#v31118-ck8s1) - 2023-07-03
- [v3.10.7-ck8s1](#v3107-ck8s1) - 2022-09-21
- [v1.11.1-ck8s2](#v1111-ck8s2) - 2022-06-08
- [v1.11.1-ck8s1](#v1111-ck8s1) - 2022-03-11
- [v1.7.0-ck8s1](#v170-ck8s1) - 2021-12-23
<!-- END TOC -->

!!!note

    These are only the user-facing changes.

### v4.0.6-ck8s3

Released 2025-05-20

!!! warning "Application Developer Notice(s)"

    - Allow applications to use the HTTP(S) management API from application developer namespaces.
    - Network policies for external traffic now properly adapt based on exposed ports.

#### Improvement(s)

- deploy: Add Network Policy enabled flag, enabled by default
- deploy: Allow internal management from application developer namespaces

#### Other(s)

- bug - deploy: Rework internal and external Network Policy rules
- bug - scripts: Handle CNAME records for object storage hosts

### v4.0.6-ck8s2

Released 2025-04-25

#### Other(s)

- Correct script to update Cluster DNS for Network Policies, no Application Developer facing change.

<!--
    Release notes before 2024-11-29 are excluded from spellchecking.
    Please make sure to put new release notes above this line.
-->
<!-- vale off -->

### v4.0.6-ck8s1

Released 2025-02-28

!!! warning "Application Developer Notice(s)"

    - Added Network Policies:
        - For new clusters, these will deny access to the RabbitMQ cluster by default. To gain access to the RabbitMQ clusters, add this label to your pods: `elastisys.io/rabbitmq-<cluster_name>-access: allow`
        - For existing clusters, these will **not** deny access to the RabbitMQ cluster by default. Once your pods have been labeled with `elastisys.io/rabbitmq-<cluster_name>-access: allow`, enforcement can be enabled by sending a Service Request to your Platform Administrator.
    - AMQP 1.0 is now a core protocol, and is always enabled.<br>Classic queue mirroring is now removed.

#### Feature(s)

- Network Policies are added to the Cluster deployments which will deny access by default.

#### Improvement(s)

- RabbitMQ is upgraded v4.0, which is a new major release.

### v3.13.7-ck8s1

Released 2024-12-09

#### Improvement(s)

- Updated Cluster operator to `2.9.0`, updated server to `3.13.7` and monitoring to `2.9.0`.
- Updated the backup process to use `rabbitmqctl` for improved reliability and compatibility.
- Added a `LICENSE` file to the repository to provide clarity on usage and distribution.

### v3.12.6-ck8s1

Released 2024-01-17

#### Updated

- Updated server to `3.12.6`
- Update release process and use new changelog generator

### v3.11.18-ck8s1

Released 2023-07-03

#### Updated

- Updated Cluster operator to `v2.3.0`, updated server to `3.11.18`
- Include updated Overview dashboard

### v3.10.7-ck8s2

Released 2022-11-28

#### Fixed

- **Corrected the Queue Details Grafana dashboard and improved alerting**

### v3.10.7-ck8s1

Released 2022-09-21

!!!note

    From this release the version tracks the RabbitMQ server version rather than the RabbitMQ cluster operator version.

#### Updated

- **Upgraded RabbitMQ server version to `3.10.7`** <br/>
  This is a two minor version jump that introduces new upstream features while remaining compatible with current clients.
  The most exciting features includes the new Stream queue type tuned for bulk messaging, and much improved efficiency for Quorum and Classic queue types.
  See [the upstream changelog](https://www.rabbitmq.com/changelog.html) for more detailed information.

#### Added

- **Added support for external access** <br/>
  Using either a LoadBalancer or NodePort Service, additionally with a self-signed chain of trust to enable TLS and host verification.

#### Changed

- **Improved observability** <br/>
  Improved the alerting and replaced the per queue metrics source and dashboard, removing the need for an external exporter.

### v1.11.1-ck8s2

Released 2022-06-08

#### Changed

- **Reworked monitoring** <br/>
  Added additional metrics collection and a new dashboard to show metrics per queue, and fixed those added by the previous release.
- **Tuned performance** <br/>
  Configured and tuned the performance according to RabbitMQ upstream production checklist.
  Including better constraints to improve scheduling for redundancy.

### v1.11.1-ck8s1

Released 2022-03-11

#### Updated

- **Upgraded RabbitMQ to version `3.8.21`** <br/>
  Using Cluster operator version `1.11.1` providing bugfixes.

#### Added

- **Added definitions-exporter** <br/>
  Taking daily backups of the RabbitMQ messaging topology and users for quick and easy reconfiguring in case of disaster.

#### Changed

- Reduced RabbitMQ privilege for security.
- Improved RabbitMQ observability through better monitoring.

### v1.7.0-ck8s1

Released 2021-12-23

First stable release using RabbitMQ version `3.8.16`!
