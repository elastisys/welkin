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

## Link <!-- link to relevant ticket or issue where the change was requested, if applicable -->

## Executive Summary <!-- short description of the operation, include keywords that can be easily searchable -->

## Cause <!-- note down the identified cause -->

## Steps <!-- step by step guide on what was executed, add URL to documentation or another adminlog if that was used -->
