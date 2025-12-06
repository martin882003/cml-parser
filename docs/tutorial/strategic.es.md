# 1. DDD Estratégico {#strategic}

El modelado estratégico define cómo se divide el problema y cómo se relacionan las partes.

## Dominios y Subdominios {#domains}

Los dominios agrupan la lógica de negocio. Es fundamental distinguir qué es el núcleo (Core) del negocio y qué es soporte.

```cml
Domain Retail {
  domainVisionStatement = "Una experiencia de compra fluida y moderna"

  Subdomain Core type CORE_DOMAIN {
    domainVisionStatement = "Gestión de pedidos y checkout"
  }
  
  Subdomain Catalog type GENERIC_SUBDOMAIN {
    domainVisionStatement = "Catálogo de productos (comprado o genérico)"
  }
  
  Subdomain Notifications type SUPPORTING_DOMAIN {}
}
```

- **Tipos**: `CORE_DOMAIN`, `SUPPORTING_DOMAIN`, `GENERIC_SUBDOMAIN`.
- `domainVisionStatement`: Describe el propósito del dominio o subdominio.

## Bounded Contexts {#bounded-contexts}

Los Bounded Contexts son los límites donde aplica un modelo específico. Usualmente se vinculan a un Subdominio.

```cml
BoundedContext Checkout implements Core {
  type = SYSTEM
  responsibilities = "Procesar órdenes de compra"
  implementationTechnology = "Python / FastAPI"
  knowledgeLevel = CONCRETE
  
  // Opción avanzada: Modularizar dentro del contexto
  Module Pricing {
    basePackage = "com.retail.pricing"
    // Aquí pueden ir agregados y servicios específicos
  }
}
```

- `implements`: Vincula el contexto a un Subdominio (lo que "realiza").
- Atributos clave: `type` (SYSTEM, FEATURE, TEAM, etc.), `responsibilities`, `implementationTechnology`.

## Context Maps y Relaciones {#context-maps}

Define cómo interactúan los Bounded Contexts.

```cml
ContextMap RetailLandscape {
  type = SYSTEM_LANDSCAPE
  state = TO_BE

  contains Checkout, Catalog, Shipping

  // Relación con patrón específico (Anti-Corruption Layer)
  Checkout [ACL]-> Shipping {
    implementationTechnology = "REST/JSON"
    downstreamRights = VETO_RIGHT
  }

  // Relación simple (Shared Kernel)
  Checkout [SK]<-> Catalog
}
```

**Tipos de Relaciones Soportadas:**

- `[U]->[D]`: Upstream-Downstream genérico.
- `[P]<->[P]`: Partnership (Asociación).
- `[SK]<->[SK]`: Shared Kernel (Núcleo Compartido).
- `[C]<-[S]`: Customer-Supplier (Cliente-Proveedor).
- `[ACL]<-`: Anti-Corruption Layer (Capa Anticorrupción en el lado downstream).
- `[OHS]->`: Open Host Service (Servicio Anfitrión Abierto en el upstream).
- `[PL]->`: Published Language (Lenguaje Publicado).
- `[CF]<-`: Conformist (Conformista).
