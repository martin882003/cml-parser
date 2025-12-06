# 3. DDD Táctico {#tactical}

Dentro de un `BoundedContext`, definimos el modelo de dominio detallado.

## Agregados y Entidades {#aggregates}

```cml
BoundedContext Checkout {
  Aggregate OrderAgg {
    owner "CheckoutTeam"
    
    Entity Order {
      aggregateRoot // Marca la raíz del agregado
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

- **Sintaxis**:
    - Tipos: `String`, `int`, `boolean`, `Date`, etc. o tipos propios.
    - Referencias: Usa `-` antes del tipo (ej: `- CustomerId customer`).
    - Métodos: `def ReturnType methodName(ArgType arg);`

## Servicios y Repositorios {#services}

```cml
BoundedContext Checkout {
  Aggregate OrderAgg {
    // ... entidades ...

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

- `Repository`: Interfaz para persistencia, usualmente ligada a un Agregado.
- `Service`: Lógica de dominio que no pertenece a una entidad específica.

## Eventos de Dominio {#domain-events}

```cml
DomainEvent OrderPlaced {
  - OrderId orderId
  Date timestamp
}
```
