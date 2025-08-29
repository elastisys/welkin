#!/usr/bin/env python3
"""
Convert JSON Schemas into a nice table
"""
import argparse
import io
import os
import re
import sys

from dataclasses import dataclass
import requests
import yaml

MISSING = "—"  # Em dash for missing values
BOLD = "\033[1m"  # Terminal bold start
RESET = "\033[0m" # Terminal bold end

def sanitize(value):
    """Escape pipes/newlines and insert <wbr> soft-breaks for Markdown."""
    if value is None or not value:
        return MISSING
    if not isinstance(value, str):
        value = str(value)
    value = value.replace("|", "\\|").replace("\n", "<br>")
    return value

CODE_REGEX = re.compile("^[^`#]*$")
def render_code(value):
    """Sanitize a value to Markdown code"""
    if value is None or not value:
        return MISSING
    if not isinstance(value, str):
        value = str(value)
    if not CODE_REGEX.fullmatch(value):
        raise ValueError(f'Value {value} does not match expected regex {CODE_REGEX}.')
    return f'`{value}`'

PATH_REGEX = re.compile(r"^[a-zA-Z0-9\[\]/._-]*$")
def render_path(path):
    """
    Turns a JSON path into safe anchor to be used in a table cell
    """
    if path is None or not path:
        raise ValueError('Missing path')
    if not isinstance(path, str):
        path = str(path)

    anchor = re.sub(r'[^a-zA-Z0-9_-]+', '-', path).strip('-').lower()

    if not PATH_REGEX.fullmatch(path):
        raise ValueError(f'Path {path} does not match expected regex {PATH_REGEX}.')

    label = re.sub(r'([./_-])', r'\1<wbr>', path)

    return f'<a id="{anchor}"></a>[{label}](#{anchor})'

@dataclass
class Counters:
    """
    Various counters which should be displayed at the end.
    """
    missing_type: int = 0
    missing_desc: int = 0
    keys: int = 0

def traverse(schema, path=""):
    """
    Traverse a JSON Schema and yield table rows.

    Args:
        schema: The current JSON Schema node.
        path: JSON path of this node (dot/bracket notation).

    Returns:
        A generator returning tubles: key path, type, default and description.
    """
    # JSON Schema allows non-dict nodes (e.g. `true` / `false` for
    # boolean schemas, or scalars in certain contexts like `enum`).
    # These don’t have type/description/default, so we skip them here.
    if not isinstance(schema, dict):
        return

    schema_type = schema.get("type")

    # Add current node
    if path:
        desc = schema.get("description")
        enum = schema.get("enum")
        examples = schema.get("examples")

        # Handle array items
        if schema_type == "array":
            path = f"{path}[]" if path else "[]"

            item_schema = schema.get("items", {})
            item_desc = item_schema.get("description")
            if item_desc:
                desc += f'\n\n{item_desc}'

            item_type = item_schema.get("type")
            if item_type:
                schema_type += f' of {item_type}'

        yield [
            path,
            schema_type,
            schema.get("default"),
            desc,
            enum,
            examples,
        ]

    # Handle object properties (sorted alphabetically)
    if schema_type == "object" and "properties" in schema:
        for key in sorted(schema["properties"].keys()):
            subschema = schema["properties"][key]
            full_path = f"{path}.{key}" if path else key
            yield from traverse(subschema, full_path)

def flush_notes(md, notes):
    """Write out all notes and clear list of notes"""
    for path, text in sorted(notes.items()):
        md.append("\n")
        md.append(f'<h3 id="note:{path}">Notes for <code>{path}</code></h3>')
        md.append(text)
        md.append('\n')
        md.append(f'<a href="#noteref:{path}" title="Jump back to {path}">↩</a>')
        md.append('\n')
    notes.clear()

def schema_to_markdown(schema, source_name):
    """
    Converts a schema into a markdown document. Count missing stuff.
    """
    counters = Counters()
    md = []
    notes = {}

    header = ["Key", "Type", "Default", "Description"]

    # Source attribution
    if source_name.startswith("http://") or source_name.startswith("https://"):
        filename = source_name.split('/')[-1]
        md.append(f"This table was generated from [{filename}]({source_name}).\n")
    else:
        md.append(f"This table was generated from the file `{source_name}`.\n")

    # Legend
    md.append('Cells marked with "—" mean "not specified in schema".\n')

    # Keep track to split the table
    last_section = None

    # Table body
    for path, schema_type, default, desc, enum, examples \
            in traverse(schema):
        counters.keys += 1

        if not schema_type:
            counters.missing_type += 1
            schema_type = MISSING

        section = path.split('.')[0]
        if section != last_section:
            flush_notes(md, notes)

            # Section header
            md.append(f'\n## `{section}`\n')
            md.append(f'{desc}\n') # desc is assumed to be markdown

            # Table header
            md.append("| " + " | ".join(header) + " |")
            md.append("|" + "|".join(["---"] * len(header)) + "|")
            last_section = section

            continue

        desc_cell = MISSING

        # Add enums and examples to description
        if not desc:
            desc = ''
            counters.missing_desc += 1

        if examples:
            desc += '\n\nExamples:\n'
            for e in examples:
                desc += f'\n- {render_code(e)}'
            desc += '\n'
        if enum:
            desc += '\n\nPossible values:\n'
            for e in enum:
                desc += f'\n- {render_code(e)}'
            desc += '\n'

        lines = desc.splitlines()
        if len(desc) > 200 or len(lines) > 3:  # heuristic
            notes[path] = desc
            desc_cell = f'<a id="noteref:{path}" href="#note:{path}">See note</a>'
        else:
            desc_cell = sanitize(desc)

        md.append("| " + " | ".join([
            render_path(path),
            re.sub(r'[^a-zA-Z0-9_ -]+', '-', str(schema_type)),
            render_code(default),
            desc_cell
        ]) + " |")

    flush_notes(md, notes)

    return "\n".join(md), counters

def load_schema(path_or_url):
    """
    Load a JSON Schema (YAML) from a local file or URL.

    Args:
        path_or_url: Path to a schema file on disk, or an HTTP(S) URL.

    Returns:
        A Python object (dict) representing the parsed YAML schema.

    Raises:
        OSError: If the file cannot be read.
        IOError: If the URL cannot be read.
        yaml.YAMLError: If the content cannot be parsed as YAML.
    """
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        resp = requests.get(path_or_url, timeout=10, stream=True)
        resp.raise_for_status()
        content = resp.content
    else:
        with open(path_or_url, "rb") as f:
            content = f.read()

    return yaml.safe_load(content)

def resolve_schema_ref(repo, rev):
    """
    Convert a branch name in the Welkin public docs to a tag name in Welkin Apps.

    Examples:

    - main -> main
    - release-v0.47 -> v0.47.2
    """
    if re.match(r"release-", rev):
        version = rev.split("-", 1)[1]

        # Fetch tags
        tags_url = f"https://api.github.com/repos/{repo}/tags"
        resp = requests.get(tags_url, timeout=10)
        resp.raise_for_status()
        tags = [t["name"] for t in resp.json()]

        # Sort tags reverse (like yq: sort | reverse)
        tags_sorted = sorted(tags, reverse=True)

        # Find the first tag that matches the version
        matches = [t for t in tags_sorted if re.search(version, t)]
        if matches:
            return matches[0]
        raise ValueError(f"unable to resolve full revision for {rev}")

    return rev

def main():
    """Entrypoint (duh!)"""
    parser = argparse.ArgumentParser(
        description="Convert JSON Schema (YAML) to Markdown tables"
    )
    parser.add_argument(
        "inputs", nargs="*",
        help="Schema files or URLs (default: Welkin Apps schemas from GitHub)"
    )
    parser.add_argument(
        "-o", "--output-dir", default="./docs/operator-manual/schema/",
        help="Output folder (default: ./docs/operator-manual/schema/)"
    )
    parser.add_argument(
        "-r", "--rev", default=os.environ.get('GITHUB_REF_NAME', 'main'),
        help=
            "Produce specified documentation version "
            "(default: $GITHUB_REF_NAME or 'main')"
    )
    args = parser.parse_args()

    # Apply defaults if no inputs provided
    if not args.inputs:
        print(f"🔎 Resolving ref… {args.rev}")
        ref = resolve_schema_ref(
            'elastisys/compliantkubernetes-apps', args.rev)
        print(f"🏷️  Resolved {args.rev} → {ref}")
        args.inputs = [
            "https://raw.githubusercontent.com/elastisys/compliantkubernetes-apps"
            f"/{ref}/config/schemas/config.yaml",
            "https://raw.githubusercontent.com/elastisys/compliantkubernetes-apps"
            f"/{ref}/config/schemas/secrets.yaml",
        ]

    os.makedirs(args.output_dir, exist_ok=True)

    for input_path in args.inputs:
        try:
            print(f"📥 Downloading… {input_path}")
            schema = load_schema(input_path)

            print(f"⚙️ Processing… {input_path}")
            source_name = input_path
            markdown, counters = schema_to_markdown(schema, source_name)

            print(
                f"⚠️ Missing type: {BOLD}{counters.missing_type}{RESET}, "
                f"missing description: {BOLD}{counters.missing_desc}{RESET}, "
                f"out of {counters.keys} configuration keys."
            )

            # Pick a name
            base = os.path.basename(input_path)
            if base.endswith((".yaml", ".yml", ".json")):
                base = base.rsplit(".", 1)[0]
            out_path = os.path.join(args.output_dir, f"{base}.md")

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(markdown)

            print(f"✅ Wrote {out_path}")
        except (OSError, IOError, yaml.YAMLError) as e:
            print(f"❌ Failed to process {input_path}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
