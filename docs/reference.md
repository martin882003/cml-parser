# Reference

A quick tour of the main types exposed by the parser. All objects are plain dataclasses for easy inspection.

## Root: `CML`

- `domains: list[Domain]`
- `context_maps: list[ContextMap]`
- `stakeholders, stakeholder_groups`
- `value_registers`
- Helpers: `get_domain`, `get_subdomain`, `get_context_map`, `get_context`, `get_aggregate`, `get_entity`, `get_use_case`

## Strategic DDD

### `Domain`
- `name`, `vision`
- `subdomains` (with convenience lists: `core`, `supporting`, `generic`)

### `Subdomain`
- `name`, `type` (`CORE_DOMAIN`, `SUPPORTING_DOMAIN`, `GENERIC_SUBDOMAIN`)
- `vision`, `entities`
- `implementations`: contexts that implement this subdomain

### `ContextMap`
- `name`, `type`, `state`
- `contexts: list[Context]`
- `relationships: list[Relationship]`
- `get_context(name)`

### `Context`
- `name`, `type`, `vision`, `responsibilities`, `implementation_technology`, `knowledge_level`
- `aggregates`, `services`, `modules`, `implements` (subdomains)
- Helpers: `get_aggregate`, `get_service`, `get_module`, `get_subdomain`

### `Relationship`
- Endpoints: `left`, `right` (`Context`)
- `type` (see `RelationshipType` enum, e.g., `ACL`, `PL`, `Customer-Supplier`)
- Attributes: `roles`, `implementation_technology`, `downstream_rights`, `exposed_aggregates`

## Tactical DDD

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
- `visibility` (if present), `collection_type`

### `Operation`
- `name`, `return_type`
- `parameters: list[Parameter]`
- `visibility`, `throws`, `is_abstract`

### `Parameter`
- `name`, `type`, `is_reference`

### `Enum`
- `name`, `values`, `is_aggregate_lifecycle`

## Application layer extensions

- `Application`: `commands`, `flows`
- `CommandEvent`, `DataTransferObject`, `Module`
- `Flow` and `FlowStep` support simple command/event flows in the application layer.

For concrete examples of each object in context, see `test_full_coverage.cml` and `test_tactical_ddd.py`.
