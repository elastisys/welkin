# Runbooks

> [!NOTE]
> This page describes runbooks for platform administrators.
> As an application developer, you are most likely looking for [Troubleshooting for Application Developers](../user-guide/troubleshooting.md).

!!! elastisys-self-managed
    To get access to the Welkin runbooks, [contact Elastisys](https://elastisys.com/contact/).

Runbooks document step-by-step processes, ensuring that tasks are performed consistently and correctly, reducing errors and reliance on tribal knowledge.
Runbooks are essential for maintaining efficiency, consistency, and reliability in Welkin operations.

Welkin runbooks are searchable and describe what to do:

- when receiving a change request from an application developer;
- how to handle an alert.

The remainder of this page illustrates an example of a Welkin runbook for the ThanosCompactHalted alert.

<!--
    Ignore markdown errors below this line, given that we just included this document verbatimely.
-->
<!-- markdownlint-disable -->

<hr>

# Example: Thanos Compact Halted - PVC

## Alert: ThanosCompactHalted

## Tags

- Thanos
- ThanosCompactHalted
- PVC

## Reason

The [Thanos compactor](https://thanos.io/tip/components/compact.md/) is responsible for downsampling and pushing metrics from its PVC to object storage.

One reason the compactor has halted is that the volume attached to Thanos compactor is full.

## Impact

## Diagnosis

Start investigating if the PVC for the Thanos compactor is full.
This can be easily checked in the Grafana dashboard (Kubernetes/Persistent Volumes).

It is also possible to look at the compactor logs, which should show that there is no space left on the device.

```console
kubectl logs -n thanos deployments/thanos-receiver-compactor | grep halt

ts=2024-07-18T05:53:16.578898999Z caller=compact.go:527 level=error msg="critical error detected; halting" ... 2 errors: preallocate: no space left on device; ..."
```

## Mitigation

To resolve this issue, we need to increase the volume size for the compactor.

Update the sc/mc-config.yaml to increase the PVC for Thanos compactor

```diff
     persistence:
       size: 50Gi
   compactor:
      persistence:
-      size: XGi
+      size: YGi
```

```bash
./bin/ck8s ops helmfile sc -l app=thanos diff
./bin/ck8s ops helmfile sc -l app=thanos apply
```

Wait for a while, then check for halting again.

```bash
kubectl logs -n thanos deployments/thanos-receiver-compactor | grep halt
```
