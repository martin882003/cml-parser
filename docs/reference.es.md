# Referencia

Recorrido rápido por los tipos principales expuestos por el parser. Todos son dataclasses fáciles de inspeccionar.

## Raíz: `CML`

- `domains: list[Domain]`
- `context_maps: list[ContextMap]`
- `stakeholders, stakeholder_groups`
- `value_registers`
- Helpers: `get_domain`, `get_subdomain`, `get_context_map`, `get_context`, `get_aggregate`, `get_entity`, `get_use_case`

## Análisis de Requerimientos

### `UseCase`
- `name`, `actor`, `interactions`
- `benefit`, `scope`, `level`

### `UserStory`
- `name`, `role`, `feature`, `benefit`

### `Stakeholder`
- `name`, `influence`, `interest`, `priority`, `impact`, `consequences`

### `StakeholderGroup`
- `name`, `stakeholders` (lista de `Stakeholder`)

### `ValueRegister`
- `name`, `context`
- `values` (lista de `Value`)
- `clusters` (lista de `ValueCluster`)

### `Value`
- `name`, `is_core`, `demonstrator`
- `stakeholders` (lista de `Stakeholder`)

### `ValueCluster`
- `name`, `core_value`, `demonstrator`
- `values` (lista de `Value`)

## DDD estratégico

### `Domain`
- `name`, `vision`
- `subdomains` (listas de conveniencia: `core`, `supporting`, `generic`)

### `Subdomain`
- `name`, `type` (`CORE_DOMAIN`, `SUPPORTING_DOMAIN`, `GENERIC_SUBDOMAIN`)
- `vision`, `entities`
- `implementations`: contextos que implementan este subdominio

### `ContextMap`
- `name`, `type`, `state`
- `contexts: list[Context]`
- `relationships: list[Relationship]`
- `get_context(name)`

### `Context`
- `name`, `type`, `vision`, `responsibilities`, `implementation_technology`, `knowledge_level`
- `aggregates`, `services`, `modules`, `implements` (subdominios)
- Helpers: `get_aggregate`, `get_service`, `get_module`, `get_subdomain`

### `Relationship`
- Extremos: `left`, `right` (`Context`)
- `type` (ver enum `RelationshipType`, p.ej. `ACL`, `PL`, `Customer-Supplier`)
- Atributos: `roles`, `implementation_technology`, `downstream_rights`, `exposed_aggregates`

## DDD táctico

### `Aggregate`
- `name`, `owner`
- `entities`, `value_objects`, `domain_events`, `enums`, `services`, `command_events`, `data_transfer_objects`
- Helpers: `get_entity`, `get_value_object`, `get_enum`, `get_service`

### `Entity`
- `name`, `is_aggregate_root`, `attributes`, `operations`, `extends`, `is_abstract`
- Helpers: `get_attribute`, `get_operation`

### `ValueObject`
- `name`, `attributes`, `operations`, `extends`, `is_abstract`

### `DomainEvent`
- `name`, `attributes`, `operations`, `extends`, `persistent`, `is_abstract`

### `Service`
- `name`, `operations`

### `Attribute`
- `name`, `type`
- Flags: `is_reference`, `is_key`
- `visibility` (si está), `collection_type`

### `Operation`
- `name`, `return_type`
- `parameters: list[Parameter]`
- `visibility`, `throws`, `is_abstract`

### `Parameter`
- `name`, `type`, `is_reference`

### `Enum`
- `name`, `values`, `is_aggregate_lifecycle`

## Extensiones de capa de aplicación

- `Application`: `commands`, `flows`, `coordinations`, `services`
- `CommandEvent`, `DataTransferObject`
- `Module`: `name`, `aggregates`, `services`, `domain_objects`
- `Flow` y `FlowStep`: soportan flujos simples de comando/evento.
- `Coordination`: `name`, `steps` (lista de cadenas de coordinación).

Para ejemplos concretos en contexto, mira `test_full_coverage.cml` y `test_tactical_ddd.py`.
