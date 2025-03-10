#!/bin/bash

IMAGE=ubuntu:24.04
CMD=bash

OVERRIDES='''
{
  "apiVersion": "v1",
  "spec": {
     "containers": [{
       "name": "shell",
       "image": "'$IMAGE'",
       "args": ["'$CMD'"],
       "tty": true,
       "stdin": true,
       "securityContext": {
         "runAsUser": 1000
       },
       "resources": {
         "requests": {
            "cpu": "100m",
            "memory": "100M"
         }
       }
    }]
  }
}
'''

kubectl run --rm -ti shell-$USER --overrides="$OVERRIDES" --image=overridden -- overridden
