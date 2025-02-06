---
search:
  boost: 2
---

# Using GPU Workload in Welkin

!!! elastisys "For Elastisys Managed Services Customers"
    You can order a new Environment with GPU support by filing a [service ticket](https://elastisys.atlassian.net/servicedesk/).
    Make sure to specify the need for GPU Nodes in "Additional information or comments".
    If you are unsure, get in touch with your account manager.

As the demand for AI, machine learning, and data science workloads grows, Kubernetes provides a flexible and scalable platform to manage these applications.
In this guide, we'll focus on how to use GPU in the Welkin platform.

> [!NOTE]
> Not all infrastructure providers have support for GPU.
> Check with the platform administrator to find out if your environment has support for GPU workload.

## Deployment

To use GPU resources in your cluster, you need to create a deployment that is using the resource `nvidia.com/gpu`.
Here's an example of how to configure GPU resources for a Pod:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cuda-vectoradd
spec:
  restartPolicy: OnFailure
  containers:
  - name: cuda-vectoradd
    image: "nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda11.7.1-ubuntu20.04"
    resources:
      limits:
        nvidia.com/gpu: 1
```

### Managing Node Types for GPU Workloads

GPU Nodes are essential for certain high-performance workloads, such as machine learning or data processing.
Clusters often host a variety of workloads, some of which require GPU Nodes, while others can run on standard CPU Nodes.
To optimize resource usage and prevent unnecessary costs—since GPU Nodes are significantly more expensive than CPU Nodes—we have introduced multiple Node types with corresponding labels and taints.
This ensures workloads are deployed on appropriate Node types based on their requirements.

#### Node Labels and Taints

To enforce resource-specific scheduling, Nodes have been configured with the following labels and taints:

- **CPU Nodes**:
    - **Label**: `elastisys.io/node-group=worker`
    - **Taint**: None
    - These Nodes serve as the default option for general workloads and require no additional configuration in Pod specifications.

- **GPU Nodes**:
    - **Labels**:
        - `elastisys.io/node-type=gpu`
        - `elastisys.io/node-group=gpu-worker`
    - **Taint**: `elastisys.io/node-type=gpu:NoSchedule`
    - These Nodes are reserved exclusively for workloads requiring GPU resources. To schedule Pods on GPU Nodes, specific **node affinity** and **toleration** must be configured in the Pod definition.

By using these labels and taints, we ensure that:

1. General workloads remain on CPU Nodes by default.
1. Only workloads explicitly configured to use `GPUs` are scheduled on GPU Nodes.

!!! elastisys-self-managed "For Elastisys Self-Managed Customers"

    Elastisys can help you ensure that your GPU Nodes are labeled and tainted as described in this page.
    This prevents workloads from unintentionally consuming GPU resources, thereby avoiding unnecessary expenses.

##### How to Configure GPU Workloads

Application developers who need to deploy workloads on GPU Nodes must include the appropriate affinity and toleration settings in the Pod specification. Below is an example configuration:

```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
            - key: elastisys.io/node-type
              operator: In
              values:
              - gpu
  tolerations:
    - effect: NoSchedule
      key: elastisys.io/node-type
      operator: Equal
      value: gpu
```

This configuration ensures the workload is scheduled only on GPU Nodes.

##### Advanced example Scenario

Let’s imagine you have a workload that specifically requires a GPU flavor called `Standard_B2s`.
You want to ensure this workload is scheduled exclusively on Nodes with this GPU type. Here’s how you can achieve this:

1. Ask your platform administrator, or if you're an Elastisys Managed Service Customer you can file a service ticket [here](https://elastisys.atlassian.net/servicedesk/) and ask to add a new GPU flavor `Standard_B2s` and a label to that GPU Node like `node.kubernetes.io/instance-type=Standard_B2s`
1. Modify the workload manifest file to include the additional label. The updated manifest would look like this:

  ```yaml
  spec:
    affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
              - key: elastisys.io/node-type
                operator: In
                values:
                - gpu
              - key: node.kubernetes.io/instance-type
                operator: In
                values:
                - Standard_B2s
    tolerations:
      - effect: NoSchedule
        key: elastisys.io/node-type
        operator: Equal
        value: gpu
  ```

This configuration ensures that the workload is only scheduled on GPU Nodes labeled with both `elastisys.io/node-type=gpu` and `node.Kubernetes.io/instance-type=Standard_B2s`.

> [!NOTE]
> If your cluster is using the cluster autoscaling feature and there's currently not enough resources, the autoscaler will create one for you.
> It might take a couple of minutes for the new Node to join the cluster and to install all the pre-requisites.

### Further Reading

- [Kubernetes Schedule GPU Documentation](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)
- [Kubernetes Cluster Autoscaler Documentation](https://kubernetes.io/docs/concepts/cluster-administration/cluster-autoscaling/)
- [Cluster Autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)
