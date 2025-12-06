# Ejemplos

Snippets para copiar y pegar; podés correrlos con `python -m cml_parser.parser ...` o desde Python.

## DDD estratégico

### Context Map mínimo

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

### Dominio + Subdominios

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

### Relaciones con atributos y agregados expuestos

**cml:** `rels.cml`
```cml
ContextMap Landscape {
  contains Billing, Policy

  Billing [PL]-> Policy {
    implementationTechnology = "REST/JSON"
    downstreamRights = VETO_RIGHT
    exposedAggregates = PolicyAgg
  }
}

BoundedContext Billing {}
BoundedContext Policy {
  Aggregate PolicyAgg {}
}
```

**parseo:**
```python
from cml_parser import parse_file_safe

cml = parse_file_safe("rels.cml")
cm = cml.get_context_map("Landscape")
rel = cm.relationships[0]
print(rel.type, rel.implementation_technology, rel.downstream_rights, rel.exposed_aggregates)
```

**salida:**
```
PL REST/JSON VETO_RIGHT ['PolicyAgg']
```

### Dominio con entidades dentro del subdominio

**cml:** `subdomain_entities.cml`
```cml
Domain Marketplace {
  Subdomain Core type CORE_DOMAIN {
    Entity Product { String name }
    Entity Customer { String email }
  }
}
```

**parseo:**
```python
from cml_parser import parse_file_safe

cml = parse_file_safe("subdomain_entities.cml")
sd = cml.get_domain("Marketplace").get_subdomain("Core")
print("Entidades:", [e.name for e in sd.entities])
```

**salida:**
```
Entidades: ['Product', 'Customer']
```

## DDD táctico

### Agregado táctico

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

## Análisis de Requerimientos

### Stakeholders y Registro de Valor

**cml:** `requirements.cml`
```cml
StakeholderGroup Customers {
  Stakeholder PremiumUsers {
    influence = "Medium"
    interest = "High"
  }
}

ValueRegister RetailValues {
  Value Efficiency {
    stakeholders PremiumUsers
  }
}
```

**parse:**
```python
from cml_parser import parse_file_safe

cml = parse_file_safe("requirements.cml")
group = cml.stakeholder_groups[0]
val_reg = cml.value_registers[0]

print(f"Grupo: {group.name}")
print(f"Stakeholder: {group.stakeholders[0].name}")
print(f"Valor: {val_reg.values[0].name} para {val_reg.values[0].stakeholders[0].name}")
```

**output:**
```
Grupo: Customers
Stakeholder: PremiumUsers
Valor: Efficiency para PremiumUsers
```

## Validación por CLI

Valida cualquier archivo y obtené un resumen:
```bash
python -m cml_parser.parser minimal.cml --summary
```

## Capa de aplicación

### Flujo con comandos/eventos

**cml:** `appflow.cml`
```cml
ContextMap AppFlowMap { contains Onboarding }

BoundedContext Onboarding {
  Aggregate CustomerAgg {
    Entity Customer { aggregateRoot String name }
    CommandEvent RegisterCustomer {}
    DataTransferObject CustomerDTO { String name }
  }

  Application OnboardingApp {
    command RegisterCustomer using CustomerDTO
    flow Onboard {
      command RegisterCustomer
      event CustomerRegistered
    }
  }
}
```

**parseo:**
```python
from cml_parser import parse_file_safe

cml = parse_file_safe("appflow.cml")
ctx = cml.get_context("Onboarding")
app = ctx.application
print("Comandos:", [c.name for c in app.commands])
flow = app.flows[0]
print("Pasos:", [(s.type, s.name) for s in flow.steps])
```

**salida:**
```
Comandos: ['RegisterCustomer']
Pasos: [('command', 'RegisterCustomer'), ('event', 'CustomerRegistered')]
```
