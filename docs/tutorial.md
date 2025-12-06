# Learn CML

Context Mapper Language (CML) es un DSL creado por el proyecto [Context Mapper](https://contextmapper.org/) para modelar Domain-Driven Design de punta a punta. Con CML puedes describir:
- La vista estratégica (Context Maps, Bounded Contexts, Dominios/Subdominios y relaciones).
- La vista táctica (Agregados, Entidades, Value Objects, Servicios, Eventos, Enums).
- La capa de aplicación (commands, events, DTOs y flows).

## Pilares de CML

- **Context Maps**: mapean Bounded Contexts y sus relaciones.
- **Dominios y Subdominios**: organizan el modelo estratégico.
- **Bounded Contexts**: delimitan modelos tácticos y su implementación.
- **DDD táctico**: Agregados, Entidades, Value Objects, Services, Domain Events, Enums.
- **Capa de aplicación**: Commands, Events, DTOs y Flows.

## Context Maps y relaciones

```cml
ContextMap PaymentsLandscape {
  type = SYSTEM_LANDSCAPE
  state = AS_IS
  contains Billing, Risk, Ledger

  Billing [ACL]-> Risk {
    implementationTechnology = "REST/JSON"
    downstreamRights = VETO_RIGHT
    exposedAggregates = FraudCheck
  }

  Risk [PL]-> Ledger {
    implementationTechnology = "Kafka"
  }
}
BoundedContext Billing {}
BoundedContext Risk {}
BoundedContext Ledger {}
```

- `type`: SYSTEM_LANDSCAPE o TEAM_MAP.
- `state`: AS_IS o TO_BE.
- Relaciones: flechas (`[ACL]->`) o palabras clave (`Customer-Supplier`, `Partnership`, `Shared-Kernel`, etc.).
- Atributos de relación: `implementationTechnology`, `downstreamRights`, `exposedAggregates`.

## Dominios y Subdominios

```cml
Domain Retail {
  domainVisionStatement = "Great shopping experience"
  Subdomain Core type CORE_DOMAIN { domainVisionStatement = "Checkout" }
  Subdomain Support type SUPPORTING_DOMAIN {}
  Subdomain Catalog type GENERIC_SUBDOMAIN {}
}
```

- Tipos de subdominio: CORE_DOMAIN, SUPPORTING_DOMAIN, GENERIC_SUBDOMAIN.
- Visión opcional en dominio/subdominio.

## Bounded Contexts e implementaciones

```cml
BoundedContext Checkout implements Core {
  type = SYSTEM
  responsibilities = "Process orders"
  implementationTechnology = "Python"
  knowledgeLevel = CONCRETE
}

BoundedContext ProductCatalog implements Catalog {}
```

- `implements` vincula subdominios a contextos.
- Atributos comunes: `type`, `responsibilities`, `implementationTechnology`, `knowledgeLevel`.

## DDD táctico: Agregados y objetos

```cml
BoundedContext Checkout {
  Aggregate OrderAgg {
    owner OrdersTeam

    Entity Order {
      aggregateRoot
      - OrderId id
      Money total
      OrderStatus status
    }

    ValueObject OrderId { String value key }
    ValueObject Money { int amount String currency }

    enum OrderStatus { CREATED, PAID, SHIPPED }

    Service OrderService {
      void createOrder(OrderId id, Money total);
      void markPaid(OrderId id);
    }
  }
}
```

- `aggregateRoot` marca la entidad raíz.
- Prefijo `-` indica referencia.
- `ValueObject` y `enum` modelan tipos de apoyo.
- `Service` agrupa operaciones del dominio táctico.

## Eventos y DTOs

```cml
BoundedContext Checkout {
  Aggregate OrderAgg {
    CommandEvent RegisterOrder {}
    DataTransferObject OrderDTO { String id Money total }
  }
}
```

`CommandEvent` y `DataTransferObject` permiten modelar contratos de mensajes.

## Capa de aplicación (flows y commands)

```cml
BoundedContext Checkout {
  Application CheckoutApp {
    command RegisterOrder using OrderDTO
    flow Fulfillment {
      command RegisterOrder
      event OrderRegistered
    }
  }
}
```

- `Application` declara comandos y flujos.
- `flow` lista pasos tipo `command` o `event`.

## Use Cases y otros elementos

```cml
UseCase PayInvoice {
  actor "Customer"
  benefit "Pay online"
  scope "Checkout"
  level "Summary"
}
```

Útil para documentar actores/beneficios/alcance.

## Patrón de archivo

Un mismo archivo `.cml` puede mezclar ContextMaps, Domains, BoundedContexts y elementos tácticos. El orden no es crítico; las referencias se enlazan por nombre:

- Declara ContextMaps con sus contextos en `contains` o en relaciones.
- Declara Domains/Subdomains para organizar la visión.
- Declara BoundedContexts y sus agregados/táctica.
- Añade Application, UseCase, eventos y DTOs cuando correspondan.

Con estas piezas puedes modelar sistemas completos en CML. Usa los ejemplos de esta guía como base y adapta los atributos según tu escenario.
