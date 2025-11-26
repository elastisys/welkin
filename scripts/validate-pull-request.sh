#!/usr/bin/env bash

set -euo pipefail
shopt -s extglob

declare -a output

# Raw input stage
declare -a raw
if [[ -f "${1:-}" ]]; then
  readarray -t raw <"${1}"
else
  echo "error: missing or invalid file argument" >&2
  exit 1
fi

# Input stage: remove comments, trailing spaces, and multiple newlines
declare -a input
for line in "${raw[@]}"; do
  # If we're not in a comment
  if [[ -z "${comment:-}" ]]; then
    # If we enter a comment
    if [[ "${line}" =~ (<!--) ]]; then
      # Stage the part of the line before the comment
      stage="${line%%<!--*}"
      line="${line#"${stage}"}"

      comment="true"

    else
      # Stage trimmed line
      stage="${line%%+( )}"

      # Keep if we have staged content
      if [[ -n "${stage}" ]]; then
        input+=("${stage}")
      # Keep if we have input content and last input line had content
      elif [[ -n "${input[*]:-}" ]] && [[ -n "${input[-1]:-}" ]]; then
        input+=("${stage}")
      fi
      # Multiple empty lines will be skipped
    fi
  fi

  # While we're in a comment
  while [[ -n "${comment:-}" ]]; do
    # If we exit a comment
    if [[ "${line}" =~ (-->) ]]; then
      line="${line#*-->}"

      # If we enter a comment
      if [[ "${line}" =~ (<!--) ]]; then
        # Stage the part of the line before the comment
        stage="${stage}${line%%<!--*}"
        line="${line#"${stage}"}"

        comment="true"

      else
        # Stage trimmed line
        stage="${stage}${line}"
        stage="${stage%%+( )}"

        # Keep if we have staged content
        if [[ -n "${stage}" ]]; then
          input+=("${stage}")
        # Keep if we have input content and last input line had content
        elif [[ -n "${input[*]:-}" ]] && [[ -n "${input[-1]:-}" ]]; then
          input+=("${stage}")
        fi
        # Multiple empty lines will be skipped

        comment=""
      fi

    else
      break
    fi
  done
done

for line in "${input[@]}"; do
  if [[ "$line" =~ ^[[:space:]]*-[[:space:]]+\[\ \][[:space:]]*(.*) ]]; then
    unchecked_text=${BASH_REMATCH[1]}
    # Note: Currently, in this repo, all checkboxes are mandatory.
    output+=("a mandatory checkbox is not checked: $unchecked_text")
  fi
done

# Output stage: Custom annotations for GitHub Actions and regular error output otherwise
if [[ -n "${output[*]:-}" ]]; then
  if [[ -n "${GITHUB_ACTIONS:-}" ]]; then
    echo "pull request failed validation:" >>"${GITHUB_STEP_SUMMARY:-}"
    for line in "${output[@]}"; do
      echo "- ${line}" >>"${GITHUB_STEP_SUMMARY:-}"
      echo "::error ::${line}"
    done
  else
    echo "pull request failed validation:" >&2
    for line in "${output[@]}"; do
      echo "- ${line}" >&2
    done
  fi
  exit 1
fi
