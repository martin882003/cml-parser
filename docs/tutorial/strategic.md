# 1. Strategic DDD {#strategic}

Strategic modeling defines how the problem is divided and how independent parts relate to each other.

## Domains and Subdomains {#domains}

Domains organize business logic. It is fundamental to distinguish what is Core business and what is support.

```cml
Domain Retail {
  domainVisionStatement = "A seamless and modern shopping experience"

  Subdomain Core type CORE_DOMAIN {
    domainVisionStatement = "Order management and checkout"
  }
  
  Subdomain Catalog type GENERIC_SUBDOMAIN {
    domainVisionStatement = "Product catalog (purchased or generic)"
  }
  
  Subdomain Notifications type SUPPORTING_DOMAIN {}
}
```

- **Types**: `CORE_DOMAIN`, `SUPPORTING_DOMAIN`, `GENERIC_SUBDOMAIN`.
- `domainVisionStatement`: Describes the purpose of the domain or subdomain.

## Bounded Contexts {#bounded-contexts}

Bounded Contexts are the boundaries where a specific model applies. They are usually linked to a Subdomain.

```cml
BoundedContext Checkout implements Core {
  type = SYSTEM
  responsibilities = "Process purchase orders"
  implementationTechnology = "Python / FastAPI"
  knowledgeLevel = CONCRETE
  
  // Advanced option: Modularize within the context
  Module Pricing {
    basePackage = "com.retail.pricing"
    // Aggregates and specific services can go here
  }
}
```

- `implements`: Links the context to a Subdomain (what it "realizes").
- Key attributes: `type` (SYSTEM, FEATURE, TEAM, etc.), `responsibilities`, `implementationTechnology`.

## Context Maps and Relationships {#context-maps}

Defines how Bounded Contexts interact.

```cml
ContextMap RetailLandscape {
  type = SYSTEM_LANDSCAPE
  state = TO_BE

  contains Checkout, Catalog, Shipping

  // Relationship with specific pattern (Anti-Corruption Layer)
  Checkout [ACL]-> Shipping {
    implementationTechnology = "REST/JSON"
    downstreamRights = VETO_RIGHT
  }

  // Simple relationship (Shared Kernel)
  Checkout [SK]<-> Catalog
}
```

**Supported Relationship Types:**

- `[U]->[D]`: Generic Upstream-Downstream.
- `[P]<->[P]`: Partnership.
- `[SK]<->[SK]`: Shared Kernel.
- `[C]<-[S]`: Customer-Supplier.
- `[ACL]<-`: Anti-Corruption Layer (on the downstream side).
- `[OHS]->`: Open Host Service (on the upstream side).
- `[PL]->`: Published Language.
- `[CF]<-`: Conformist.
