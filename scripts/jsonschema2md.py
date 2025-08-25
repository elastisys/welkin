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
import pycurl
import yaml

MISSING = "—"  # Em dash for missing values
BOLD = "\033[1m"  # Terminal bold start
RESET = "\033[0m" # Terminal bold end

def sanitize(value, add_breaks=False):
    """Escape pipes/newlines and insert <wbr> soft-breaks for Markdown."""
    if value is None or not value:
        return MISSING
    if not isinstance(value, str):
        value = str(value)
    value = value.replace("|", "\\|").replace("\n", "<br>")
    if add_breaks:
        value = re.sub(r'([./_-])', r'\1<wbr>', value)
    return value

def make_anchor(path):
    """
    Turns a JSON path into safe anchor to be used in a table cell
    """
    anchor = re.sub(r'[^a-zA-Z0-9_-]+', '-', path).strip('-').lower()
    label = sanitize(path, add_breaks=True)
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
        yield [
            path,
            schema.get("type"),
            schema.get("default"),
            desc
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
    for path, schema_type, default, desc in traverse(schema):
        counters.keys += 1

        if not schema_type:
            counters.missing_type += 1

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
        if desc:
            lines = desc.splitlines()
            if len(desc) > 200 or len(lines) > 3:  # heuristic
                notes[path] = desc
                desc_cell = f'<a id="noteref:{path}" href="#note:{path}">See note</a>'
            else:
                desc_cell = sanitize(desc)
        else:
            counters.missing_desc += 1

        md.append("| " + " | ".join([
            make_anchor(path),
            sanitize(schema_type, add_breaks=True),
            sanitize(default, add_breaks=True),
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
        pycurl.error: If the URL cannot be fetched.
        yaml.YAMLError: If the content cannot be parsed as YAML.
    """
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        # pycurl downloads in < 0.3s, whereas requests takes > 10s
        # Didn't fully understand why.
        buffer = io.BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, path_or_url)
        c.setopt(c.FOLLOWLOCATION, True)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        raw = buffer.getvalue()
    else:
        with open(path_or_url, "rb") as f:
            raw = f.read()

    return yaml.safe_load(raw)

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
    args = parser.parse_args()

    # Apply defaults if no inputs provided
    if not args.inputs:
        args.inputs = [
            "https://raw.githubusercontent.com/elastisys/compliantkubernetes-apps"
            "/refs/heads/main/config/schemas/config.yaml",
            "https://raw.githubusercontent.com/elastisys/compliantkubernetes-apps"
            "/refs/heads/main/config/schemas/secrets.yaml",
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
        except (OSError, yaml.YAMLError, pycurl.error) as e:
            print(f"❌ Failed to process {input_path}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
