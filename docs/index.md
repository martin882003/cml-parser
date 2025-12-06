# CML Parser

Parse Context Mapper Language (CML) models from Python using an ANTLR4 grammar and a typed object model. The parser offers strict validation and a safe mode that preserves diagnostics without throwing.

## Highlights

- Full ANTLR4 grammar for CML (strategic and tactical DDD constructs)
- Strict parsing (`parse_file`) or safe parsing with diagnostics (`parse_file_safe`)
- Rich object model with helpers to navigate domains, context maps, and aggregates
- CLI for quick validation and summaries
- Tested against the official Context Mapper examples

## Quick example

```python
from cml_parser import parse_file_safe

cml = parse_file_safe("examples/LakesideMutual/ooad-example.cml")
if cml.parse_results.ok:
    print(f"Domains: {len(cml.domains)}")
    cm = cml.get_context_map("LakesideMutual")
    for ctx in cm.contexts:
        print(f"Context: {ctx.name}")
else:
    for err in cml.parse_results.errors:
        print(err.pretty())
```

## What is CML?

Context Mapper Language is a DSL for modeling strategic and tactical Domain-Driven Design elements (domains, bounded contexts, context maps, aggregates, entities, services, and relationships). Learn more at [contextmapper.org](https://contextmapper.org/).

## Installation

- `pip install cml-parser`
- or `uv pip install cml-parser`
- or clone and install in editable mode: `pip install -e .`

See the [Quickstart](quickstart.md) for a full setup walk-through.
