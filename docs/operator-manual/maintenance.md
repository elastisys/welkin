---
tags:
  #- ISO 27001:2013 A.12.6.1 Management of Technical Vulnerabilities
  - BSI IT-Grundschutz APP.4.4.A21
  - HIPAA S16 - Security Awareness and Training - Security Reminders - § 164.308(a)(5)(ii)(A)
  - MSBFS 2020:7 4 kap. 12 §
  - NIST SP 800-171 3.4.5
  - NIST SP 800-171 3.7.1
---

# Maintaining and Upgrading your Welkin environment

In order to keep your Welkin environment running smoothly, and to assure that you are up to date with the latest patches you need to perform regular maintenance on it.

This guide assumes that:

- Your Welkin environment is running normally, if not, please see the [Troubleshooting guide](troubleshooting.md).
- Your Welkin environment is properly [sized](cluster-sizing.md)
- You have performed the actions in the [Go-live Checklist](../user-guide/go-live.md) as failure to do so might cause downtime during maintenance.

## Compliance needs

Many regulations require you to secure your information system against unauthorized access, data loss, and breaches.
An important part of this is keeping your Welkin environment up to date with the latest security patches to not run outdated versions of components that are no longer supported.
This maps to objectives in ISO Annex [A.12.6.1 Management of Technical Vulnerabilities](https://www.isms.online/iso-27001/annex-a-12-operations-security/).

## What maintenance do I need to do and how?

In short, there are three levels of maintenance that should be performed on a regular basis.

- Patching the underlying OS on the Nodes
- Upgrading the Welkin application stack
- Upgrading Welkin Core (Kubespray or Cluster-API)

> [!NOTE]
> These docs only include maintenance steps for Kubespray and not Cluster-API.

Let's go through them one by one.

> [!IMPORTANT]
> Welkin advises against rollbacks and instead argues for performing staged rollouts and, in the case that a defective patch made it all the way to production, perform a rollforward instead.
> Performing a rollback for distributed and stateful applications can be a very complex process, is prone to errors and can lead to data- loss, inconsistencies, corruption etc.
> To avoid such issues, we recommend the following:
>
> - It is recommended to have separate staging and production environments, so that each new release is first tested in the staging environment before upgrading production.
> - If issues are encountered in production, it is recommended to address and patch those issues instead of doing a rollback.

### Patching the Nodes

Security patches for the underlying OS on the Nodes are constantly being released, and to ensure your environment is secured, the Nodes that run Welkin must be updated with these patches.
We recommend that you use the [AutomaticSecurityUpdates](https://help.ubuntu.com/community/AutomaticSecurityUpdates) feature that is available in Ubuntu (similar feature exist in other Linux distributions) to install these updates.
Note that the Nodes still need to be rebooted for some of these updates to be applied.
In order to reboot the Nodes, you can either use a tool like [kured](https://github.com/kubereboot/kured) or you can do it manually by logging on to the Nodes and rebooting them manually.
When doing that, reboot one Node at the time and make sure that the rebooted Node is 'Ready' and that Pods are scheduled to it before you move on to the next, or you risk downtime.

There is a playbook in the compliantkubernetes-kubespray repository that can assist with the reboot of Nodes.
It will cordon and reboot the Nodes one by one.

```bash
./bin/ck8s-kubespray reboot-nodes <wc|sc> [--extra-vars manual_prompt=true] [<options>]
```

### Upgrading the Welkin application stack

Welkin consists of a multitude of open source components that interact to form a smooth End User experience.
In order to free you of the burden of keeping track of when to upgrade the various components, new versions of Welkin are regularly released.
When a new version is released, it becomes available as a [tagged release](https://github.com/elastisys/compliantkubernetes-apps/tags) in the GitHub repository.

> [!NOTE]
> Before upgrading to a new release, please review the [changelog](https://github.com/elastisys/compliantkubernetes-apps/tree/main/changelog) and if possible, apply the upgrade to a staging environment before upgrading any environments with production data.

#### Prerequisites

- [ ] Notify the users (if any) before the upgrade starts;
- [ ] Check if there are any pending changes to the environment;
- [ ] Check the state of the environment, Pods, Nodes and backup jobs:

> [!NOTE]
> the below steps should be run from compliantkubernetes-apps root directory.

```bash
./bin/ck8s test sc|wc
./bin/ck8s ops kubectl sc|wc get pods -A -o custom-columns=NAMESPACE:metadata.namespace,POD:metadata.name,READY-false:status.containerStatuses[*].ready,REASON:status.containerStatuses[*].state.terminated.reason | grep false | grep -v Completed
./bin/ck8s ops kubectl sc|wc get nodes
./bin/ck8s ops kubectl sc|wc get jobs -A
./bin/ck8s ops velero sc|wc get backup
```

- [ ] Silence the notifications for the alerts. e.g you can use [Alertmanager silences](https://prometheus.io/docs/alerting/latest/alertmanager/#silences);

#### Upgrading compliantkubernetes-apps

For security, compliance, and support reasons, environments should stay up to date with the latest version of [compliankubernetes-apps](https://github.com/elastisys/compliantkubernetes-apps).

Note what version of compliantkubernetes-apps that is currently used and the version that you want to upgrade to.
Then check the release notes for each version in between to see if there are anything that might cause any problems, if so then consult the rest of the operations team before proceeding.
**You should never upgrade more than one minor version of compliantkubernetes-apps at a time.**

Check and follow the migration document for the release you want to upgrade to: <https://github.com/elastisys/compliantkubernetes-apps/tree/main/migration>

### Upgrading Kubespray/Kubernetes

All Clusters should stay up to date with the latest Kubespray version used in [compliantkubernetes-kubespray](https://github.com/elastisys/compliantkubernetes-kubespray).

Note what version of Kubespray that is currently used in the Cluster and the Kubespray version you want to upgrade to.
Then check the release notes for each version in between to see if there are anything that might cause any problems, if so then consult the rest of the operations team before proceeding.
Also check if the newer Kubespray version would upgrade Kubernetes to a new minor version, if so then Application Developers should get a notice of x weeks before proceeding to let them check for any deprecated APIs that they might be using.
**You should never upgrade more than one minor version of compliantkubernetes-kubespray at a time.**
Read more about Kubespray upgrades in their [documentation](https://kubespray.io/#/docs/operations/upgrades).

Check and follow the migration document for the release you want to upgrade to: <https://github.com/elastisys/compliantkubernetes-kubespray/tree/main/migration>

### After doing any upgrades or maintenance

- [ ] Check the state of the environment, Pods and Nodes:

> [!NOTE]
> the below steps should be run from compliantkubernetes-apps root directory.

```bash
./bin/ck8s test sc|wc
./bin/ck8s ops kubectl sc|wc get pods -A -o custom-columns=NAMESPACE:metadata.namespace,POD:metadata.name,READY-false:status.containerStatuses[*].ready,REASON:status.containerStatuses[*].state.terminated.reason | grep false | grep -v Completed
./bin/ck8s ops kubectl sc|wc get nodes
```

- [ ] Check if any alerts generated by the upgrade didn't close;
- [ ] Check if you can login to Grafana, OpenSearch or Harbor;
- [ ] Enable the notifications for the alerts;
- [ ] Notify the users (if any) when the upgrade is complete;
- [ ] Check that you can see fresh metrics and logs.
