---
description: Learn how to debug your application pod on Welkin, the Kubernetes platform for software critical to our society
search:
  boost: 2
---

# Step 4: Debug

Welcome to the fourth and final step, Application Developer!

Sometimes, your application might be end up with issue - for instance, it might be stuck, fail silently. In such cases, you may want to debug the Pod.

## Attach a Debug Container

Welkin supports Kubernetes `kubectl debug` command, which allows you to temporarily attach an **ephemeral container** to a running Pod for troubleshooting purposes. This container can share the Pod’s process and network space and can include useful tools not available in the original container image.

!!!note
   
    Welkin enforces security guardrails:

    - The image must come from an [allowed registry](safeguards/enforce-trusted-registries.md)
    - The container must run as a **non-root user**
    - Privilege escalation is not allowed

### Example Usage

```bash
kubectl debug -n staging my-app-6c9f75f457-abcde \
  --image=harbor.com/tools/nonroot-debug:latest \
  --target=my-app \
  --share-processes \
  --tty --stdin
```

## Next step? Going deeper!

By now, you're fully up and running! You have an application. The next step is to open the "Go Deeper" section of this documentation and read up on more topics that interest you.

Thank you for starting your journey beyond the clouds with Welkin!
