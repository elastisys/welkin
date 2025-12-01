#!/bin/env bash

here="$(dirname "$(readlink -f "$0")")"
root="$(readlink -f "${here}/../")"

# Cleanup old template run
if [ -f "${here}/templates/.tmp/network-policies.md" ]; then
  rm "${here}/templates/.tmp/network-policies.md"
fi

gomplate \
  -f "${here}/templates/microsegmentation.md.tmpl" \
  --datasource "state=${here}/templates/.tmp/" \
  --datasource "known_cidrs=${here}/templates/known-cidrs.yaml" \
  -o "${here}/templates/.tmp/network-policies.md"

sed '/^> \[!note\]/,$d' "${root}/docs/operator-manual/microsegmentation.md" | cat - "${here}/templates/.tmp/network-policies.md" > "${here}/templates/.tmp/microsegmentation.md"

mv "${here}/templates/.tmp/microsegmentation.md" "${root}/docs/operator-manual/microsegmentation.md"
