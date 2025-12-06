# Usage

Learn how to parse CML and navigate the resulting object model.

## Parsing modes

- **Strict**: `parse_file(path)` or `parse_text(text)` raise `CmlSyntaxError` on the first syntax error.
- **Safe**: `parse_file_safe(path)` returns a `CML` object with `parse_results` containing errors and warnings while still building as much of the model as possible.

```python
from cml_parser import parse_file_safe

cml = parse_file_safe("model.cml")
if cml.parse_results.ok:
    print("Parsed!")
else:
    for err in cml.parse_results.errors:
        print(err.pretty())
```

## Navigating the model

The root object `CML` gives you access to domains, context maps, contexts, and tactical DDD elements:

```python
cm = cml.get_context_map("InsuranceLandscape")
ctx = cm.get_context("PolicyManagement")
agg = ctx.get_aggregate("PolicyAggregate")
entity = agg.get_entity("Policy")
for attr in entity.attributes:
    print(attr.name, attr.type)
```

Common helpers on `CML`:

- `get_context_map(name)`
- `get_context(name)`
- `get_domain(name)` / `get_subdomain(name)`
- `get_aggregate(name)` / `get_entity(name, context_name=None, aggregate_name=None)`
- `get_use_case(name)`

Context maps and relationships:

```python
for rel in cm.relationships:
    print(rel.type, rel.left.name, "->", rel.right.name)
```

## Diagnostics

`ParseResult` is attached to the returned `CML` instance as `parse_results`:

```python
pr = cml.parse_results
print(pr.ok)          # bool
print(pr.errors)      # list[Diagnostic]
print(pr.warnings)    # list[Diagnostic]
print(pr.filename)    # original file path
```

`Diagnostic.pretty()` formats errors with file/line/col when available.

## CLI

Run the parser from the command line:

```bash
python -m cml_parser.parser path/to/model.cml --summary
python -m cml_parser.parser path/to/model.cml --json
```

- Returns exit code `0` on success, `1` on parse errors.
- `--json` is useful for scripting in CI.
