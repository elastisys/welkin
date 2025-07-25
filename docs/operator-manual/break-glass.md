---
tags:
  - HIPAA S45 - Access Control - Emergency Access Procedure - § 164.312(a)(2)(ii)
---

# Break-glass

In this section we describe a workaround when access to the environment is broken for the Platform Administrators/operators and/or users.

## Platform Administrator Access

When Dex or the OpenID provider is malfunctioning, the Platform Administrator might be unable to access the Cluster. The following steps will give you temporary access sufficient for troubleshooting and recovery:

1. `SSH` to one of the control-plane Nodes.

1. Use `/etc/kubernetes/admin.conf` and run `kubectl` commands to check the problem

    ```bash
    export KUBECONFIG=/etc/kubernetes/admin.conf
    #run kubectl command
    sudo kubectl get po -A
    ```

## Kubernetes User Access

> [!NOTE]
> This is a temporary solution and access should be disabled once the issue with Dex is resolved.

If Dex is broken, you can manually create a `kubeconfig` file for a user. While there are different ways to create `kubeconfig` files, we will use the X.509 client certificates with OpenSSL. Follow the steps below to create a user `kubeconfig` file.

1. Create a private key:

    ```sh
    openssl genrsa -out user1.key 2048
    ```

1. Create a certificate signing request (CSR). `CN` is the username and `O` the group.

    ```sh
    openssl req -new -key user1.key \
    -out user1.csr \
    -subj "/CN=user1/O=companyname"
    ```

1. Get the Base64 encoding for the generated CSR file.

    ```sh
    cat user1.csr | base64 | tr -d '\n'
    ```

1. Create a Certificate Signing Request with Kubernetes

    ```sh
    cat <<EOF | kubectl  apply -f -
    apiVersion: certificates.k8s.io/v1
    kind: CertificateSigningRequest
    metadata:
        name: user1
    spec:
        groups:
        - system:authenticated
        request: # put here the Base64 encoded text for the CRS that you get in step 3
        signerName: kubernetes.io/kube-apiserver-client
        usages:
        - client auth
    EOF
    ```

1. Approve the CSR

    ```sh
    kubectl certificate approve user1
    ```

1. Get the certificate.
    Retrieve the certificate from the CSR:

    ```sh
    kubectl get csr/user1 -o yaml
    ```

    The certificate value is in Base64-encoded format under `status.certificate`. Put the content under `client-certificate-data:`. And also get the Base64 encoded content for the private key and put it under `client-key-data:`. To get the Base64 encoded content `cat user1.key | base64 | tr -d '\n'`.

    The kubeconfig file for `user1` user looks like:

    ```yaml
    apiVersion: v1
    clusters:
    - cluster:
        certificate-authority-data: <CA>
        server: https://control-node-ip:6443 # ip address of one of the control nodes
      name: <cluster-name>
    contexts:
    - context:
        cluster: <cluster-name>
        user: user1 # <USER>
      name: <USER>@<CLUSTER-NAME>
    kind: Config
    users:
    - name: user1
      user:
        client-certificate-data: <CLIENT-CRT-DATA>
        client-key-data: <CLIENT-KEY-DATA>
    ```

1. Add the user and namespaces that s/he has access to in wc-config.yaml file.

    ```yaml
    user:
      # This only controls if the namespaces should be created, user RBAC is always created.
      createNamespaces: true
      namespaces:
        - namespace1 # namespaces that the user is allowed to access
      adminUsers:
        - user1 # the user
    ```
