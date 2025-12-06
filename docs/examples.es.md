# Ejemplos

Snippets para copiar y pegar; podés correrlos con `python -m cml_parser.parser ...` o desde Python.

## Context Map mínimo

**cml:** `minimal.cml`
```cml
ContextMap Demo {
  contains Billing, Shipping
  Billing [ACL]-> Shipping {
    implementationTechnology = "REST"
  }
}
BoundedContext Billing {}
BoundedContext Shipping {}
```

**parseo:**
```python
from cml_parser import parse_file_safe

cml = parse_file_safe("minimal.cml")
cm = cml.get_context_map("Demo")
for rel in cm.relationships:
    print(rel.type, rel.left.name, "->", rel.right.name, rel.implementation_technology)
```

**salida:**
```
ACL Billing -> Shipping REST
```

## Dominio + Subdominios

**cml:** `domain.cml`
```cml
Domain Commerce {
  Subdomain Core type CORE_DOMAIN {}
  Subdomain Catalogue type SUPPORTING_DOMAIN {}
}

BoundedContext Store implements Core {}
BoundedContext Catalog implements Catalogue {}
```

**parseo:**
```python
from cml_parser import parse_file_safe

cml = parse_file_safe("domain.cml")
dom = cml.get_domain("Commerce")
core = dom.get_subdomain("Core")
print("Implementaciones Core:", [c.name for c in core.implementations])
```

**salida:**
```
Implementaciones Core: ['Store']
```

## Agregado táctico

**cml:** `order.cml`
```cml
ContextMap SalesMap { contains Sales }

BoundedContext Sales {
  Aggregate OrderAgg {
    owner SalesTeam

    Entity Order {
      aggregateRoot
      - OrderId id
      Money total
    }

    ValueObject OrderId { String value key }
    ValueObject Money { int amount String currency }

    Service OrderService {
      void createOrder(OrderId id, Money total);
    }
  }
}
```

**parseo:**
```python
from cml_parser import parse_file_safe

cml = parse_file_safe("order.cml")
ctx = cml.get_context("Sales")
agg = ctx.get_aggregate("OrderAgg")
order = agg.get_entity("Order")
print("Atributos:", [(a.name, a.type, a.is_reference) for a in order.attributes])
```

**salida:**
```
Atributos: [('id', 'OrderId', True), ('total', 'Money', False)]
```

## Validación por CLI

Valida cualquier archivo y obtené un resumen:
```bash
python -m cml_parser.parser minimal.cml --summary
```
