# 2. Análisis de Requerimientos {#requirements}

CML permite capturar requerimientos y actores antes de entrar en el diseño técnico.

## Casos de Uso e Historias de Usuario {#use-cases}

```cml
UseCase PayInvoice {
  actor "Customer"
  benefit "Pagar facturas online rápidamente"
  scope "Checkout System"
  level "Summary"
}

UserStory CreateAccount {
  role "Nuevo Usuario"
  feature "crear una cuenta"
  benefit "guardar mis preferencias"
}
```

## Stakeholders y Valor {#stakeholders}

Puedes modelar quiénes influyen en el proyecto y qué valor esperan.

```cml
StakeholderGroup Customers {
  Stakeholder PremiumUsers {
    influence = "High"
    interest = "High"
  }
}

ValueRegister RetailValues {
  Value Efficiency {
    stakeholders PremiumUsers
  }
}
```
