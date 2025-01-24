---
tags:
  - ISO 27001 A.12.4.3 Administrator & Operator Logs
  - HIPAA S18 - Security Awareness, Training, and Tools - Log-in Monitoring - § 164.308(a)(5)(ii)(C)
  - HIPAA S48 - Audit Controls - § 164.312(b)
  - MSBFS 2020:7 4 kap. 16 §
  - HSLF-FS 2016:40 4 kap. 9 § Kontroll av åtkomst till uppgifter
  - NIST SP 800-171 3.1.7
  - NIST SP 800-171 3.3.1
---

# Audit Logs

To help comply with various data protection regulations, Welkin comes built-in with audit logs, which can be accessed via [OpenSearch Dashboard](../user-guide/logs.md).

## What are audit logs?

In brief, audit logs are lines answering "**who** did **what** and **when**?".

## Why are audit logs important?

Audit logs help both with proactive and reactive security:

- Regular audit [log reviews](log-review.md) give you a chance to catch an attacker before they succeed.
- After-the-fact, audit logs allow you to gather evidence for forensics and assess the extend of the damage caused by an attacker.

## What audit logs are included?

Welkin follow a risk-based approach to audit logs.
We enable audit logs on all APIs which can be used to compromise data security.
Then we filter high-volume low-risk audit logs.
Don't forget that, at the end of the day, logs are only as useful as someone looks at them.
See [log review](log-review.md) for details.

Specifically, the following audit logs are configured by default:

- Kubernetes API audit logs;
- SSH access logs.

Further audit logs can be configured on a case-by-case basis, as described below.

## Kubernetes API Audit Logs

The audit logs are stored in the `kubeaudit*` index pattern.
The audit logs cover calls to the Kubernetes API, specifically **who** did **what** and **when** on **which** Kubernetes cluster.

Thanks to integration with [your Identity Provider](../user-guide/kubernetes-api.md#authentication-and-access-control-in-welkin) (IdP), if who is a person, their email address will be shown. If who is a system -- e.g., a CI/CD pipeline -- the name of the ServiceAccount is recorded.

Your change management or incident management process should ensure that you also cover **why**.

Both users (Application Developers) and administrators will show in the audit log. The former will change resources related to their application, whereas the latter will change Welkin system components.

The exact configuration of the Kubernetes audit logs can be found [here](https://github.com/elastisys/compliantkubernetes-kubespray/blob/main/config/common/group_vars/k8s_cluster/ck8s-k8s-cluster.yaml).

To view the audit logs for a specific user:

1. Open the `Audit user` dashboard in OpenSearch;
1. Under `User selector` add the name of the user you want to audit (e.g <admin@example.com>);
1. Apply changes;

![Example of Audit Logs](img/audit-logs.png)

## SSH Access Logs

Welkin also captures highly privileged SSH access to the worker Nodes in the `authlog*` index pattern. Only administrators should have such access.

![Example of SSH Access Logs](img/authlog.png)

!!!note

    This section helps you implement ISO 27001, specifically:

    - A.9.2.1 User Registration and Deregistration

    Many data protection regulation will require you to [individually identify administrators](../adr/0005-use-individual-ssh-keys.md), hence individual SSH keys. This allows you to individually identify administrators in the SSH access log.

### Assessment on Usage of Group Accounts

Usage of group accounts needs to be clearly specified, according to:

- [BDEW Requirement 4.5.2](https://www.bdew.de/media/documents/BDEW-OE-VSE-Whitepaper-3.0.pdf);
- ISO/IEC 27002:2022 5.16, 5.17, 5.18, 8.5, 8.15;
- ISO/IEC 27019:2017 9.2.1, 9.3.1, 9.4.2, 12.4.1

Furthermore, a clear assessment needs to documented to show that such usage does not add an unacceptable risk.
This section provides such an assessment.

Platform administrators need to perform certain operations, such as Kubespray upgrades and incident resolution, via a very privileged access.
Welkin recommends such access be done by SSH-ing using the group account `ubuntu` with individual SSH keys, then using `sudo` to gain access to the `root` account.
This is standard practice with the [Ubuntu Cloud Images](https://cloud-images.ubuntu.com/) recommended by Welkin.

We assessed such usage not to pose unnecessary risk because:

- The individual having logged in can be identified in the SSH Access Logs by looking at the IP address and SSH key.
Seeing a log line `EVE_IP logged in as EVE_USERNAME using EVE_SSH_KEY` does not reduce any risk compared to `EVE_IP logged in as ubuntu using EVE_SSH_KEY`.
Hence, in case of an insider attack or a platform administrator account take-over, one can already narrow down a list of suspected individuals.
- Even with individual accounts, we are extremely limited in knowing exactly what the platform administrator did after they logged in, due to technical reasons.
Most interesting actions are often hidden in temporary scripts, such as those installed in `/tmp` during normal Ansible usage.
If we really wanted to be 100% able to prove that an individual did something bad, then we would need individual accounts _and_ individual root accounts _and_ eBPF intercept all syscalls _and_ log these into a tamper-proof environment.
This is, of course, not technically impossible, however very costly in terms of system resources -- not to mention questionable in terms of added security, given the permissions of root accounts.

To mitigate the risk of insider attacks or platform administrator account take-over, Welkin recommends the following security measures:

- Severely limit the number of people with platform administrator access.
- Do background checks on people with platform administrator access.
- Enforce security hygiene on platform administrator workstations, e.g., no personal errands nor unauthorized applications.
- Enforce storing SSH keys on a Hardware Security Module (HSM) which requires user interaction before logging in, such as [YubiKeys](https://www.yubico.com/).

Regarding the last point, the BDEW white paper itself recommends:

> Where technically possible, strong 2-factor authentication shall be used, e.g. through the use of tokens or smart cards.

Note that, except these two group accounts on the underlying Linux operating system level on Nodes (`ubuntu` and `root`), all Welkin access happens via individual accounts, as illustrated in the [Credentials](../operator-manual/credentials.md) page.

## Audit Logs for Additional Services

The Kubernetes Audit Logs capture user access to additional services, i.e., `kubectl exec` or `kubectl port-forward` commands. Additional services usually do not have audit logging enabled, since that generates a lot of log entries. Too often the extra bandwidth, storage capacity, performance loss comes with little benefit to data security.

**Prefer audit logs in your application to capture audit-worthy events**, such as login, logout, patient record access, patient record change, etc. Resist the temptation to enable audit logging too "low" in the stack. Messages like "Redis client connected" are plenty and add little value to your data protection posture.

Out of all additional services, audit logging for the [database](../user-guide/additional-services/postgresql.md) makes the most sense. It can be enabled via [PGAudit](https://github.com/pgaudit/pgaudit/blob/master/README.md). Make sure you discuss your auditing requirements with the service-specific administrator, to ensure you find the best risk-reduction-to-implementation-cost trade-off. Typically, you want to discuss:

- which databases and tables are audited: e.g., audit `app.users`, but not `app.emailsSent`;
- what operations are audited: e.g., audit `INSERT/UPDATE/DELETE`, but not `SELECT`;
- by which users: e.g., audit person access, but not application access.

## Further Reading

- [Kubernetes Auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)
- [PGAudit](https://www.pgaudit.org/)
