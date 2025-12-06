# 2. Requirements Analysis {#requirements}

CML allows capturing requirements and actors before diving into technical design.

## Use Cases and User Stories {#use-cases}

```cml
UseCase PayInvoice {
  actor "Customer"
  benefit "Pay invoices online quickly"
  scope "Checkout System"
  level "Summary"
}

UserStory CreateAccount {
  role "New User"
  feature "create an account"
  benefit "save my preferences"
}
```

## Stakeholders and Value {#stakeholders}

You can model who influences the project and what value they expect.

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
