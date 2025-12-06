# Examples

Copy–paste friendly snippets that you can run locally with `python -m cml_parser.parser ...` or from Python code.

## Minimal Context Map

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

**parse:**
```python
from cml_parser import parse_file_safe

cml = parse_file_safe("minimal.cml")
cm = cml.get_context_map("Demo")
for rel in cm.relationships:
    print(rel.type, rel.left.name, "->", rel.right.name, rel.implementation_technology)
```

**output:**
```
ACL Billing -> Shipping REST
```

## Domain + Subdomains

**cml:** `domain.cml`
```cml
Domain Commerce {
  Subdomain Core type CORE_DOMAIN {}
  Subdomain Catalogue type SUPPORTING_DOMAIN {}
}

BoundedContext Store implements Core {}
BoundedContext Catalog implements Catalogue {}
```

**parse:**
```python
from cml_parser import parse_file_safe

cml = parse_file_safe("domain.cml")
dom = cml.get_domain("Commerce")
core = dom.get_subdomain("Core")
print("Core implementations:", [c.name for c in core.implementations])
```

**output:**
```
Core implementations: ['Store']
```

## Tactical Aggregate

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

**parse:**
```python
from cml_parser import parse_file_safe

cml = parse_file_safe("order.cml")
ctx = cml.get_context("Sales")
agg = ctx.get_aggregate("OrderAgg")
order = agg.get_entity("Order")
print("Attributes:", [(a.name, a.type, a.is_reference) for a in order.attributes])
```

**output:**
```
Attributes: [('id', 'OrderId', True), ('total', 'Money', False)]
```

## CLI validation

Validate any file and get a summary:
```bash
python -m cml_parser.parser minimal.cml --summary
```
