---
tags:
  - HIPAA S13 - Information Access Management - Access Authorization - § 164.308(a)(4)(ii)(B)
  - HIPAA S14 - Information Access Management - Access Establishment and Modification - § 164.308(a)(4)(ii)(C)
  - HIPAA S43 - Access Control - § 164.312(a)(1)
  - HIPAA S44 - Access Control - Unique User Identification - § 164.312(a)(2)(i)
  - MSBFS 2020:7 4 kap. 3 §
  - MSBFS 2020:7 4 kap. 4 §
  - HSLF-FS 2016:40 4 kap. 3 § Styrning av behörigheter
  - NIS2 Minimum Requirement (i) Access Control
  - ISO 27001 Annex A 5.15 Access Control
---

# Access control

## Group claims

This guide describes how to set up and make use of group claims for applications.

!!!note

    This guide assumes your group claim name is `groups`.

### Kubernetes

To set up [kubelogin](https://github.com/int128/kubelogin) to fetch and use groups make sure that your kubeconfig looks something like this.

```yaml
users:
  - name: user@my-cluster
    user:
      exec:
        apiVersion: client.authentication.k8s.io/v1beta1
        args:
          - oidc-login
          - get-token
          - --oidc-issuer-url=https://dex.my-cluster-domain.com
          - --oidc-client-id=my-client-id
          - --oidc-client-secret=my-client-secret
          - --oidc-extra-scope=email,groups # Make sure groups are here
        command: kubectl
```

!!!tips

    Your token can be found in `~/.kube/cache/oidc-login/`.
    This is useful if you're trying to debug your claims since you can just paste the token to [jwt.io](https://jwt.io) and check it.

    Example:

    ```console
    $ ls ~/.kube/cache/oidc-login/

    $ kubectl get pod
    <log in>

    $ ls ~/.kube/cache/oidc-login/
    13b165965d8e80749ce3b8d442da3e4e9f5ff5e38900ef104eee99fde85a39d4

    $ cat ~/.kube/cache/oidc-login/13b165965d8e80749ce3b8d442da3e4e9f5ff5e38900ef104eee99fde85a39d4 | jq -r .id_token
    eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2RleC5teS1jbHVzdGVyLWRvbWFpbi5jb20iLCJpYXQiOjE2MjE1MTUxNzcsImV4cCI6MTY1MzEzNzU3NywiYXVkIjoibXktY2xpZW50LWlkIiwic3ViIjoiSGlVUE92S1BKMmVwWUkwR1R1U0JYWGRxYTJTV2ZxRnc1ZjBXNVBQeThTWSIsIm5vdW5jZSI6IkNoVXhNRFk0TVRZNE1qRXpORFUzTURVM01ERXlNREFTQm1kdmIyZHNaUSIsImF0X2hhc2giOiI1aUZjbF9Sc1JvblhHekZaMU0xQ2JnIiwiZW1haWwiOiJ1c2VyQG15LWRvbWFpbi5jb20iLCJlbWFpbF92ZXJpZmllZCI6InRydWUiLCJncm91cHMiOlsibXktZ3JvdXAtb25lIiwibXktZ3JvdXAtdHdvIl19.s65Aowfn6B1PiyQvRGPRu9KgX7G39nkLtx6yCAEElao
    ```

    Copy the token to [jwt.io](https://jwt.io) and ensure that the payload includes the expected groups claim.

### OpenSearch

To enable OpenSearch to use the groups for OpenSearch Dashboards access.

```yaml
opensearch:
  sso:
    scope: "... groups" # Add groups to existing
  extraRoleMappings:
    - mapping_name: kibana_user
      definition:
        backend_roles:
          - my-group-name
    - mapping_name: kubernetes_log_reader
      definition:
        backend_roles:
          - my-group-name
```

### Harbor

Set correct group claim name since the default scopes includes groups already.
This groups can be assigned to projects or as admin group.

```yaml
harbor:
  oidc:
    groupClaimName: groups
```

!!!note

    When OIDC (e.g. DeX) is enabled we cannot create static users using the Harbor web interface. But when anyone logs in via DeX they automatically get a user and we can promote that user to admin.
    Once there is one admin, they can set specific permissions for other users (there should be at least a few users promoted to admins).

### Grafana

#### OPS Grafana

```yaml
grafana:
  ops:
    oidc:
      enabled: true
      userGroups:
        grafanaAdmin: my-admin-group
        grafanaEditor: my-editor-group
        grafanaViewer: my-viewer-group
      scopes: ".... groups" # Add groups to existing
      allowedDomains:
        - my-domain.com
```

#### User Grafana

```yaml
grafana:
  user:
    oidc:
      userGroups:
        grafanaAdmin: my-admin-group
        grafanaEditor: my-editor-group
        grafanaViewer: my-viewer-group
      scopes: "... groups" # Add groups to existing
      allowedDomains:
        - my-domain.com
```

## Users onboarding

This describes how to configure Welkin with the Application Developers who should be OpenSearch, Grafana or Harbor Administrators.

### OpenSearch

This is configured via `sc-config.yaml`

```yaml
opensearch:
  extraRoleMappings:
    # Application developer access
    - mapping_name: kibana_user
      definition:
        users:
          - user@domain.tld
    # Extra permissions for Application developer
    - mapping_name: kubernetes_log_reader
      definition:
        users:
          - user@domain.tld
    - mapping_name: alerting_ack_alerts
      definition:
        users:
          - user@domain.tld
    - mapping_name: alerting_read_access
      definition:
        users:
          - user@domain.tld
    - mapping_name: alerting_full_access
      definition:
        users:
          - user@domain.tld
    # Administrator access
    - mapping_name: all_access
      definition:
        users:
          - user@domain.tld
        backend_roles:
          - group@domain.tld
```

### Grafana

1. Application Developer logs in to Grafana via OpenID

1. Administrator logs in to Grafana via static admin user.

    !!!note

        To get the static admin username and password you need to have access to the SC cluster and then run

        `kubectl get secret user-grafana-env -n monitoring -o json | jq '.data | map_values(@base64d)'`

1. Administrator promotes the OpenID user to Grafana admin at `grafana.domain.tld/admin/users`

### Harbor

1. Application Developer logs in to Harbor via OpenID

1. Administrator logs in to Harbor via static admin user.

    !!!note

        To get the static admin username and password you need to have access to the SC cluster and then run

        `kubectl get secret harbor-init-secret -n harbor -o json | jq '.data."harbor-password" | @base64d'`

        Username is: admin

1. Administrator promotes the OpenID user to Harbor admin at `harbor.domain.tld/harbor/users`

## OpenSearch Index Per Namespace

This section defines how to enable indices for Kubernetes namespaces.

To enable logging and control indices per namespace in OpenSearch, this is configured in `common-config.yaml` as follows:

```yaml
opensearch:
  indexPerNamespace: true
```

### Defining Access Control Per Index

This section describes how to define access control for specific indices in OpenSearch.

This is configured via `sc-config.yaml`

```yaml
opensearch:
  extraRoles:
    - role_name: namespace1_reader
      definition:
        index_permissions:
          - index_patterns:
              - "namespace1-*"
            allowed_actions:
              - read
    - role_name: namespace2_reader
      definition:
        index_permissions:
          - index_patterns:
              - "namespace2-*"
            allowed_actions:
              - read
  extraRoleMappings:
    - mapping_name: kibana_user # needed to be able to view index patterns
      definition:
        users:
          - user1@domain.tld
          - user2@domain.tld
    - mapping_name: namespace1_reader
      definition:
        users:
          - user1@domain.tld
        backend_roles: []
    - mapping_name: namespace2_reader
      definition:
        users:
          - user2@domain.tld
        backend_roles: []
# we also need to configure retention period in curator to delete the indices
  curator:
    retention:
      - pattern: ^[^.].*
        sizeGB: 5000
        ageDays: 30
```

Do note that the configured users needs to create the index patterns manually in OpenSearch Dashboards under `Dashboards Management` -> `Index patterns` -> `Create index pattern`:

![OpenSearch create index pattern](../img/opensearch-create-index-pattern.png)

## OpenSearch Document-level security

This section describes how to configure [Document-level security](https://opensearch.org/docs/latest/security/access-control/document-level-security/) in order to restrict access to a subset of documents within an index. This makes it possible to limit access to certain logs of an application based on the contents of fields.

The following example describes a role that will not be able to display documents where the field `level=audit` or where `message` contains `level=audit`

```yaml
opensearch:
  extraRoles:
   - role_name: kubernetes-without-audit
      definition:
        index_permissions:
          - index_patterns:
              - "kubernetes*"
            allowed_actions:
              - read
            dls: |-
              {
                "bool": {
                  "must_not": [
                    {
                      "match_phrase": {
                        "message": "level=audit"
                      }
                    },
                    {
                      "match_phrase": {
                        "level": "audit"
                      }
                    }
                  ]
                }
              }
  extraRoleMappings:
    - mapping_name: kubernetes-without-audit
      definition:
        users:
          - less-privileged-user@domain.tld
    - mapping_name: kibana_user # needed to be able to view index patterns
      definition:
        users:
          - less-privileged-user@domain.tld

```
