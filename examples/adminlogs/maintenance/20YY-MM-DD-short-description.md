# [What] <!-- short title, e.g., added a Node, monthly maintenance -->

## Who: [e.g. GitHub user]

> [!NOTE]
> Record terminal during operation:
>
> ```bash
> # start recording terminal
> script /tmp/script-$(date -I)-short-description.log
> ```
>
> Once done with the operation, stop recording by simply running `exit` in the terminal.
>
> Archive and encrypt logs and store them in the [secret](./secret/) folder.
>
> ```bash
> tar -cz /tmp/script-*.log | sops -e /dev/stdin > $(date --iso-8601)-short-description.tgz.sops
>
> # remove the old terminal output logs
> wipe /tmp/script-*.log
> ```

## Executive Summary <!-- short description of the operation, include keywords that can be easily searchable -->

## Cause <!-- applicable only for issues, if the was identified please note it here -->

## Steps <!-- step by step guide on what was executed, add URL to documentation or another adminlog if that was used -->

## Checklist <!-- Steps that you should perform before and after doing maintenance -->

<!-- The checklist should be adapted to the need of the platform administrators -->

### Before maintenance <!--- Steps done when preparing before a maintenance -->

- [ ] The environment is in a good state
    - [ ] Check the status of Pods and resources
    - [ ] Check the "Kubernetes Cluster status" Grafana dashboard
    - [ ] Check the status of backup jobs (Harbor, OpenSearch, Velero)

### After maintenance <!--- Steps done after a maintenance -->

- [ ] Run the `./bin/ck8s test sc|wc` test scripts
- [ ] Check that all Pods in all namespaces are starting up again
- [ ] Check if any alerts are still open after the maintenance that need to be addressed
