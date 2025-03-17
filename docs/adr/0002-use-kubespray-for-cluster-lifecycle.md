# Use Kubespray for Cluster Life-cycle

- Status: accepted
- Deciders: Lars, Johan, Cristian, Emil, Viktor, Geoff, Ewnetu, Fredrik (potentially others who attended the architecture meeting, but I can't remember)
- Date: 2020-11-17

## Context and Problem Statement

Welkin promises: "Multi-cloud. Open source. Compliant". So far, we delivered on our multi-cloud promise by using our in-house `ck8s-cluster` implementation. This strategy feels unsustainable for two reasons: First, we don't have the resources to catch up and keep up with open source projects in the Cluster life-cycle space. Second, we don't want to differentiate on how to set up vanilla Kubernetes Cluster, i.e., lower in the Kubernetes stack. Rather we want to differentiate on services on top of vanilla Kubernetes Clusters.

## Decision Drivers

- We want to differentiate on top of vanilla Kubernetes Cluster.
- We want to be able to run Welkin on top of as many Infrastructure Providers as possible.
- We promise building on top of best-of-breeds open source projects.
- We want to reduce burden with developing and maintaining our in-house tooling for Cluster life-cycle management.

## Considered Options

- [Rancher](https://www.rancher.com/)
- [kubeadm via in-house tools (ck8s-Cluster)](https://github.com/elastisys/ck8s-cluster)
- [Kubespray](https://github.com/kubernetes-sigs/kubespray)
- [kops](https://github.com/kubernetes/kops)

## Decision Outcome

We chose Kubespray, because it is best aligned with our interests, both feature- and roadmap-wise. It has a large community and is expected to be well maintained in the future. It uses kubeadm for domain knowledge on how to set up Kubernetes Clusters.

### Positive Consequences

- We learn how to use a widely-used tool for Cluster lifecycle management.
- We support many Infrastructure Providers.
- We can differentiate on top of vanilla Kubernetes.

### Negative Consequences

- We need training on Kubespray.
- We need to port our tooling and practices to Kubespray.
- We need to port `compliantkubernetes-apps` to work on Kubespray.

## Pros and Cons of the Options

### Rancher

- Good, because it provides Cluster life-cycle management at scale.
- Bad, because it creates Clusters in an opinionated way, which is insufficiently flexible for our needs.
- Bad, because it is not a community project, hence entails long-term licensing uncertainty.

### kubeadm via in-house tool (ck8s-Cluster)

- Good, because we know it and we built it.
- Good, because it works well for current use-cases.
- Bad, because it entails a lot of effort to develop and maintain.
- Bad, because it is lagging behind feature-wise with other Cluster life-cycle solutions.

### kops

- Good, because it integrates well with the underlying Infrastructure Provider (e.g., AWS).
- Bad, because it supports fewer Infrastructure Providers than Kubespray.

NOTE: In the future, we might want to support `compliantkubernetes-apps` on top of both kops and Kubespray, but this does not seem to bring value just now.
