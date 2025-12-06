# Tutorial: CML y el parser

Una guía rápida para entender CML, cómo se escribe y cómo usar el parser para validarlo y recorrerlo.

## ¿Qué es CML?

Context Mapper Language (CML) es un DSL para modelar Domain-Driven Design:
- **DDD estratégico:** Dominios, Subdominios, Bounded Contexts, Context Maps y relaciones (ACL, PL, Customer-Supplier, etc.).
- **DDD táctico:** Agregados, Entidades, Value Objects, Services, Domain Events, Enums y capa de aplicación (commands, events, DTOs, flows).

## Estructura básica de un modelo

```cml
ContextMap Demo {
  contains Billing, Shipping
  Billing [ACL]-> Shipping {
    implementationTechnology = "REST"
  }
}

Domain Commerce {
  Subdomain Core type CORE_DOMAIN {}
  Subdomain Catalogue type SUPPORTING_DOMAIN {}
}

BoundedContext Billing implements Core {}
BoundedContext Shipping implements Catalogue {}
```

- `ContextMap` define contextos y relaciones.
- `BoundedContext` declara un contexto; puede implementar subdominios.
- `Domain` y `Subdomain` organizan la visión estratégica.

## Extender con táctica

```cml
BoundedContext Billing {
  Aggregate InvoiceAgg {
    Entity Invoice {
      aggregateRoot
      - InvoiceId id
      Money total
    }
    ValueObject InvoiceId { String value key }
    ValueObject Money { int amount String currency }
    Service InvoiceService {
      void createInvoice(InvoiceId id, Money total);
    }
  }
}
```

- `Aggregate` agrupa entidades/VOs.
- Prefijo `-` marca referencia; `aggregateRoot` indica raíz.
- `Service` define operaciones.

## Capa de aplicación

```cml
BoundedContext Billing {
  Application BillingApp {
    command RegisterInvoice using InvoiceDTO
    flow BillingFlow {
      command RegisterInvoice
      event InvoiceRegistered
    }
  }
  Aggregate InvoiceAgg {
    CommandEvent RegisterInvoice {}
    DataTransferObject InvoiceDTO { String id int amount }
  }
}
```

## Usar el parser (Python)

Instalá el paquete (`pip install cml-parser`) y parseá en modo seguro:

```python
from cml_parser import parse_file_safe

cml = parse_file_safe("demo.cml")
if not cml.parse_results.ok:
    for err in cml.parse_results.errors:
        print(err.pretty())
else:
    cm = cml.get_context_map("Demo")
    for rel in cm.relationships:
        print(rel.type, rel.left.name, "->", rel.right.name)
```

Recorrer objetos:

```python
ctx = cml.get_context("Billing")
agg = ctx.get_aggregate("InvoiceAgg")
invoice = agg.get_entity("Invoice")
print([ (a.name, a.type, a.is_reference) for a in invoice.attributes ])
```

## Validar desde CLI

```bash
python -m cml_parser.parser demo.cml --summary
# o salida JSON
python -m cml_parser.parser demo.cml --json
```

## Archivos de ejemplo

Usá los modelos en `examples/` del repo o los snippets de [Ejemplos](examples.md) para probar el parser. Incluyen:
- Context Maps y relaciones
- Dominios/Subdominios e implementaciones
- Agregados con entidades/VOs/servicios
- Flujos de aplicación con commands/events/DTOs
