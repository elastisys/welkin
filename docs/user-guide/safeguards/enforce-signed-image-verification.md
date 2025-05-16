---
search:
  boost: 2
tags: []
---

# Enforce Signed Image Verification

> [!IMPORTANT]
> This guardrail is disabled by default. Contact your Platform Administrator if you want to enable it.

## Problem

How can you ensure the integrity and authenticity of a container image between building it, storing it in a container registry and deploying a workload to run it?

## Solution

One method to protect against image tampering throughout the pipeline is the use of image signatures and verification.
This method uses a public key signing algorithm to sign container images as close to build time as possible, and enforcing verification of signatures before a container image is run.
Thus an image that has been tampered with will not be run, as it will not have the correct signature.

## How Does Welkin Help?

Your Platform Administrator can configure Welkin to technically enforce verification of container image signatures before they are run.
You provide your administrator with one or more public keys or certificates that will be used for this verification, and you have to sign all your container images with at least one of the corresponding private keys.

## Image Signing

This safeguard supports image signing and verification using [Sigstore Cosign](https://docs.sigstore.dev/cosign/) or [Notary Notation](https://notaryproject.dev/docs/notary-project-overview/).

### Sigstore Cosign

To get started using Cosign to sign your images, you should [install the CLI](https://docs.sigstore.dev/cosign/system_config/installation/).
After you have built and pushed your container image to your container registry, you can then sign it using the CLI:

1. Sign an image:

    ```bash
    cosign sign --key <PRIVATE-KEY> <IMAGE>
    ```

    If you don't already have a key pair, you can generate one with the following command:

    ```bash
    cosign generate-key-pair
    ```

    When signing an image you will be prompted to upload a [transparency log](https://docs.sigstore.dev/logging/overview/) entry.
    If you do not wish to do so, you need to run the following command instead:

    ```bash
    cosign sign --key <PRIVATE-KEY> <IMAGE> --tlog-upload=false
    ```

1. After signing your image, you can verify the signature with:

    ```bash
    cosign verify --key <PUBLIC-KEY> <IMAGE>
    ```

    If you decided to opt out of uploading a transparency log entry, you would need to run the following instead:

    ```bash
    cosign verify --key <PUBLIC-KEY> <IMAGE> --insecure-ignore-tlog
    ```

> [!IMPORTANT]
> You should also inform your Platform Administrator if you are not using the transparency log, so that they can configure the verification policy accordingly.

### Notary Notation

To get started using Notary to sign your images, you should [install the CLI](https://notaryproject.dev/docs/user-guides/installation/cli/).
After you have built and pushed your container image to your container registry, you can then sign it using the CLI:

1. Add an existing certificate with the following command:

    ```bash
    notation cert add --type <TYPE> --store <STORE> <PATH-TO-CERT-FILE>
    ```

    You can also generate a new test certificate with:

    ```bash
    notation cert generate-test <STORE>
    ```

1. Identify the signing `<KEY>` corresponding to your certificate with:

    ```bash
    notation key ls
    ```

1. Sign an image with the following command, using the `<KEY>` from the previous step:

    ```bash
    notation sign --key <KEY> <IMAGE>
    ```

1. Create and import a trust policy, replacing `<TYPE>` and `<STORE>` with what was used in step one:

    ```bash
    cat <<EOF > ./trustpolicy.json
    {
        "version": "1.0",
        "trustPolicies": [
            {
                "name": "my-trust-policy",
                "registryScopes": [ "*" ],
                "signatureVerification": {
                    "level" : "strict"
                },
                "trustStores": [ "<TYPE>:<STORE>" ],
                "trustedIdentities": [
                    "*"
                ]
            }
        ]
    }
    EOF
    ```

1. Import the policy with:

    ```bash
    notation policy import trustpolicy.json
    ```

1. Verify the image with:

    ```bash
    notation verify <IMAGE>
    ```

### Troubleshooting

The following error indicates that you are attempting to deploy a workload with an image that has not been signed.
You should verify that it has been signed correctly.

This error could also indicate that no transparency log has been uploaded when signing the image, but the policy has been configured to check for transparency logs when verifying signatures.
This is configured by your Platform Administrator.

```error
error: failed to create deployment: admission webhook "mutate.kyverno.svc-fail" denied the request:

resource Deployment/namespace/deployment-name was blocked due to the following policies

verify-image-signature:
  autogen-verify-image-signature: 'failed to verify image <IMAGE>:
    .attestors[0].entries[0]: failed to verify <IMAGE>@sha256:xxx:
    no signature is associated with "<IMAGE>@sha256:xxx:",
    make sure the artifact was signed successfully'
```

The following error indicates that you are attempting to deploy a workload with an image that is signed, but not by a trusted signer.
You should verify that the image is signed with the correct signing keys, and that the correct public keys or certificates have been provided to your Platform Administrator.

```error
error: failed to create deployment: admission webhook "mutate.kyverno.svc-fail" denied the request:

resource Deployment/namespace/deployment-name was blocked due to the following policies

verify-image-signature:
  autogen-verify-image-signature: |-
    failed to verify image <IMAGE>: .attestors[0].entries[0]: failed to verify <IMAGE>@sha256:xxx: signature verification failed
    failed to verify signature with digest sha256:xxx, signature is not produced by a trusted signer
```
