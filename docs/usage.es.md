# Uso

Cómo parsear CML y navegar el modelo de objetos resultante.

## Modos de parseo

- **Estricto**: `parse_file(path)` o `parse_text(text)` lanzan `CmlSyntaxError` en el primer error de sintaxis.
- **Seguro**: `parse_file_safe(path)` devuelve un objeto `CML` con `parse_results` que incluye errores y warnings, construyendo el modelo hasta donde sea posible.

```python
from cml_parser import parse_file_safe

cml = parse_file_safe("model.cml")
if cml.parse_results.ok:
    print("Parseado!")
else:
    for err in cml.parse_results.errors:
        print(err.pretty())
```

## Navegar el modelo

El objeto raíz `CML` da acceso a dominios, context maps, contextos y elementos tácticos DDD:

```python
cm = cml.get_context_map("InsuranceLandscape")
ctx = cm.get_context("PolicyManagement")
agg = ctx.get_aggregate("PolicyAggregate")
entity = agg.get_entity("Policy")
for attr in entity.attributes:
    print(attr.name, attr.type)
```

Helpers comunes en `CML`:

- `get_context_map(name)`
- `get_context(name)`
- `get_domain(name)` / `get_subdomain(name)`
- `get_aggregate(name)` / `get_entity(name, context_name=None, aggregate_name=None)`
- `get_use_case(name)`

Context maps y relaciones:

```python
for rel in cm.relationships:
    print(rel.type, rel.left.name, "->", rel.right.name)
```

## Diagnósticos

`ParseResult` se adjunta a la instancia `CML` como `parse_results`:

```python
pr = cml.parse_results
print(pr.ok)          # bool
print(pr.errors)      # list[Diagnostic]
print(pr.warnings)    # list[Diagnostic]
print(pr.filename)    # ruta del archivo
```

`Diagnostic.pretty()` formatea errores con archivo/línea/columna cuando están disponibles.

## CLI

Ejecutar el parser desde línea de comandos:

```bash
python -m cml_parser.parser path/to/model.cml --summary
python -m cml_parser.parser path/to/model.cml --json
```

- Retorna código `0` si parsea, `1` ante errores.
- `--json` es útil para scripting en CI.
