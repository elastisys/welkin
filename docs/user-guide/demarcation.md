---
description: The demarcation between what users can and cannot do in Welkin, the Kubernetes platform for software critical to our society
search:
  boost: 2
tags:
  - BSI IT-Grundschutz APP.4.4.A3
  - HIPAA S13 - Information Access Management - Access Authorization - § 164.308(a)(4)(ii)(B)
  - HIPAA S14 - Information Access Management - Access Establishment and Modification - § 164.308(a)(4)(ii)(C)
  - HIPAA S43 - Access Control - § 164.312(a)(1)
  - MSBFS 2020:7 4 kap. 3 §
  - MSBFS 2020:7 4 kap. 4 §
  - HSLF-FS 2016:40 4 kap. 3 § Styrning av behörigheter
  - NIST SP 800-171 3.1.15
  - NIST SP 800-171 3.13.3
  - NIS2 Minimum Requirement (i) Access Control
  - ISO 27001 Annex A 5.3 Segregation of Duties
  - ISO 27001 Annex A 8.2 Privileged Access Rights
---

<!-- markdownlint-disable-file first-line-h1 -->

!!!danger "TL;DR: You **cannot** install:"

    * ClusterRoles, ClusterRoleBindings
    * Roles and RoleBindings that would [escalate your privileges](../architecture.md)
    * CustomResourceDefinitions (CRDs)
    * PodSecurityPolicies
    * ValidatingWebhookConfiguration, MutatingWebhookConfiguration

    **This means that generally you cannot deploy [Operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/).**

!!!danger "TL;DR: You **cannot**:"

    * Run containers as root (`uid=0`)
    * SSH into any Node

# Can I?

Welkin comes with a lot of guardrails to ensure you protect your business reputation and earn the trust of your Application Developers. Furthermore, it is a good idea to keep regulators happy, since they bring public trust into digitalization. Public trust is necessary to shift Application Developers away from pen-and-paper to drive usage of your amazing application.

If you used Kubernetes before, especially if you acted as a Platform Administrator, then being a Welkin user might feel a bit limiting. For example, you might not be able to run containers with root (`uid=0`) as you were used to. Again, these are not limitations, rather guardrails.

## Why?

As previously reported, [Kubernetes is not secure by default, nor by itself](https://www.techtarget.com/searchitoperations/news/252487963/Kubernetes-security-defaults-prompt-upstream-dilemma).
This is due to the fact that Kubernetes prefers to keep its "wow, it just works" experience. This might be fine for a company that does not process personal data. However, if you are in a regulated industry, for example, because you process personal data or health information, your regulators will be extremely unhappy to learn that your platform does not conform to security best practices.

In case of Welkin this implies a clear separation of roles and responsibilities between Welkin users and administrators.
The mission of administrators is to make you, the Welkin user, succeed. Besides allowing you to develop features as fast as possible, the administrator also needs to ensure that you build on top of a platform that lives up to regulatory requirements, specifically data privacy and data security regulations.

## General Principle

Welkin does not allow users to make any changes which may compromise the security of the platform. This includes compromising or working around access control, logging, monitoring, backups, alerting, etc. For example, accidental deletion of the CustomResourceDefinitions of Prometheus would prevent administrators from getting alerts and fixing Cluster issues before your application is impacted. Similarly, accidentally deleting Fluentd Pods would make it impossible to capture the Kubernetes audit log and investigate data breaches.

## Specifics

To stick to the general principles above, Welkin comes with some technical guardrails. These are implemented through [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) enforcing that user namespaces adhere to the `restricted` [Pod Security Standard](https://kubernetes.io/docs/concepts/security/pod-security-standards/#restricted), in combination with OPA Policies and RBAC. This list may be updated in the future to take into account the fast evolving risk and technological landscape.

More technically, Welkin does not allow users to:

<!--guardrails-start-->
- change the Kubernetes API through [CustomResourceDefinitions](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) or [Dynamic Webhooks](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#what-are-admission-webhooks);
- run container images as root or mount [`hostPath`s](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath);
- mutate ClusterRoles or Roles so as to [escalate privileges](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#privilege-escalation-prevention-and-bootstrapping);
- mutate Kubernetes resources in administrator-owned namespaces, such as `monitoring` or `kube-system`;
- re-configure system Pods, such as Prometheus or Fluentd;
- access the hosts directly.
<!--guardrails-end-->

## But what if I really need to?

Unfortunately, many application asks for more permissions than Welkin allows by default. When looking at the Kubernetes resources, the following are problematic:

- ClusterRoles, ClusterRoleBindings
- Too permissive Roles and RoleBindings
- Namespaces that do not have the `restricted` Pod Security Standard enforced
- CustomResourceDefinitions
- WebhookConfiguration

In such a case, ask your administrator to make a risk-reward analysis. As long as they stick to the general principles, this should be fine. However, as much as they want to help, they might not be allowed to say "yes". Remember, administrators are there to help you focus on application development, but at the same time they have a responsibility to protect your application against security risks.
