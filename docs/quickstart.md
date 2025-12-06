# Quickstart

Get up and running with the CML parser for both library and CLI usage.

## Install

Using pip:

```bash
pip install cml-parser
```

Using uv (recommended):

```bash
uv pip install cml-parser
```

From source:

```bash
git clone https://github.com/martin882003/cml-parser.git
cd cml-parser
uv sync  # or: python -m venv .venv && source .venv/bin/activate && pip install -e .
```

## Parse a model

```python
from cml_parser import parse_file

model = parse_file("path/to/model.cml")
print(model.context_maps)
```

### Error-tolerant parsing

```python
from cml_parser import parse_file_safe

cml = parse_file_safe("path/to/model.cml")
if not cml.parse_results.ok:
    for err in cml.parse_results.errors:
        print(err.pretty())
```

## CLI validation

You can validate a single file without writing code:

```bash
python -m cml_parser.parser examples/LakesideMutual/ooad-example.cml --summary
```

Flags:

- `--summary`: prints counts of domains and context maps
- `--json`: emits the parse result (diagnostics and metadata) as JSON

Exit codes: `0` on success, `1` when parsing fails.

## Where to go next

- See [Usage](usage.md) for traversal helpers and diagnostics
- See [Reference](reference.md) for the object model overview
