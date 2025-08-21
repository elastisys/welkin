#!/usr/bin/env python3
"""
Convert JSON Schemas into a nice table
"""
import argparse
import io
import os
import sys
import time

import pycurl
import yaml

MISSING = "—"  # Em dash for missing values

def sanitize(value, inline=False):
    """Escape pipes and optionally replace newlines for table cells."""
    if value is None or value == "":
        return MISSING
    if not isinstance(value, str):
        value = str(value)
    value = value.replace("|", "\\|")
    if inline:
        value = value.replace("\n", "<br>")
    return value

def shorten_key(key: str) -> str:
    """Insert <wbr> breakpoints so long keys can wrap in Markdown/HTML."""
    return key.replace(".", ".<wbr>").replace("[]", "[]<wbr>")

def traverse(schema, path="", notes=None):
    rows = []
    if notes is None:
        notes = {}

    if not isinstance(schema, dict):
        return rows, notes

    schema_type = schema.get("type")

    # Handle object properties (sorted alphabetically)
    if schema_type == "object" and "properties" in schema:
        for key in sorted(schema["properties"].keys()):
            subschema = schema["properties"][key]
            full_path = f"{path}.{key}" if path else key
            subrows, notes = traverse(subschema, full_path, notes)
            rows.extend(subrows)

    # Handle array items
    elif schema_type == "array" and "items" in schema:
        full_path = f"{path}[]" if path else "[]"
        subrows, notes = traverse(schema["items"], full_path, notes)
        rows.extend(subrows)

    # Add current node
    if path:
        desc = schema.get("description", "")
        desc_cell = MISSING
        if desc:
            lines = desc.splitlines()
            if len(desc) > 200 or len(lines) > 3:  # heuristic
                note_id = len(notes) + 1
                notes[note_id] = desc
                desc_cell = f"See note [^{note_id}]"
            else:
                desc_cell = sanitize(desc, inline=True)

        rows.append([
            sanitize(shorten_key(path), inline=True),   # Key
            sanitize(schema.get("type", ""), True),     # Type
            sanitize(schema.get("default", ""), True),  # Default
            desc_cell                                   # Description
        ])

    return rows, notes

def format_footnote(idx, text):
    """Format footnotes so MkDocs/GitHub render them properly."""
    lines = text.strip().splitlines()
    if not lines:
        return f"[^{idx}]:"
    out = [f"[^{idx}]: {lines[0]}"]
    for line in lines[1:]:
        out.append("    " + line)  # indent continuation lines
    return "\n".join(out)

def schema_to_markdown(schema, source_name):
    rows = [["Key", "Type", "Default", "Description"]]
    rows_body, notes = traverse(schema)
    rows += rows_body

    # Sort final rows (excluding header) alphabetically by Key
    rows[1:] = sorted(rows[1:], key=lambda r: r[0])

    md = []

    # Source attribution
    if source_name.startswith("http://") or source_name.startswith("https://"):
        md.append(f"This table was generated from [{source_name}]({source_name}).\n")
    else:
        md.append(f"This table was generated from the file `{source_name}`.\n")

    # Table header
    md.append("| " + " | ".join(rows[0]) + " |")
    md.append("|" + "|".join(["---"] * len(rows[0])) + "|")

    # Table body
    for row in rows[1:]:
        md.append("| " + " | ".join(row) + " |")

    # Legend
    md.append("\n*Cells marked with — mean \"not specified in schema\".*")

    # Footnotes
    if notes:
        md.append("\n")
        for idx, text in notes.items():
            md.append(format_footnote(idx, text))

    return "\n".join(md)

def load_schema(path_or_url):
    """Load schema from a local file or a URL."""
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
        return yaml.safe_load(raw)
    else:
        with open(path_or_url, "r") as f:
            return yaml.safe_load(f)

def main():
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
            "https://raw.githubusercontent.com/elastisys/compliantkubernetes-apps/refs/heads/main/config/schemas/config.yaml",
            "https://raw.githubusercontent.com/elastisys/compliantkubernetes-apps/refs/heads/main/config/schemas/secrets.yaml",
        ]

    os.makedirs(args.output_dir, exist_ok=True)

    for input_path in args.inputs:
        try:
            print(f"📥 Downloading… {input_path}")
            schema = load_schema(input_path)

            print(f"⚙️ Processing… {input_path}")
            source_name = input_path
            markdown = schema_to_markdown(schema, source_name)

            # Pick a name
            base = os.path.basename(input_path)
            if base.endswith((".yaml", ".yml", ".json")):
                base = base.rsplit(".", 1)[0]
            out_path = os.path.join(args.output_dir, f"{base}.md")

            with open(out_path, "w") as f:
                f.write(markdown)

            print(f"✅ Wrote {out_path}")
        except Exception as e:
            print(f"❌ Failed to process {input_path}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
