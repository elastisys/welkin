# Getting Started

Setting up Welkin consists of two parts: setting up [at least two vanilla Kubernetes Clusters](../architecture.md#level-2-clusters) and deploying `compliantkubernetes-apps` on top of them.

## Pre-requisites for Creating Vanilla Kubernetes Clusters

In theory, any vanilla Kubernetes Cluster can be used for Welkin. We suggest the [Kubespray](https://github.com/kubernetes-sigs/kubespray) way. To this end, you need:

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Python3 pip](https://packaging.python.org/en/latest/guides/installing-using-linux-tools/)
- [Terraform](https://developer.hashicorp.com/terraform/downloads)
- [Ansible](https://www.ansible.com/)
- [`pwgen`](https://manpages.ubuntu.com/manpages/trusty/man1/pwgen.1.html)

Ansible is best installed as follows:

```shell
git clone --recursive https://github.com/elastisys/compliantkubernetes-kubespray
cd compliantkubernetes-kubespray
pip3 install -r kubespray/requirements.txt
```

Optional: For debugging, you may want CLI tools to interact with your chosen Infrastructure Provider:

- [AWS CLI](https://github.com/aws/aws-cli)
- [Exoscale CLI](https://github.com/exoscale/cli)
- [OpenStack Client](https://pypi.org/project/python-openstackclient/)
- [VMware vSphere CLI (govmomi)](https://github.com/vmware/govmomi)

## Pre-requisites for Welkin Apps

Install pre-requisites for Welkin Apps:

```shell
git clone https://github.com/elastisys/compliantkubernetes-apps
cd compliantkubernetes-apps
./bin/ck8s install-requirements
```

## Misc

Welkin relies on SSH for accessing Nodes. If you haven't already done so, generate an SSH key as follows:

```bash
ssh-keygen
```

Configuration secrets in Welkin are encrypted using [SOPS](https://github.com/getsops/sops).
We currently only support using PGP when encrypting secrets.
If you haven't already done so, generate your own PGP key as follows:

```bash
gpg --full-generate-key
```
