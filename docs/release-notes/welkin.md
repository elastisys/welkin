<!--apps-release-notes-start-->

# Release Notes

## Welkin

<!-- BEGIN TOC -->

- [v0.47.1](#v0471) - 2025-07-17
- [v0.47.0](#v0470) - 2025-06-25
- [v0.46.1](#v0461) - 2025-07-17
- [v0.46.0](#v0460) - 2025-05-15
- [v0.45.1](#v0451) - 2025-03-25
- [v0.45.0](#v0450) - 2025-03-21
- [v0.44.2](#v0442) - 2025-03-25
- [v0.44.1](#v0441) - 2025-03-12
- [v0.44.0](#v0440) - 2025-02-21
- [v0.43.3](#v0433) - 2025-03-28
- [v0.43.2](#v0432) - 2025-03-25
- [v0.43.1](#v0431) - 2025-03-12
- [v0.43.0](#v0430) - 2025-01-27
- [v0.42.4](#v0424) - 2025-03-28
- [v0.42.3](#v0423) - 2025-03-25
- [v0.42.2](#v0422) - 2025-03-12
- [v0.42.1](#v0421) - 2025-01-02
- [v0.42.0](#v0420) - 2024-11-14
- [v0.41.0](#v0410) - 2024-10-02
- [v0.40.1](#v0401) - 2024-09-18
- [v0.40.0](#v0400) - 2024-08-21
- [v0.39.2](#v0392) - 2024-09-04
- [v0.39.1](#v0391) - 2024-07-15
- [v0.39.0](#v0390) - 2024-06-19
- [v0.38.2](#v0382) - 2024-06-19
- [v0.38.1](#v0381) - 2024-05-24
- [v0.38.0](#v0380) - 2024-05-17
- [v0.37.0](#v0370) - 2024-04-12
- [v0.36.0](#v0360) - 2024-02-12
- [v0.34.2](#v0342) - 2024-01-16
- [v0.35.1](#v0351) - 2024-01-16
- [v0.34.1](#v0341) - 2023-12-22
- [v0.35.0](#v0350) - 2023-12-20
- [v0.34.0](#v0340) - 2023-11-21
- [v0.33.1](#v0331) - 2023-10-20
- [v0.32.2](#v0322) - 2023-10-20
- [v0.33.0](#v0330) - 2023-09-28
- [v0.32.0](#v0320) - 2023-08-07
- [v0.31.0](#v0310) - 2023-07-17
- [v0.30.1](#v0301) - 2023-06-05
- [v0.30.0](#v0300) - 2023-05-16
- [v0.29.0](#v0290) - 2023-03-16
- [v0.28.1](#v0281) - 2023-03-02
- [v0.28.0](#v0280) - 2023-01-30
- [v0.27.0](#v0270) - 2022-11-17
- [v0.26.0](#v0260) - 2022-09-19
- [v0.25.0](#v0250) - 2022-08-25
- [v0.24.1](#v0241) - 2022-08-01
- [v0.24.0](#v0240) - 2022-07-25
- [v0.23.0](#v0230) - 2022-07-06
- [v0.22.0](#v0220) - 2022-06-01
- [v0.21.0](#v0210) - 2022-05-04
- [v0.20.0](#v0200) - 2022-03-21
- [v0.19.1](#v0191) - 2022-03-01
- [v0.19.0](#v0190) - 2022-02-01
- [v0.18.2](#v0182) - 2021-12-16
- [v0.17.2](#v0172) - 2021-12-16
- [v0.18.1](#v0181) - 2021-12-08
- [v0.17.1](#v0171) - 2021-12-08
- [v0.18.0](#v0180) - 2021-11-04
- [v0.17.0](#v0170) - 2021-06-29
- [v0.16.0](#v0160) - 2021-05-27
<!-- END TOC -->

!!!note

    For a more detailed look check out the full [changelog](https://github.com/elastisys/compliantkubernetes-apps/tree/main/changelog).

<!--
    Release notes before 2024-11-29 are excluded from spellchecking.
    Please make sure to put new release notes above this line.
-->
<!-- vale off -->

## v0.47.1

Released 2025-07-17

### Other(s)

- Fix NetworkPolicy for NGINX to allow uptime Ingress

## v0.47.0

Released 2025-06-25

!!! warning "Application Developer Notice(s)"

    - Alertmanager has been reworked.
       -  The configuration of the user alertmanager secret has been updated. It is now managed via the `alertmanager-kube-prometheus-stack-alertmanager` secret.

### Feature(s)

- Added configuration options to control the user session timeout for OpenSearch Dashboards. These can be adjusted by the administrator.
- Centralized container image configuration

### Improvement(s)

- Improved monitoring stability by inreasing Thanos distributor replicas

## v0.46.1

Released 2025-07-17

## v0.46.0

Released 2025-05-15

!!! danger "Security Notice(s)"

    - Ingress-nginx upgraded to address the following CVEs:
        -CVE-2025-24513
        -CVE-2025-24514
        -CVE-2025-1097
        -CVE-2025-1098
        -CVE-2025-1974

!!! warning "Application Developer Notice(s)"

    - A new GPU access rule is now configured, you need to explicitly request an NVIDIA GPU in your application's resource requests specification to access the GPU drivers.
    - A new gatekeeper policy has been added that will deny any PodDisruptionBudget and connected Pod controller if the PodDisruptionBudget does not allow at least 1 Pod disruption.

### Feature(s)

- Add OPA policy to restrict PDBs, always allow at least 1 disruption
- Add support for Kyverno
- Allow exposing internal Ingress-NGINX LoadBalancer in workload Cluster

### Improvement(s)

- Upgrade Grafana to 11.5.1 (chart 8.9.1)
- Upgrade GPU operator to 24.9.2, allow additional configuration options
- Upgrade Ingress-NGINX chart to v4.12.1
- Upgrade OPA/gatekeeper to v3.18.2
- Upgrade kube-prometheus-stack to 70.6.0

### Other(s)

- Fix GPU driver insufficient for CUDA runtime issue in operator v24.9.2
- Bump kubectl version to v1.31.7 in the requirements

## v0.45.1

Released 2025-03-25

!!! danger "Security Notice(s)"

    - Ingress-NGINX was upgraded to address the following vulnerabilities:
        - CVE-2025-24513
        - CVE-2025-24514
        - CVE-2025-1097
        - CVE-2025-1098
        - CVE-2025-1974

### Other(s)

- Upgraded Ingress-NGINX chart to v4.12.1

## v0.45.0

Released 2025-03-21

!!! danger "Security Notice(s)"

    - Upgraded cert-manager to v1.17.1 which addresses critical [CVE-2024-45337](https://github.com/advisories/GHSA-v778-237x-gjrc)

!!! warning "Application Developer Notice(s)"

    - A new guardrail is added that is enabled by default on ClusterAPI environments. It will by default warn but not deny usage of emptyDir storage, since this can stop cluster autoscaler from scaling down nodes. Read more on [this page](../user-guide/safeguards/enforce-no-local-storage-emptydir.md).
    - A new guardrail is added that is enabled by default on ClusterAPI environments. It will by default warn but not deny usage of Pods without backing controllers, since this can stop cluster autoscaler from scaling down nodes. Read more on [this page](../user-guide/safeguards/enforce-no-pod-without-controller.md).
    - Cert-manager was upgraded to v1.17.1. This comes with some potentially [breaking changes](https://github.com/cert-manager/cert-manager/releases/tag/v1.16.0) for [Venafi Issuer](https://cert-manager.io/docs/configuration/venafi/)
    - RBAC to modify the configmaps `fluentd-extra-config` and `fluentd-extra-plugins`, and to delete any fluentd pod in the `fluentd` namespace has been removed.<br>Reach out to a platform administrator if any additional config or plugins are needed!

### Feature(s)

- Add gatekeeper policies to reject local storage emptydir and reject Pods without controller
- Add cert-manager mixin dashboard

### Improvement(s)

- Update helm/trivy-operator to 0.26.0 and trivy-operator to 0.24.0
- Upgrade cert-manager helm chart to v1.17.1
- Upgrade Thanos chart to v15.13.1

### Deprecation(s)

- Remove rbac for additional Fluentd config and plugins configmaps

### Other(s)

- Change query expression for LessKubeletsThanNodes alerts
- Fixed S3 size alert to not double count postgres buckets

## v0.44.2

Released 2025-03-25

!!! danger "Security Notice(s)"

    - Ingress-NGINX was upgraded to address the following vulnerabilities:
        - CVE-2025-24513
        - CVE-2025-24514
        - CVE-2025-1097
        - CVE-2025-1098
        - CVE-2025-1974

### Other(s)

- Upgraded Ingress-NGINX chart to v4.12.1

## v0.44.1

Released 2025-03-12

!!! warning "Application Developer Notice(s)"

    - Permissions to modify the additional Fluentd ConfigMaps have been removed.<br>Reach out to a Platform Administrator if any changes to the Fluentd config or plugins are needed!

### Deprecation(s)

- Remove permissions for Application Developers to modify the additional Fluentd ConfigMaps

## v0.44.0

Released 2025-02-21

!!! warning "Application Developer Notice(s)"
    - Prometheus has been upgraded to [version 3.0](https://prometheus.io/blog/2024/11/14/prometheus-3-0/). This includes changes to the Prometheus UI. Prometheus V3 comes with some changes that may affect existing PromQL expressions in alerts or dashboards. Please have a look at the Prometheus V3 [migration guide](https://prometheus.io/docs/prometheus/3.0/migration/).
    - The [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html) was added to Welkin. The Operator can be installed by a Platform Administrator and facilitates provisioning GPU on infrastructure providers where this is supported.

### Feature(s)

- Added the NVIDIA GPU Operator.

### Improvement(s)

- Upgraded kube-prometheus-stack to 67.11.0.
- Upgraded Falco to v0.40.0.
- Upgraded Fluentd to v1.18.0.
- Upgraded OpenSearch and OpenSearch Dashboards to v2.18.0.

### Other(s)

- Changed some messages and documentation to Welkin, as part of our rebranding.
- Fixed KubeContainerOOMKilled alert for newly created Pods.

## v0.43.3

Released 2025-03-28

### Other(s)

- Made Fluentd-forwarder image configurable

## v0.43.2

Released 2025-03-25

!!! danger "Security Notice(s)"

    - Ingress-NGINX was upgraded to address the following vulnerabilities:
        - CVE-2025-24513
        - CVE-2025-24514
        - CVE-2025-1097
        - CVE-2025-1098
        - CVE-2025-1974

### Other(s)

- Upgraded Ingress-NGINX chart to v4.12.1

## v0.43.1

Released 2025-03-12

!!! warning "Application Developer Notice(s)"

    - Permissions to modify the additional Fluentd ConfigMaps have been removed.<br>Reach out to a Platform Administrator if any changes to the Fluentd config or plugins are needed!

### Deprecation(s)

- Remove permissions for Application Developers to modify the additional Fluentd ConfigMaps

## v0.43.0

Released 2025-01-27

!!! danger "Security Notice(s)"

    - Upgrades Grafana to `11.3.0` to fix [CVE-2024-9264](https://nvd.nist.gov/vuln/detail/cve-2024-9264)
    - OpenSearch Dashboards was upgraded to `2.17.1` which mitigates [CVE-2024-45801](https://github.com/advisories/GHSA-mmhx-hmjr-r674)

### Improvement(s)

- Upgraded Grafana to 11.3.0 and chart to 8.5.9
- Upgraded OpenSearch to v2.17.1
- Upgraded Harbor to v2.12.1

### Other(s)

- Added JSON schema contribution guide
- Rebrand to Welkin in configuration and documentation

## v0.42.4

Released 2025-03-28

### Other(s)

- Made Fluentd-forwarder image configurable

## v0.42.3

Released 2025-03-25

!!! danger "Security Notice(s)"

    - Ingress-NGINX was upgraded to address the following vulnerabilities:
        - CVE-2025-24513
        - CVE-2025-24514
        - CVE-2025-1097
        - CVE-2025-1098
        - CVE-2025-1974

### Other(s)

- Upgraded Ingress-NGINX chart to v4.12.1

## v0.42.2

Released 2025-03-12

!!! warning "Application Developer Notice(s)"

    - Permissions to modify the additional Fluentd ConfigMaps have been removed.<br>Reach out to a Platform Administrator if any changes to the Fluentd config or plugins are needed!

### Deprecation(s)

- Remove permissions for Application Developers to modify the additional Fluentd ConfigMaps

## v0.42.1

Released 2025-01-02

### Other(s)

- Use Mirror for Bitnami images

## v0.42.0

Released 2024-11-14

### Feature(s)

- Added Prometheus metrics to the diagnostics script

### Improvement(s)

- Upgraded Grafana to v11.2.3.
    - Drops support for dashboards using Angular plugins. See [here](https://grafana.com/docs/grafana/latest/developers/angular_deprecation/) for more information.
- Upgraded Falco to v0.38.2.
- Fix deprecated Grafana dashboards

## v0.41.0

Released 2024-10-02

### Feature(s)

- Added option to use Velero CSI volume snapshot.

### Improvement(s)

- Added NetworkPolicies for Tekton to reduce blast radius.
- Enabled matchConditions for HNC webhook by default.
    - This is used to allow Velero to restore certain resources managed by HNC.
- Fixed deprecated Grafana dashboards.
- Improved support for logging stack on Azure.
- Fixed a bug with Harbor restore on Azure.
- Improvements to automated testing.
- Node-local-dns was upgraded to v1.23.1.
- Added a flag to include config files for diagnostics script.

### Other(s)

- Calico-accountant image and chart was upgraded.

## v0.40.1

Released 2024-09-18

!!! danger "Security Notice(s)"

    - This patch release mitigates the following high and medium severity vulnerabilities:
        - Ingress-NGINX [CVE-2024-7646](https://github.com/kubernetes/kubernetes/issues/126744)
        - Grafana [CVE-2024-6837](https://grafana.com/blog/2024/08/14/grafana-security-release-medium-severity-security-fix-for-cve-2024-6837/)

### Improvement(s)

- Ingress-NGINX was upgraded to v1.11.2 and NGINX itself to v1.25.5.
- Grafana was upgraded to v10.4.7.

### Other(s)

- Fix for install-requirements script.
- Fixed a broken Cluster status dashboard.

## v0.40.0

Released 2024-08-21

!!! warning "Application Developer Notice(s)"

    - Alerts for kured in workload clusters have been removed.

### Improvement(s)

- OpenSearch and OpenSearch Dashboards has been upgraded to v2.15.0.
- Harbor has been upgraded to v2.11.0.
- Dex has been upgraded to v2.40.0.
- Added Node filter to more graphs in the Kubernetes status dashboard.
- Increased default Grafana timeout.
- Improved diagnostics script.

### Other(s)

- Various fixes for install-requirements script.
- Replaced deprecated Angular panels in Daily and Backup Dashboards.

## v0.39.2

Released 2024-09-04

!!! danger "Security Notice(s)"

    - This patch release mitigates the following high and medium severity vulnerabilities:
        - Ingress-NGINX [CVE-2024-7646](https://github.com/kubernetes/kubernetes/issues/126744)
        - Grafana [CVE-2024-6837](https://grafana.com/blog/2024/08/14/grafana-security-release-medium-severity-security-fix-for-cve-2024-6837/)

### Improvement(s)

- Ingress-NGINX was upgraded to v1.11.2 and NGINX itself to v1.25.5.
- Grafana was upgraded to v10.4.7.

## v0.39.1

Released 2024-07-15

### Improvement(s)

- Increased rclone default job deadline to 14400 seconds allowing for rclone to complete its operations.

## v0.39.0

Released 2024-06-19

!!! warning "Application Developer Notice(s)"

    - There is a new feature to allow certain Pods access to Prometheus, e.g. for [remote-read](https://prometheus.io/docs/prometheus/latest/querying/remote_read_api/) or [federation](https://prometheus.io/docs/prometheus/latest/federation/) from another Prometheus instance. This feature has to be enabled by a Platform Administrator, who will require a list of namespaces to allow access from. You must also label each Pod that should have access with `elastisys.io/prometheus-access: allow`.

### Feature(s)

- Add config option to allow internal traffic to Prometheus.

### Improvement(s)

- Trivy Operator was upgraded to v0.20.1.
- Velero was upgraded to v1.13.0.

### Other(s)

- Fixed an error that would occur when applying with rclone enabled.

## v0.38.2

Release 2024-06-19

### Other(s)

- Fixed various platform administrator bugs.

## v0.38.1

Release 2024-05-24

### Other(s)

- Fixed an error that would occur when applying with rclone enabled.

## v0.38.0

Released 2024-05-17

### Feature(s)

- A new Gatekeeper constraint was added. It will warn if the user tries to deploy a Deployment or StatefulSet with less than 2 replicas.

### Improvement(s)

- Thanos was upgraded to v0.34.1.
- Gatekeeper was upgraded to v3.15.1.

## v0.37.0

Released 2024-04-12

### Improvement(s)

- OpenSearch and OpenSearch Dashboards were upgraded to v2.12
- Grafana was upgraded to v10.4
- Falco was upgraded to v0.37.1
- A new capacity management Grafana dashboard is now available. This will give better visibility over resource usage per Node groups
- We recommend using the [ingressClassName](https://cert-manager.io/docs/configuration/acme/http01/#ingressclassname) field over the `class` field for cert-manager issuers

## v0.36.0

Released 2024-02-12

### Feature(s)

- Added some initial disk performance alerts
- Added probe Ingress to monitor services

### Improvement(s)

- Upgrade Velero to v1.11.1

### Other(s)

- bug - Fixed issue where large Harbor backups would fail
- clean-up - Removed the ciskubernetesbenchmark dashboard from Grafana

## v0.34.2

Released 2024-01-16

### Improvement(s)

- Added more configuration options for Trivy-Operator

## v0.35.1

Released 2024-01-16

### Improvement(s)

- Added more configuration options for Trivy-Operator

## v0.34.1

Released 2023-12-22

### Improvement(s)

- Updated trivy-operator helm chart to v0.19.1 and application to v0.17.1

### Other(s)

- bug - Fixed issue where large Harbor backups would fail

## v0.35.0

Released 2023-12-20

!!! danger "Security Notice(s)"

    - Enabling "chroot" for the ingress-nginx controller is one way to limit nginx inside the ingress-nginx controller container from having access to list secrets cluster-wide.
      Note that this also allows the controller to use the `unshare` and `clone` syscalls which are not normally allowed when using the default seccompProfile.

!!! warning "Application Developer Notice(s)"

    - As of Harbor v2.9, Notary V1 is **removed**. If you rely on this for artifact signing, you will need to migrate to one of the alternatives. You can read more about this [here](https://github.com/goharbor/harbor/wiki/Harbor-Deprecates-Notary-v1-Support-in-v2.9.0).

### Feature(s)

- Added option to run NGINX in chroot
- Added support for self-managed Kafka

### Improvement(s)

- Upgrade Harbor to v2.9.1

## v0.34.0

Released 2023-11-23

!!! danger "Security Notice(s)"

    - New curl release (CVE-2023-38545 and CVE-2023-38546)
    - New Go release (https://github.com/advisories/GHSA-qppj-fm5r-hxr3 and https://github.com/advisories/GHSA-4374-p667-p6c8)
    - Fix for HTTP/2 Rapid Reset Attack [CVE-2023-44487](https://nvd.nist.gov/vuln/detail/CVE-2023-44487)

### Feature(s)

- Dashboard for visualizing how spread-out Pods are across Nodes
- Application developers can now self manage CRDs for MongoDB, SealedSecrets and Flux
- Upgrade HNC and expose opt-in propagation

### Improvement(s)

- Update Gatekeeper violation messages
- Add Network Policies for hnc
- Upgrade Ingress-NGINX controller to 1.8.4 and chart to 4.7.3
- Upgrade Falco chart and rework exceptions

## v0.33.1

Released 2023-10-20

### Updated

- **Ingress-NGINX controller to 1.8.4 and chart to 4.7.3 (HTTP/2 fix for CVE-2023-44487)**
    - a limit of no more than 2 \* max_concurrent_streams new streams per one event loop iteration was introduced
    - refused streams are now limited to maximum of max_concurrent_streams and 100

## v0.32.2

Released 2023-10-20

### Updated

- **Ingress-NGINX controller to 1.8.4 and chart to 4.7.3 (HTTP/2 fix for CVE-2023-44487)**
    - a limit of no more than 2 \* max_concurrent_streams new streams per one event loop iteration was introduced
    - refused streams are now limited to maximum of max_concurrent_streams and 100

## v0.33.0

Released 2023-09-28

### Changed

- **Increased the default `proxy-buffer-size` setting in Ingress-NGINX to `8k`.**

### Fixed

- **Refer to Grafana, OpenSearch and Harbor as Web Portals in Grafana and OpenSearch welcome dashboards**

### Removed

- **Removed the deprecated Grafana dashboard Image vulnerabilities.**

## v0.32.0

Released 2023-08-07

### Updated

- **Upgraded Falco chart version to `3.3.0` and app version to `0.35.1`.**

### Added

- **Added support to turn off trailing dots for Grafana.**
    - This fixes an issue with the certificate for Grafana appearing not to be valid on some browsers.

### Changed

- **Increased window for `FrequentPacketsDroppedFromWorkload` and `FrequentPacketsDroppedToWorkload` alerts.**
    - To make it less sensitive to semi-consistent blocked network traffic.
- **Reduced CPU requests for some components in the service Cluster.**

### Fixed

- **Added some default annotations for Harbor that will fix issues with not being able to upload larger images.**
- **Fixed the Gatekeeper Grafana dashboard.**
    - Updated queries to produce correct numbers
    - Removed broken/duplicate panels

## v0.31.0

Released 2023-07-17

### Updated

- **Harbor is upgraded to `v2.8.2`.**
    - This version drops the support for chartmuseum and replaces it with a OCI compatible chart storage. You can find the documentation for how to use OCI compatible chart storage [here](https://goharbor.io/docs/2.7.0/working-with-projects/working-with-images/managing-helm-charts/#manage-helm-charts-with-the-oci-compatible-registry-of-harbor).
    - They are also replacing the Notary image signer with Cosign image signer. You can find the documentation for how to use Cosign to sign images [here](https://goharbor.io/docs/2.7.0/working-with-projects/working-with-images/sign-images/#use-cosign-to-sign-artifacts).
    - Dex is now the default login page.
- **Ingess-NGINX is upgraded to `v1.8.0`.**
- **Grafana is upgraded to `v9.5.5`.**
- **OpenSearch and OpenSearch Dashboard are upgraded to `v2.8.0`.**

### Added

- **Added RBAC for admin users to view events and logs.**
- **Possibility to add custom config for Node-local-dns.**
- **Harbor GC is enabled by default and will run every Sunday at midnight UTC.**

## v0.30.1

Released 2023-06-05

### Updated

- **Update Trivy Operator Dashboard to improve the user experience.**
- **Another Network Policy fix for Harbor to allow garbage collection.**
- **Fixed duplicate exception for Falco alerts.**
- **Update Falco rules and Falco alert exceptions.**

### Changed

- **Change Trivy Operator Dashboard to only count image states once per image instead for each namespace and resource.**

## v0.30.0

Released 2023-05-16

### Added

- **Kubernetes Jobs will now have a default TTL of 7 days if unset to ensure resources are cleaned up.**

### Updated

- **kube-prometheus-stack chart to `v45.2.0`.**
    - the portName for Alertmanager and Prometheus have been renamed from web to http-web. If this port names are used by you application or to port-forward to Prometheus/Alertmanager, you will need to update them to http-web or use the port numbers instead (e.g 9090 for Prometheus and 9093 for Alertmanager);
    - added default metric relabeling for cAdvisor and apiserver metrics to reduce cardinality;
    - Alertmanager, using regex field from the Matcher type is deprecated and it will be removed in a future version.

### Changed

- **Kubernetes PodSecurityPolcies have been replaced with Kubernetes Pod Security Standards and additional Gatekeeper Constraints and Mutations.**
    - This should not affect user applications as the default behavior is kept, and the new default restricted Pod Security Standard is slightly less restricted than the previous restricted PodSecurityPolicy following the upstream changes;
    - You might see `warnings` generated by PodSecurity while deploying manifests into your Kubernetes Cluster, if fields are unset or do not follow the [Restricted policy for the Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/#restricted). If fields are unset, the new Gatekeeper mutations will set defaults, that follow the restricted Pod Security Standards, as the Pods get scheduled.
- **Trivy Operator has replaced Starboard Operator as the online security scanning tool.**
    - This includes a new Trivy Operator dashboard and the deprecation of the old Image vulnerabilities dashboard.
- **Both `responseObject` and `requestObject` are no longer dropped in Fluentd from Kubernetes audit events.**
- **Changed timekey to stageTimestamp for Kubernetes audit logs. Use auditID to correlate stages of the same request.**

### Removed

- **Remove HNC admin-rbac from admin (attached to user admins).**
    - User admins will now only have the HNC user-rbac instead.
- **Removed the ability to edit HierarchyConfiguration for users.**
    - HierarchyConfiguration controls the Pod Security Standard level, and as such should not be allowed to be changed by a user.
- **Disable Non sudo setuid Falco rule.**

## v0.29.0

Released 2023-03-16

### Added

- **Static users can now be added in OpenSearch.**

### Changed

- **The Fluentd Deployment has changed considerably and users must ensure that their custom filters continue to work as expected.**

### Updated

- **cert-manager updated to `v1.11.0`.**
    - The containers in Pods created by cert-manager have been renamed to better reflect what they do. This can be breaking for automation that relies on these names being static.
    - The cert-manager Gateway API integration now uses the v1beta1 API version. ExperimentalGatewayAPISupport alpha feature users must upgrade to v1beta of Gateway API.

## v0.28.1

Released 2023-03-02

### Added

- **Added Falco rules to ignore Redis operator related alerts.**

## v0.28.0

Released 2023-01-30

### Changed

- **Updated Rook alerts to `v1.10.5`.**
- **NGINX Ingress Controller service can now have multiple annotations instead of just one.**
- **Synced all Grafana dashboards to use the default organization timezone.**
- **Several default resource requests and limits have changed for the included services.**

### Fixed

- **Use FQDN for services connecting from the Workload Cluster to the service Cluster to prevent resolve timeouts.**
- **Fixed `KubeletDown` alert rule not alerting if a kubelet was missing.**
- **Added permissions to the `alerting_full_access` role in OpenSearch to be able to view notification channels.**
- **Added `fluent-plugin-record-modifier` to the Fluentd image to prevent mapping errors.**
- **Various fixes to Network Policies.**

### Added

- **Improved security posture by adding Network Policies for some of the networking and storage components.**
- **Added alert for less kubelets than Nodes in the Cluster.**
- **Added alert for object limits in buckets.**

## v0.27.0

Released 2022-11-17

### Updated

- **Updated Dex helm chart to `v0.12.0`, which also upgrades Dex to `v2.35.1`.**
- **Updated Falco helm chart to `2.2.0`, which also upgrades Falco to `0.33.0` and Falco Sidekick to `2.26.0`.**
- **Updated Falco Exporter helm chart to `0.9.0`, which also upgrades Falco Exporter to `0.8.0`.**
- **Updated Velero helm chart to `v2.31.8`, which also upgrades Velero to `v1.9.2`.**
- **Updated Grafana helm chart to `v6.43.4`, which also upgrades Grafana to `v9.2.4`.**

### Changed

- **Improved Network security by adding Network Policies to a lot of the included services.**
- **NetworkPolicies are now automatically propagated from a parent namespace to its subnamespaces in HNC.**
- **Several default resource requests and limits have changed for the included services.**
- **Lowered the default retention age for Kubernetes logs in the prod flavor down to 30 days.**
- **Made Dex ID Token expiration time configurable.**
- **User Alertmanager is now enabled by default.**

### Fixed

- **Fixed an issue with the "Kubernetes Cluster status" Grafana dashboard not loading data for some panels**
- **Rclone can now be configured to run every x minutes/hours/days/week/month/year.**

### Added

- **Added RBAC for admin users to view Gatekeeper constraints.**
- **New section in the welcoming dashboards, displaying the most relevant features and changes for the user added in the last two releases.**
- **Added an option to configure alerts for growing indices in OpenSearch.**
    - **The settings for this might need to be tweaked to better suit the environment.**
- **Added an alert for failed evicted Pods (KubeFailedEvictedPods).**

## v0.26.0

Released 2022-09-19

### Updated

- **Harbor upgraded to `v2.6.0`**
- **Upgraded OpenSearch helm chart to `2.6.0`, this upgrades OpenSearch to `2.3.0`. For more information about the upgrade, check out their [2.3 Launch Announcement](https://opensearch.org/blog/opensearch-2-3-is-ready-for-download/).**

### Fixed

- **Fixed the welcome dashboard template for OpenSearch Dashboards**

### Added

- **Option to create custom solvers for Let's Encrypt issuers, including a simple way to add secrets**
- **Kube-bench runs on every Node**
  Automated CIS tests are performed on each Node using kube-bench
  Added a CIS kube-bench Grafana dashboard
- **Added option for kured to notify to slack when draning and rebooting Nodes**
- **Allow users to proxy and port-forward to Prometheus running in the Workload Cluster**

## v0.25.0

Released 2022-08-25

### Added

- **Added Hierarchical Namespace Controller**<br/> Allowing users to create and manage subnamespaces, namespaces within namespaces. You can read more about this in our [FAQ](../user-guide/faq.md#how-do-i-add-a-new-namespace).
- **Added support for custom solvers in Cluster issuers** <br/> Allowing DNS01 challenges for certificate requests.
- **Added support for running Harbor in High Availability**

### Updated

- **Updated cert-manager from v1.6.1 to v1.8.2** <br/> API versions `v1alpha2`, `v1alpha3`, and `v1beta1` have been removed from the custom resource definitions (CRDs), certificate rotation policy will now be validated. See their [changelog](https://github.com/cert-manager/cert-manager/releases) for more details.

- **Updated OpenSearch with new usability improvements and features** <br/> Checkout their [launch announcement](https://opensearch.org/).

### Changed

- **New additions to the Kubernetes Cluster status Grafana dashboard** <br/> It now shows information about resource requests and limits per Node, and resource usage vs request per Pod.

## v0.24.1

Released 2022-08-01

- **Required patch to be able to use release `v0.24.0`**<br/>

### Fixed

- Fixed a formatting issue with Harbor S3 configuration.

## v0.24.0

Released 2022-07-25

### Updated

- **Upgraded Helm stack**<br/>
  Upgrades for Helm, Helmfile and Helm-secrets.

- **Image upgrade to Node-local-dns**<br/>

### Changed

- **Improved stability to automatic Node reboots**<br/>

### Added

- **Further configurability to Ingress-NGINX**<br/>

## v0.23.0

Released 2022-07-06

### Updated

- **Updated the Ingress Controller `ingress-nginx` to image version v1.2.1**<br/>
    - You can find the changelog [here](https://github.com/kubernetes/ingress-nginx/releases/tag/controller-v1.2.1).

### Changed

- **Added support for accessing Alertmanager via port-forward**<br/>

### Added

- **Backups can now be encrypted before they are replicated to an off-site S3 service.**<br/>
- **Improved metrics and alerting for OpenSearch.**<br/>

### Fixed

- **The Deployment of Dex is now properly configured to be HA, ensuring that the Dex instances are placed on different Kubernetes worker Nodes.**<br/>

## v0.22.0

Released 2022-06-01

### Added

- **Added support for Elastx and UpCloud!**<br/>

- **New 'Welcoming' dashboard in OpenSearch and Grafana.**<br/>
  Users can now access public docs and different urls to the services provided by Welkin.

- **Improved availability of metrics and alerting.**<br/>
  Alertmanager now runs with two replicas by default, Prometheus can now be run in HA mode.

- **Added Falco rules to reduce alerts for services in Welkin.**<br/>
  Falco now alerts less on operations that are expected out of these services.

### Fixed

- **Fixed a bug where users couldn't silence alerts when portforwarding to Alertmanager.**<br/>

- **Improved logging stack and fixed a number of issues to ensure reliability.**<br/>

## v0.21.0

Released 2022-05-04

### Changed

- **Users can now view ClusterIssuers.**<br/>

- **User admins can now add users to the ClusterRole user-view.**<br/>
  This is done by adding users to the ClusterRoleBinding `extra-user-view`.

- **User can now get ClusterIssuers.**<br/>

- **Ensured all CISO dashboards are available to users.**<br/>
  All the Grafana dashboards in our [CISO docs](../ciso-guide/index.md) are now available.

- **Better stability for Dex**<br/>
  Dex now runs with two replicas and has been updated.

### Updated

- **Image upgrades to reduce number of vulnerabilities**<br/>
  Upgrades for Fluentd, Grafana, and Harbor chartmuseum.

## v0.20.0

Released 2022-03-21

### Added

- **Added kured - Kubernetes Reboot Daemon.**<br/>
  This enables automatic Node reboots and security patching of the underlying base Operating System image, container runtime and Kubernetes Cluster components.

- **Added Fluentd Grafana dashboard and alerts.**<br/>

- **Added RBAC for admin users.**<br/>
  Admin users can now list Pods Cluster wide and run the kubectl top command.

- **Added containerd support for Fluentd.**<br/>

### Changed

- **Added the new OPA policy.**<br/>
  To disallow the latest image tag.

- **Persist Dex state in Kubernetes.**<br/>
  This ensure the JWT token received from an OpenID provider is valid even after security patching of Kubernetes Cluster components.

- **Add ingressClassName in ingresses where that configuration option is available.**<br/>

- **Thanos is now enabled by default.**<br/>

### Updated

- **Upgraded Ingress-NGINX helm chart to v4.0.17**<br/>
  This upgrades Ingress-NGINX to v1.1.1. When upgrading an ingressClass object called NGINX will be installed, this class has been set as the default class in Kubernetes. Ingress-NGINX has been configured to still handle existing Ingress objects that do not specify any ingressClassName.

- **Upgraded starboard-operator helm chart to v0.9.1**<br/>
  This is upgrading starboard-operator to v0.14.1

### Removed

- **Removed influxDB and dependent helm charts.**<br/>

## v0.19.1

Released 2022-03-01

### Fixed

- Fixed critical stability issue related to Prometheus rules being evaluated without metrics.

## v0.19.0

Released 2022-02-01

### Added

- **Added Thanos as a new metrics backend.**<br/>
  Provides a much more efficient and reliable platform for long-term metrics, with the capabilities to keep metrics for much longer time periods than previously possible.<br/>
  InfluxDB will still be supported in this release.

- **Added a new feature to enable off-site replication of backups.**<br/>
  Synchronizes S3 buckets across regions or clouds to keep an off-site backup.

- **Added a new feature to create and log into separate indices per namespace.**<br/>
  _Currently considered to be an alpha feature._

### Changed

- **Replacing Open Distro for Elasticsearch with OpenSearch.**<br/>
  In this release, since [the Open Distro project has reached end of life](https://opendistro.github.io/for-elasticsearch/), Elasticsearch is replaced with OpenSearch and Kibana with OpenSearch Dashboards.
  OpenSearch is a fully open source fork of Elasticsearch with a compatible API and familiar User Experience.<br/>
  _Note that recent versions of official Elasticsearch clients and tools will not work with OpenSearch as they employ a product check, compatible versions can be found [here](https://opensearch.org/docs/latest/clients/index/)._

- **Enforcing OPA policies by default.**<br/>
  Provides [strict safeguards](../user-guide/safeguards/index.md) by default.

- **Allowing viewers to inspect and temporarily edit panels in Grafana.**<br/>
  Gives more insight to the metrics and data shown.

- **Setting Fluentd to log the reason why when it can't push logs to OpenSearch.**

### Updated

- Large number of application and service updates, keeping up to date with new security fixes and changes.

## v0.18.2

Released 2021-12-16.

Changes:

- Updated Open Distro for Elasticsearch to 1.13.3 to mitigate [CVE-2021-44228 & CVE-2021-45046](https://opendistro.github.io/for-elasticsearch/blog/2021/12/update-to-1-13-3/)

## v0.17.2

Released 2021-12-16.

Changes:

- Updated Open Distro for Elasticsearch to 1.13.3 to mitigate [CVE-2021-44228 & CVE-2021-45046](https://opendistro.github.io/for-elasticsearch/blog/2021/12/update-to-1-13-3/)

## v0.18.1

Released 2021-12-08.

Changes:

- updated Grafana to 8.0.7 in order to fix [CVE-2021-43798](https://grafana.com/blog/2021/12/07/grafana-8.3.1-8.2.7-8.1.8-and-8.0.7-released-with-high-severity-security-fix/)

## v0.17.1

Released 2021-12-08.

Changes:

- updated Grafana to 8.0.7 in order to fix [CVE-2021-43798](https://grafana.com/blog/2021/12/07/grafana-8.3.1-8.2.7-8.1.8-and-8.0.7-released-with-high-severity-security-fix/)

## v0.18.0

Released 2021-11-04.

Changes:

- Ingress-NGINX-controller has been updated from v0.28.0 to v0.49.3, bringing various updates.
    - Additionally, the configuration option `allow-snippet-annotations` has been set to `false` to mitigate known security issue [CVE-2021-25742](https://github.com/kubernetes/ingress-nginx/issues/7837)
- Fixes, minor version upgrades, improvements to resource requests and limits for applications, improvements to stability.

## v0.17.0

Released 2021-06-29.

Changes:

- The dashboard tool Grafana has been updated to a new major version of 8.x.x. This introduces new features and fixes, as well as some possibly breaking changes. See their [release notes](https://grafana.com/docs/grafana/v8.0/whatsnew/whats-new-in-v8-0/) for more information.
- The single-sign-on service Dex has been updated, bringing small changes and better consistency to the UI.
- Fixes, improvements to resource limits, resource usage, and stability.

## v0.16.0

Released 2021-05-27.

Changes:

- The default retention values have been changed and streamlined for `authlog*` and `other*`. The former will be kept for a longer period of time while the latter for shorter, both have reduced sized according to their actual usage.
- Updates, fixes, and features to improve the security of the platform.
<!--apps-release-notes-end-->
