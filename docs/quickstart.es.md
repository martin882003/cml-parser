# Comenzar

Arranca rápido con el parser de CML, tanto como librería como desde CLI.

## Instalar

Con pip:

```bash
pip install cml-parser
```

Con uv (recomendado):

```bash
uv pip install cml-parser
```

Desde el código fuente:

```bash
git clone https://github.com/martin882003/cml_parser.git
cd cml_parser
uv sync  # o: python -m venv .venv && source .venv/bin/activate && pip install -e .
```

## Parsear un modelo

```python
from cml_parser import parse_file

model = parse_file("path/to/model.cml")
print(model.context_maps)
```

### Parsing tolerante a errores

```python
from cml_parser import parse_file_safe

cml = parse_file_safe("path/to/model.cml")
if not cml.parse_results.ok:
    for err in cml.parse_results.errors:
        print(err.pretty())
```

## Validar por CLI

Podés validar un archivo sin escribir código:

```bash
python -m cml_parser.parser examples/LakesideMutual/ooad-example.cml --summary
```

Flags:

- `--summary`: imprime conteo de dominios y context maps
- `--json`: emite el resultado de parseo (diagnósticos y metadata) en JSON

Códigos de salida: `0` si parsea ok, `1` si falla.

## Próximos pasos

- Mirá [Uso](usage.md) para helpers y diagnósticos
- Mirá [Referencia](reference.md) para el modelo de objetos
