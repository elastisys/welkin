# Release Notes

## Welkin PostgreSQL

<!-- BEGIN TOC -->

- [v1.14.0-ck8s1](#v1140-ck8s1) - 2025-06-25
- [v1.12.2-ck8s2](#v1122-ck8s2) - 2025-04-23
- [v1.12.2-ck8s1](#v1122-ck8s1) - 2024-09-25
- [v1.8.2-ck8s1](#v182-ck8s1) - 2022-08-24
- [v1.7.1-ck8s2](#v171-ck8s2) - 2022-04-26
- [v1.7.1-ck8s1](#v171-ck8s1) - 2021-12-21
<!-- END TOC -->

!!!note

    These are only the user-facing changes.

!!!note

    The public changelog has not been kept up-to-date with development and new releases.
    Expect the naming schema to change and the content of new releases to be more full and descriptive.

### v1.14.0-ck8s1

Released 2025-06-25

Default PostgreSQL versions:

- 17.5
- 16.9
- 15.13
- 14.18
- 13.21

Features:

- PgBouncer is now available as part of the Managed Service. See [this page](../user-guide/additional-services/pgbouncer.md) for more details.
- PostgreSQL version 17 is now available.
- New "developer" role is available, granting users/groups RBAC to port-forward to the PostgreSQL Cluster without having access to the Secret containing admin credentials.

Changes:

- TimescaleDB version bumped to `2.20.3`

### v1.12.2-ck8s2

Released 2025-04-23

Default PostgreSQL versions:

- 16.5
- 15.9
- 14.14
- 13.17

Changes:

- `Spilo` image version bumped to `spilo-16:3.3-p1-24-11-18`

### v1.12.2-ck8s1

Released 2024-09-25

Default PostgreSQL versions:

- 16.4
- 15.8
- 14.13
- 13.16

Changes:

- TimescaleDB version bumped to `2.14.2`
- pgvector version bumped to `0.7.4`

### v1.8.2-ck8s1

Released 2022-08-24

Changes:

- Upgraded postgres-operator to version `v1.8.2`
- Added a service which allows users to port-forward to the service instead of directly to Pods

### v1.7.1-ck8s2

Released 2022-04-26

Changes:

- Fixed a vulnerability with logical backups

### v1.7.1-ck8s1

Released 2021-12-21

First stable release!
