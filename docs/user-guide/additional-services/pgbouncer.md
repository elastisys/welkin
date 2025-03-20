---
search:
  boost: 2
---
# PgBouncer

!!! elastisys "For Elastisys Managed Services Customers"

    Managed PgBouncer is an addition to the Managed PostgreSQL® offering.
    You can request Managed PgBouncer without any additional cost by filing a [service ticket](https://elastisys.atlassian.net/servicedesk/).

## Install Prerequisites

When requesting an installation of Managed PgBouncer, you have the option to decide if PgBouncer will share Nodes with the PostgreSQL Cluster or if it can be scheduled on any worker Node. If PgBouncer shares Nodes with the PostgreSQL Cluster, allocated resources for PostgreSQL will be slightly decreased. PgBouncer does not usually use a lot of resources, compared to PostgreSQL.

## Getting Access

When Managed PgBouncer is installed, the Secret set up by your administrator for your PostgreSQL Cluster is updated with some new information:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: $SECRET
  namespace: $NAMESPACE
stringData:
  # PGHOST represents a cluster-scoped DNS name, which only makes sense inside the Kubernetes cluster.
  # E.g., postgresql1-pgbouncer.postgres-system.svc.cluster.local
  # PGHOST is changed to the DNS name for the PgBouncer service and should be used for all application connections.
  PGHOST: $PGHOST
  # PGBOUNCER_AUTH_FILE represents the name of the auth file Secret which stores database usernames and passwords for PgBouncer.
  PGBOUNCER_AUTH_FILE: $PGBOUNCER_AUTH_FILE
```

> [!IMPORTANT]
> The Secret is very precious! Prefer not to persist any information extracted from it, as shown below.

To extract this information, proceed as follows:

```bash
export SECRET=            # Get this from your administrator
export NAMESPACE=         # Get this from your administrator

export PGHOST=$(kubectl -n $NAMESPACE get secret $SECRET -o 'jsonpath={.data.PGHOST}' | base64 --decode)
export PGBOUNCER_AUTH_FILE=$(kubectl -n $NAMESPACE get secret $SECRET -o 'jsonpath={.data.PGBOUNCER_AUTH_FILE}' | base64 --decode)
```

## Authentication file

The `${PGBOUNCER_AUTH_FILE}` Secret contains the `userlist.txt` file. This file defines which users and passwords are allowed to authenticate, format for this file is described [here](https://www.pgbouncer.org/config.html#authentication-file-format). By default only the provided admin user `${PGUSER}` is allowed to authenticate.

To change the PgBouncer auth file, update the `userlist.txt` file by patching or editing the `${PGBOUNCER_AUTH_FILE}` Secret.

> [!WARNING]
> When changes to the auth file are detected, the PgBouncer Deployment will be automatically restarted to load the new auth file.
> This is disruptive for active connections.

## Configuration

PgBouncer is configured via the `<cluster-name>-pgbouncer-config` ConfigMap, which contains the `pgbouncer.ini` file.

Since PgBouncer configuration can be very specific to the PostgreSQL Cluster needs, the application developer with access to the PostgreSQL Cluster is allowed to change the PgBouncer configuration.

> [!CAUTION]
> The application developer is then responsible for making sure that any changed configuration works. Misconfiguration can lead to loss of service.

To change the PgBouncer configuration, update the `pgbouncer.ini` file by patching or editing the `<cluster-name>-pgbouncer-config` ConfigMap.

> [!WARNING]
> When changes to the configuration are detected, the PgBouncer Deployment will be automatically restarted to load the new configuration.
> This is disruptive for active connections.

Refer to the [upstream documentation](https://www.pgbouncer.org/config.html) for configuration details.

### Default configuration

The default PgBouncer configuration in the Managed PgBouncer offering will work in most cases. The default `max_client_conn` and `default_pool_size` settings are based on the PostgreSQL Cluster size and that the PostgreSQL Cluster has 5 active databases and 2 users per database.

Other noteworthy default configuration:

- `listen_port` is set to `5432`.
- `pool_mode` is set to `transaction`.
- `auth_type` is set to `scram-sha-256`.
- `client_tls_sslmode` is set to `required`. Clients must use TLS. If this is not possible for some reason the settings needs to be changed.
- `server_tls_sslmode` is set to `required`. Communication between PgBouncer and the PostgreSQL Cluster uses TLS.
- `admin_users` is set to the provided admin user `${PGUSER}`.
- `auth_file` should not be changed.
- `pidfile` should not be changed.

## Migration for application developers

Follow these steps if you as an application developer already use the Managed PostgreSQL offering and want to start using Managed PgBouncer.

1. File a service ticket to request installation of Managed PgBouncer.

1. Once PgBouncer is installed, configure the usernames and passwords in the `userlist.txt` file in the `${PGBOUNCER_AUTH_FILE}` Secret.

1. Review PgBouncer configuration in the `<cluster-name>-pgbouncer-config` ConfigMap and update the `pgbouncer.ini` file if necessary. If unsure the default configuration can be used.

1. Update the PostgreSQL hostname to the new `${PGHOST}` value in the application, the new service name that is referred to should contain `-pgbouncer`.
