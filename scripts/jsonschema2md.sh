#!/usr/bin/env bash

set -euo pipefail

declare here root target
here="$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"
root="$(dirname "${here}")"
target="${root}/docs/operator-manual/schema"

log.trace() {
  echo -e "trace: ${@}" >&2
}

log.note() {
  if [[ "${GITHUB_ACTIONS:-}" == "true" ]]; then
    echo -e "::notice::${@}"
  else
    echo -e "note: ${@}" >&2
  fi
}

log.error() {
  if [[ "${GITHUB_ACTIONS:-}" == "true" ]]; then
    echo -e "::error::${@}"
  else
    echo -e "error: ${@}" >&2
  fi
  exit 1
}

yq() {
  if command -v yq4 > /dev/null; then
    command yq4 "${@}"
  else
    command yq "${@}"
  fi
}

usage() {
  echo "${0}: Generate documentation for JSON Schema from path or from repositories.

  usage: ${0} [arguments...]
    --path <path> - Collect schemas from the given directory path
        example: ~/repo/elastisys/compliantkubernetes-apps
        note: Mutually exclusive with --repo
    --repo <repo> - Collect schemas from the given repository
        default: elastisys/compliantkubernetes-apps
        note: Mutually exclusive with --path
    --rev <rev> - Collect schemas from the given revision, used with --repo
        default: \${GITHUB_REF_NAME:-main}
        note: If the revision is a release branch it will attempt to find the latest matching release tag

  The script will default to --repo elastisys/compliantkubernetes-apps and --rev \${GITHUB_REF_NAME:-main}.
  Additionally the path or repo must keep the schemas in the config/schema subdirectory.
  "
}

declare mode path_arg repo_arg rev_arg

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --help)
      usage
      exit 0
      ;;
    --path)
      [[ -z "${mode:-}" ]] || log.error "option --${mode} is already set\n\n$(usage)"
      mode="path"
      [[ -n "${2:-}" ]] || log.error "option --path requires a second argument as the path\n\n$(usage)"
      path_arg="${2}"
      shift 2
      ;;
    --repo)
      [[ -z "${mode:-}" ]] || log.error "option --${mode} is already set\n\n$(usage)"
      mode="repo"
      [[ -n "${2:-}" ]] || log.error "option --repo requires a second argument as the repository\n\n$(usage)"
      repo_arg="${2}"
      shift 2
      ;;
    --rev)
      [[ -n "${2:-}" ]] || log.error "option --rev requires a second argument as the revision\n\n$(usage)"
      rev_arg="${2}"
      shift 2
      ;;
    *)
      log.error "unknown argument $1\n\n$(usage)"
      ;;
  esac
done

[[ -d "${target}" ]] || log.error "missing expected ${target} directory"

repo.resolve() {
  local repo="${1}" rev="${2}"

  if [[ "${rev}" =~ release- ]]; then
    revision="$(cut -d- -f2 <<< "${rev}")"

    declare tags
    tags="$(curl -s "https://api.github.com/repos/${repo}/tags")"

    # Resolve the full revision from tags
    revision="$(yq "[.[].name] | sort | reverse | [.[] | select(match(\"${revision}\"))] | .[0]" <<< "${tags}")"

    if [[ "${revision}" == "null" ]]; then
      log.error "unable to resolve full revision for ${rev}"
    fi

  else
    revision="${rev}"
  fi

  commit="$(curl -s "https://api.github.com/repos/${repo}/commits/${revision}")"
  commit_url="$(yq '.html_url' <<< "${commit}")"

  log.note "resolved revision: ${revision}@${commit_url}"
}

repo.collect() {
  local repo="${1}" rev="${2}" temp="${3}"

  curl -sL "https://raw.githubusercontent.com/${repo}/${rev}/config/schemas/config.yaml" -o "${temp}/config.yaml"
  curl -sL "https://raw.githubusercontent.com/${repo}/${rev}/config/schemas/secrets.yaml" -o "${temp}/secrets.yaml"

  if [[ "$(head -n 1 "${temp}/config.yaml")" == "404: Not Found" ]]; then
    log.error "unable to collect config schema: 404 not found"
  fi
  if [[ "$(head -n 1 "${temp}/secrets.yaml")" == "404: Not Found" ]]; then
    log.error "unable to collect secrets schema: 404 not found"
  fi

  log.trace "collected schema from repo"
}

path.collect() {
  local path="${1}"

  [[ -f "${path}/config/schemas/config.yaml" ]] || log.error "unable to collect config schema: file is missing"
  cp "${path}/config/schemas/config.yaml" "${temp}/config.yaml"
  [[ -f "${path}/config/schemas/secrets.yaml" ]] || log.error "unable to collect secrets schema: file is missing"
  cp "${path}/config/schemas/secrets.yaml" "${temp}/secrets.yaml"

  log.trace "collected schema from path"
}

declare commit commit_url generation_time revision staging temp

generation_time="$(date)"
staging="$(mktemp -d)"
temp="$(mktemp -d)"

case "${mode:-"repo"}" in
repo)
  # resolve commit commit_url revision
  repo.resolve "${repo_arg:-"elastisys/compliantkubernetes-apps"}" "${rev_arg:-"${GITHUB_REF_NAME:-"main"}"}"
  # collect ${temp}/config.yaml ${temp}/secrets.yaml from repo
  repo.collect "${repo_arg:-"elastisys/compliantkubernetes-apps"}" "${revision}" "${temp}"
  ;;
path)
  # collect ${temp}/config.yaml ${temp}/secrets.yaml from path
  path.collect "${path_arg}"
  commit="unknown"
  commit_url="unknown"
  revision="local"
  ;;
esac

yq -oj ".\"\$id\" = \"https://raw.githubusercontent.com/elastisys/compliantkubernetes-apps/${revision}/config/schemas/config.yaml\"" < "${temp}/config.yaml" > "${temp}/config.schema.json"
yq -oj ".\"\$id\" = \"https://raw.githubusercontent.com/elastisys/compliantkubernetes-apps/${revision}/config/schemas/secrets.yaml\"" < "${temp}/secrets.yaml" > "${temp}/secrets.schema.json"

log.trace "converted schema"

pushd "${root}" &>/dev/null || log.error "failed to change directory"
npx jsonschema2md -d "${temp}" -f yaml -o "${staging}" -x "${staging}/json"
popd &>/dev/null || log.error "failed to change directory"

log.trace "generated documentation"

# Postfix: Change README to Index
sed -i -r 's/^# README/# Index/' "${staging}/README.md"

# Postfix: Simplify headers
# - Increments the header "Definitions"
# - Increments headers under "Definitions"
# - Changes the header "Definitions group" to the key of the definition
# - Changes the header "Constraints", "Default Value", "Examples", "Type", and "Properties" to bolded text
find "${staging}" -type f -name '*.md' -exec sed -r -i \
  -e 's/^# .+ Definitions/## Definitions/' \
  -e 's/^### (.+)/#### \1/' \
  -e 's/^## Definitions group /### /' \
  -e 's/^#+ .+ Constraints/**CONSTRAINTS**:/' \
  -e 's/^#+ .+ Default Value/**DEFAULTS**:/' \
  -e 's/^#+ .+ Examples/**EXAMPLES**:/' \
  -e 's/^#+ .+ Type/**TYPE**:/' \
  -e 's/^#+ .+ Properties/**PROPERTIES**:/' \
  '{}' '+'

# Postfix: Reference JSON Schemas in Apps repository
find "${staging}" -type f -regextype sed -regex '.*/\(config\|secrets\).*\.md' -exec sed -i -r \
  -e "s#json/config.schema.json#https://github.com/elastisys/compliantkubernetes-apps/blob/${revision}/config/schemas/config.yaml#" \
  -e "s#json/secrets.schema.json#https://github.com/elastisys/compliantkubernetes-apps/blob/${revision}/config/schemas/secrets.yaml#" \
  -e 's#config.schema.json#config/schemas/config.yaml#' \
  -e 's#secrets.schema.json#config/schemas/secrets.yaml#' \
  '{}' '+'

# Postfix: Add return reference (config)
find "${staging}" -type f -regextype sed -regex '.*/\(config-\).*\.md' -exec sed -i -r \
  -e '1 a\\n[Return to the root config schema](config.md)' \
  -e '$ a\\n[Return to the root config schema](config.md)' \
  '{}' '+'

# Postfix: Add return reference (secrets)
find "${staging}" -type f -regextype sed -regex '.*/\(secrets-\).*\.md' -exec sed -i -r \
  -e '1 a\\n[Return to the root secrets schema](secrets.md)' \
  -e '$ a\\n[Return to the root secrets schema](secrets.md)' \
  '{}' '+'

# Postfix: Add under construction alert, commit and date
find "${staging}" -type f -regextype sed -regex '.*\.md' -exec sed -i -r \
  -e '1 a\\n> [!note]\n>\n> This is auto-generated documentation from a JSON schema that is under construction, this will improve over time.' \
  -e "\$ a\\\\n---\\nGenerated ${generation_time} from [elastisys/compliantkubernetes-apps@${revision}](${commit_url})" \
  '{}' '+'

# Postfix: Unescape GFM alerts
find "${staging}" -type f -regextype sed -regex '.*\.md' -exec sed -i -r \
  -e 's/^> \\\[/> \[/' \
  '{}' '+'

# Postfix: Fix numbering of anchors
find "${staging}" -type f -regextype sed -regex '.*\.md' -exec sed -i -r \
  -e 's/\(#([-0-9a-z]+)-([0-9]+)\)/(#\1_\2)/' \
  '{}' '+'

log.trace "postfixed documentation"

cat > "${staging}/undefined.md" <<EOF
# Undefined Schema

> [!warning]
> This is auto-generated documentation from a JSON schema that is under construction, this will improve over time.
>
> The referring type is undefined in the schema.

- [Return to the root config schema](config.md)
- [Return to the root secrets schema](secrets.md)
EOF

log.trace "created undefined"

rm -rf "${target}"
cp -r "${staging}" "${target}"

log.trace "placed documentation"

rm -rf "${staging}"
rm -rf "${temp}"

log.trace "completed"
