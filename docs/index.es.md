# CML Parser

Parsea modelos Context Mapper Language (CML) desde Python usando una gramática ANTLR4 y un modelo de objetos tipado. El parser ofrece modo estricto y modo seguro con diagnósticos sin lanzar excepciones.

## Puntos destacados

- Gramática completa ANTLR4 para CML (DDD estratégico y táctico)
- Modo estricto (`parse_file`) o seguro con diagnósticos (`parse_file_safe`)
- Modelo de objetos rico con helpers para navegar dominios, context maps y agregados
- CLI para validación rápida y resúmenes
- Probado contra los ejemplos oficiales de Context Mapper

## Ejemplo rápido

```python
from cml_parser import parse_file_safe

cml = parse_file_safe("examples/LakesideMutual/ooad-example.cml")
if cml.parse_results.ok:
    print(f"Dominios: {len(cml.domains)}")
    cm = cml.get_context_map("LakesideMutual")
    for ctx in cm.contexts:
        print(f"Contexto: {ctx.name}")
else:
    for err in cml.parse_results.errors:
        print(err.pretty())
```

## ¿Qué es CML?

Context Mapper Language es un DSL para modelar elementos de Domain-Driven Design estratégicos y tácticos (dominios, bounded contexts, context maps, agregados, entidades, servicios y relaciones). Más info en [contextmapper.org](https://contextmapper.org/).

## Instalación

- `pip install cml-parser`
- o `uv pip install cml-parser`
- o clonar e instalar en editable: `pip install -e .`

Revisa el [Comenzar](quickstart.md) para un recorrido completo.
