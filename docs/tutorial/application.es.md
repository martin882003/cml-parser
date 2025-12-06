# 4. Capa de Aplicación {#application}

Define la API pública del contexto (Application Services), Comandos y Flujos.

## Comandos, Eventos y DTOs

```cml
BoundedContext Checkout {
  Aggregate OrderAgg {
    CommandEvent PlaceOrderCommand { - OrderDTO details }
    DataTransferObject OrderDTO { String productId int quantity }
  }
}
```

## Flujos y Coordinación {#flows}

Modelan procesos de negocio o sagas.

```cml
BoundedContext Checkout {
  Application CheckoutApp {
    
    // Define la orquestación de un flujo
    flow OrderFulfillment {
      command PlaceOrderCommand
      event OrderPlaced
      command BillCustomer
      event PaymentReceived
    }

    // Coordina interacción entre contextos (opcional)
    coordination ShippingCoordination {
      inventoryCheck
      shippingRequest
    }
  }
}
```

---

## Patrón de Archivo Recomendado {#file-pattern}

Un archivo `.cml` puede contener todo, pero es común estructurarlo así:

1.  **Strategic**: Al inicio, Context Maps y definiciones de Dominios.
2.  **Bounded Contexts**: Definiciones vacías o de alto nivel (`BoundedContext A implements X {}`).
3.  **Details**: Luego, bloques detallados para cada Bounded Context (`BoundedContext A { ... }`) con su táctica.

El orden no es estricto, ya que CML resuelve referencias por nombre globalmente dentro del archivo.
