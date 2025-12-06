# Examples

Copy–paste friendly snippets. Each shows the CML file, a Python call to the parser, and the expected output.

## Strategic DDD

### Minimal Context Map

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

### Domain + Subdomains

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

### Relationships with attributes

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

**parse:**
```python
from cml_parser import parse_file_safe

cml = parse_file_safe("rels.cml")
cm = cml.get_context_map("Landscape")
rel = cm.relationships[0]
print(rel.type, rel.implementation_technology, rel.downstream_rights, rel.exposed_aggregates)
```

**output:**
```
PL REST/JSON VETO_RIGHT ['PolicyAgg']
```

### Subdomain with Entities

**cml:** `subdomain_entities.cml`
```cml
Domain Marketplace {
  Subdomain Core type CORE_DOMAIN {
    Entity Product { String name }
    Entity Customer { String email }
  }
}
```

**parse:**
```python
from cml_parser import parse_file_safe

cml = parse_file_safe("subdomain_entities.cml")
sd = cml.get_domain("Marketplace").get_subdomain("Core")
print("Entities:", [e.name for e in sd.entities])
```

**output:**
```
Entities: ['Product', 'Customer']
```

## Tactical DDD

### Aggregate with Value Objects and Service

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

## Application Layer

### Flow with commands/events

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

**parse:**
```python
from cml_parser import parse_file_safe

cml = parse_file_safe("appflow.cml")
ctx = cml.get_context("Onboarding")
app = ctx.application
print("Commands:", [c.name for c in app.commands])
flow = app.flows[0]
print("Flow steps:", [(s.type, s.name) for s in flow.steps])
```

**output:**
```
Commands: ['RegisterCustomer']
Flow steps: [('command', 'RegisterCustomer'), ('event', 'CustomerRegistered')]
```

## Requirements Analysis

### Stakeholders and Value Register

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

print(f"Group: {group.name}")
print(f"Stakeholder: {group.stakeholders[0].name}")
print(f"Value: {val_reg.values[0].name} for {val_reg.values[0].stakeholders[0].name}")
```

**output:**
```
Group: Customers
Stakeholder: PremiumUsers
Value: Efficiency for PremiumUsers
```

## CLI validation

Validate any file and get a summary:
```bash
python -m cml_parser.parser minimal.cml --summary
```
