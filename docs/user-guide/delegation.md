---
description: How to delegate and work with permissions in Welkin, the Kubernetes platform for software critical to our society
search:
  boost: 2
tags:
  #- ISO 27001:2013 A.9.4.1 Information Access Restriction
  - BSI IT-Grundschutz APP.4.4.A3
  - HIPAA S13 - Information Access Management - Access Authorization - § 164.308(a)(4)(ii)(B)
  - HIPAA S14 - Information Access Management - Access Establishment and Modification - § 164.308(a)(4)(ii)(C)
  - HIPAA S43 - Access Control - § 164.312(a)(1)
  - HIPAA S44 - Access Control - Unique User Identification - § 164.312(a)(2)(i)
  - MSBFS 2020:7 4 kap. 3 §
  - MSBFS 2020:7 4 kap. 4 §
  - NIST SP 800-171 3.1.2
  - NIST SP 800-171 3.1.4
  - NIST SP 800-171 3.1.5
  - NIST SP 800-171 3.1.6
  - NIS2 Minimum Requirement (i) Access Control
  - ISO 27001 Annex A 5.15 Access Control
---

# How to Delegate?

!!!note

    This section helps you implement ISO 27001, specifically:

    - A.9.4.1 Information Access Restriction

Now that you are almost ready to go live, you will certainly want to delegate some permissions to other team members or IT systems in your organization.
This page shows you how to do that.

## Authentication vs. Access Control

[Authentication](https://en.wikipedia.org/wiki/Authentication) is the act of proving your identity. Welkin is usually configured to use your organization's Identity Provider (IdP). Examples of supported IdPs include Google, Microsoft Entra ID, and [Jump Cloud](https://jumpcloud.com/). The email and group provided by your IdP are used for access control in various components.

Next sections will explain how to handle access control in each user-facing Welkin component.

## Container registry (Harbor)

Welkin uses Harbor as container registry. For access control, Harbor defines the concepts of:

- user and group -- for human access;
- robot account -- for IT system access.

You don't need to create Harbor users or groups. Welkin configures Harbor in "OIDC authentication mode", which means that Harbor will automatically onboard users logging in via your IdP and will automatically get the group from your IdP. In contrast, you need to create robot accounts, as these only exist within Harbor.

Your administrator will have configured one of your IdP groups as the "Harbor system administrator" group.
Please read the upstream documentation linked below to learn how a Harbor admin can:

- [manage user permissions by role](https://goharbor.io/docs/2.4.0/administration/managing-users/user-permissions-by-role/) and
- create [robot accounts](https://goharbor.io/docs/2.4.0/administration/robot-accounts/).

!!!note

    You can either add users or groups to a project with various roles. To simplify access control, consider only using groups and assigning users to groups from your IdP.

## Kubernetes API

Kubernetes uses the following concepts for [access control](https://kubernetes.io/docs/reference/access-authn-authz/authentication/):

- users and groups -- these are provided by your IdP;
- [ServiceAccounts](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/) -- these are configured within Kubernetes and are used by IT systems;
- [Roles (and ClusterRoles)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) -- these define a set of permissions, i.e., allowed API operations;
- [RoleBindings (and ClusterRoleBindings)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding) -- these associate Roles, i.e., a set of permissions, with users, groups or ServiceAccounts.

For delegating permissions to ServiceAccounts, follow the example on the [CI/CD page](ci-cd.md#external-cicd).

The next section covers delegation to users and groups.

### Pre-verification

First, make sure you are in the right namespace on the right Cluster:

```bash
kubectl get nodes
kubectl config view --minify --output 'jsonpath={..namespace}'; echo
```

You can only delegate as much permission as you have (see [Privilege escalation prevention](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#privilege-escalation-prevention-and-bootstrapping)). Therefore, check what permissions you have:

```bash
kubectl auth can-i --list
```

### Create a Role

Next, create a Role capturing the set of permissions you want to delegate. If unsure, start from the [example Role](https://github.com/elastisys/welkin/blob/main/user-demo/deploy/ci-cd-role.yaml) that the user demo's CI/CD pipeline needs.

```bash
kubectl apply -f ci-cd-role.yaml
```

### Delegate to a Group

Prefer delegating to a group, so that access control is centralized in your IdP.

```bash
ROLE=my-role     # Role created above
GROUP=my-group   # As set in your IdP

kubectl create rolebinding $ROLE --role $ROLE --group=$GROUP --dry-run=client -o yaml > my-role-binding.yaml
# review my-role-binding.yaml
kubectl apply -f my-role-binding.yaml
```

### Add a Kubernetes admin

In Welkin, Application Developers who are Kubernetes admins have the ability to add more `Kubernetes admins` themselves.

#### Steps

1. Edit the ClusterRoleBinding `extra-user-view` and add the desired users or groups under `subjects`. If unsure, look at an [example subject](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-subjects) from the official Kubernetes documentation.

    ```bash
    kubectl edit clusterrolebinding extra-user-view
    ```

1. In each of your user namespaces that you want the users or groups to be admin in, edit the RoleBinding `extra-workload-admins` and add the desired users or groups under `subjects`. If you have a root HNC namespace and you want the users or groups to be admin in all of **your** namespaces, you only need to edit the RoleBinding in this root namespace and it will propagate.

    ```bash
    kubectl edit rolebinding extra-workload-admins -n user-namespace
    ```

## Application Metrics (Grafana)

Your administrator will have mapped your IdP groups to the Grafana viewer, editor and admin roles.
Access can be limited to specific email domains.
Please read the [upstream documentation](https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/) to learn more.

## Application Logs (OpenSearch Dashboards)

For improved security and due to technical limitations, OpenSearch permissions can only be configured by the Platform Administrator.
Contact them to change access control to application logs.
