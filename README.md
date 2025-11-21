# CML Parser

[![CI](https://github.com/martin882003/cml_parser/actions/workflows/ci.yml/badge.svg)](https://github.com/martin882003/cml_parser/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/cml-parser.svg)](https://pypi.org/project/cml-parser/)
[![codecov](https://codecov.io/github/martin882003/cml_parser/graph/badge.svg?token=LBFYNPZQE0)](https://codecov.io/github/martin882003/cml_parser)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

# CML Parser

A Python library to parse the Context Mapper Language (CML) using textX. It aims to cover the language defined by the Context Mapper project and is validated against the official sample models.

## Context
CML is the DSL for Context Mapper, a toolkit for strategic/tactical Domain-Driven Design modeling. Reference material and canonical examples are maintained by the Context Mapper team:
- Language docs: https://contextmapper.org/
- Official examples repository: https://github.com/ContextMapper/context-mapper-examples

## Installation

```bash
pip install cml-parser
```

## Usage

```python
from cml_parser import parse_file

model = parse_file("path/to/model.cml")

# On success, model is a textX object graph you can traverse.
print(model)
# If you prefer a non-raising flow:
# from cml_parser import parse_file_safe
# result = parse_file_safe("path/to/model.cml")
# if result.error:
#     print("Parsing failed:", result.error)
```

## Development

```bash
git clone https://github.com/martin882003/cml_parser.git
cd cml_parser
python -m venv venv
source venv/bin/activate
pip install -e .
pytest
```

## License

MIT License — see [LICENSE](LICENSE).

## Contact

- Maintainer: Martin Herran — martin882003@gmail.com

## Contributing
Contributions are welcome! Please:
1. Open an issue describing the change (grammar gaps, bugs, docs).
2. Keep coverage: ensure `pytest` passes and new constructs are represented in `examples/` or new fixtures.
3. Submit a PR with a concise summary of the change.
