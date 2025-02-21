---
search:
  boost: 2
---

<!--
Note to contributors: Aim for the following format.

* Title: Highlight benefit to Application Developer
* Context
* Problem
* Solution
* Error
* Resolution
-->

# Avoid Cluster autoscaler failing to scale down Nodes due to local storage emptydir usage

!!!important

    This guardrail is enabled by default and will warn on violations, but only on clusters with cluster autoscaling.
    As a result, resources that violate this policy will not be created.

## Problem

The Cluster autoscaler can manage the amount of Nodes in the Cluster by creating or removing Nodes based on resources requested by Pods.
It will scale down Nodes once there is a Node that is not needed anymore.
However, there are [some scenarios](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-types-of-pods-can-prevent-ca-from-removing-a-node) where the autoscaler will not remove certain Nodes.
One such scenario is if there is a Pod running on the Node that is using local storage, since that Pod would lose state if it was moved to a different Node.
In Welkin this is primarily Pods that are using local storage [emptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) volumes.

Since Nodes in Kubernetes often have limited disk space, using empty dir volumes with local storage can also be disruptive for the Node if the Pod is using a larger amount of disk space.
So you should only use emptyDir volumes if you need a small amount of storage.
If you need a moderate or large amount of storage, then consider using [PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) instead.

## Solution

There are a few different solutions to avoid the scenario stated above:

1. Use emptyDir volume with `medium: Memory` instead, the Cluster autoscaler does not consider this as local storage and using this will not prevent the Pod from being evicted by the autoscaler.
    Note that this will instead use the RAM memory of the Node, instead of disk space.
    Also note that this is still ephemeral storage and the data in it will be permanently deleted if the Pod is removed from the Node.
1. Use a permanent form of storage that is not bound to a Node.
    Most likely this would be a PersistentVolume, which can be automatically provisioned by creating a PersistentVolumeClaim and binding that to the Pod.
1. If it is ok that the Pod is deleted by the autoscaler even though it is using local storage.
    Then you can annotate the Pod with `"cluster-autoscaler.kubernetes.io/safe-to-evict-local-volumes": "volume-1,volume-2,.."`, where the value of the annotation is a list that would include the emptyDir volumes.
    Alternatively you can annotate the Pod with `"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"` to note that the Pod is safe to evict in general, this would also allow the autoscaler to delete the Pod even if it is also violating some of the other rules that normally prevent the autoscaler from deleting Pods.

## How Does Welkin Help?

To make sure you don't create Pods that prevent the autoscaler from deleting Nodes, the administrator can configure Welkin to deny creation of Pods that would prevent the autoscaler.

If you get the following error:

```error
Error: UPGRADE FAILED: failed to create resource: admission webhook "validation.gatekeeper.sh" denied the request: [denied by elastisys-reject-local-storage-emptydir] The volume "emptydir-volume" emptyDir is using local storage emptyDir. This can prevent autoscaler from scaling down a node where this is running. Read more about this and possible solutions at <link-to-public-documentation>
```

Then your Pod have an emptyDir volume that would prevent the autoscaler from scaling down a Node.

Note that this is only a problem if the Pod will be scheduled on a Node that is subject to autoscaling.
However, this policy does not know where the Pod would be scheduled, so it will trigger even if the Pod would not be scheduled on an Node subject to autoscaling.
If you are certain that the Pod will not be scheduled on a Node subject to autoscaling, then you can safely add one of the annotations mentioned in the solutions above.

If your administrator has not enforced this policy yet, you can view current violations of the policy by running:

```bash
kubectl get k8srejectemptydir.constraints.gatekeeper.sh elastisys-reject-local-storage-emptydir -ojson | jq .status.violations
```
