# 3. Tactical DDD {#tactical}

Inside a `BoundedContext`, we define the detailed domain model.

## Aggregates and Entities {#aggregates}

```cml
BoundedContext Checkout {
  Aggregate OrderAgg {
    owner "CheckoutTeam"
    
    Entity Order {
      aggregateRoot // Marks the aggregate root
      - OrderId id
      Money totalamount
      OrderStatus status
      
      def void addItem(ProductItem item);
    }
    
    ValueObject OrderId { String value key }
    ValueObject Money { BigDecimal amount String currency }
    
    enum OrderStatus { CREATED, PAID, SHIPPED, CANCELLED }
  }
}
```

- **Syntax**:
    - Types: `String`, `int`, `boolean`, `Date`, etc. or custom types.
    - References: Use `-` before the type (e.g., `- CustomerId customer`).
    - Methods: `def ReturnType methodName(ArgType arg);`

## Services and Repositories {#services}

```cml
BoundedContext Checkout {
  Aggregate OrderAgg {
    // ... entities ...

    Repository OrderRepository {
      @Order save(@Order order);
      @Order findById(@OrderId id);
    }

    Service OrderProcessingService {
      void processPendingOrders();
    }
  }
}
```

- `Repository`: Interface for persistence, usually linked to an Aggregate.
- `Service`: Domain logic that doesn't belong to a specific entity.

## Domain Events {#domain-events}

```cml
DomainEvent OrderPlaced {
  - OrderId orderId
  Date timestamp
}
```
