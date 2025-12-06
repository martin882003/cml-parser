# 4. Application Layer {#application}

Defines the context's public API (Application Services), Commands, and Flows.

## Commands, Events, and DTOs

```cml
BoundedContext Checkout {
  Aggregate OrderAgg {
    CommandEvent PlaceOrderCommand { - OrderDTO details }
    DataTransferObject OrderDTO { String productId int quantity }
  }
}
```

## Flows and Coordination {#flows}

Model business processes or sagas.

```cml
BoundedContext Checkout {
  Application CheckoutApp {
    
    // Define the orchestration of a flow
    flow OrderFulfillment {
      command PlaceOrderCommand
      event OrderPlaced
      command BillCustomer
      event PaymentReceived
    }

    // Coordinate interaction between contexts (optional)
    coordination ShippingCoordination {
      inventoryCheck
      shippingRequest
    }
  }
}
```

---

## Recommended File Pattern {#file-pattern}

A single `.cml` file can contain everything, but it is common to structure it like this:

1.  **Strategic**: At the beginning, Context Maps and Domain definitions.
2.  **Bounded Contexts**: Empty or high-level definitions (`BoundedContext A implements X {}`).
3.  **Details**: Then, detailed blocks for each Bounded Context (`BoundedContext A { ... }`) with their tactics.

The order is not strict, as CML resolves references by name globally within the file.
