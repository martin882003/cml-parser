from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import List, Optional, Any, Union, Set
import json

class RelationshipType(str, Enum):
    CUSTOMER_SUPPLIER = "Customer-Supplier"
    UPSTREAM_DOWNSTREAM = "Upstream-Downstream"
    DOWNSTREAM_UPSTREAM = "Downstream-Upstream"
    PARTNERSHIP = "Partnership"
    SHARED_KERNEL = "Shared-Kernel"
    ACL = "ACL"
    CF = "CF"
    OHS = "OHS"
    PL = "PL"
    SK = "SK"
    U = "U"
    D = "D"
    S = "S"
    C = "C"
    P = "P"

class SubdomainType(str, Enum):
    CORE = "CORE_DOMAIN"
    SUPPORTING = "SUPPORTING_DOMAIN"
    GENERIC = "GENERIC_SUBDOMAIN"

@dataclass
class Diagnostic:
    message: str
    line: Optional[int] = None
    col: Optional[int] = None
    filename: Optional[str] = None
    expected: Optional[List[str]] = None
    context: Optional[str] = None

    def pretty(self) -> str:
        location = ""
        if self.filename:
            location += f"{self.filename}"
        if self.line is not None:
            location += f":{self.line}"
            if self.col is not None:
                location += f":{self.col}"
        if location:
            location = f"[{location}] "
        expected = f" (expected: {', '.join(self.expected)})" if self.expected else ""
        return f"{location}{self.message}{expected}"

@dataclass
class ParseResult:
    model: Optional[Any]
    errors: List[Diagnostic]
    warnings: List[Diagnostic]
    source: Optional[str] = None
    filename: Optional[str] = None

    @property
    def ok(self) -> bool:
        return not self.errors

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "errors": [asdict(e) for e in self.errors],
            "warnings": [asdict(w) for w in self.warnings],
            "filename": self.filename,
        }

    def __repr__(self):
        status = "OK" if self.ok else "ERROR"
        parts = [status]
        if self.filename:
            parts.append(f"file={Path(self.filename).name}")
        if self.errors:
            parts.append(f"errors={len(self.errors)}")
        if self.warnings:
            parts.append(f"warnings={len(self.warnings)}")
        return f"<ParseResult {' '.join(parts)}>"

@dataclass
class Entity:
    name: str

    def __repr__(self):
        return f"<Entity({self.name})>"

@dataclass
class Subdomain:
    name: str
    type: SubdomainType
    vision: str
    domain: 'Domain' = field(default=None, repr=False) # Avoid recursion in repr
    entities: List[Entity] = field(default_factory=list)
    implementations: List['Context'] = field(default_factory=list, repr=False)

    def get_entity(self, entity_name: str) -> Optional[Entity]:
        return next((e for e in self.entities if e.name == entity_name), None)

    def get_implementation(self, context_name: str) -> Optional['Context']:
        return next((c for c in self.implementations if c.name == context_name), None)

    def __repr__(self):
        return f"<Subdomain({self.name})>"

@dataclass
class Domain:
    name: str
    vision: str
    subdomains: List[Subdomain] = field(default_factory=list)

    @property
    def core(self) -> List[Subdomain]:
        return [s for s in self.subdomains if s.type == SubdomainType.CORE]

    @property
    def supporting(self) -> List[Subdomain]:
        return [s for s in self.subdomains if s.type == SubdomainType.SUPPORTING]

    @property
    def generic(self) -> List[Subdomain]:
        return [s for s in self.subdomains if s.type == SubdomainType.GENERIC]

    def get_subdomain(self, subdomain_name: str) -> Optional[Subdomain]:
        return next((s for s in self.subdomains if s.name == subdomain_name), None)

    def __repr__(self):
        return f"<Domain({self.name})>"

@dataclass
class Aggregate:
    name: str

    def __repr__(self):
        return f"<Aggregate({self.name})>"

@dataclass
class Service:
    name: str

    def __repr__(self):
        return f"<Service({self.name})>"

@dataclass
class Context:
    name: str
    type: str = "FEATURE"
    state: str = "UNDEFINED"
    vision: str = ""
    responsibilities: str = ""
    implementation_technology: str = ""
    knowledge_level: str = ""
    implements: List[Subdomain] = field(default_factory=list)
    context_map: Optional['ContextMap'] = field(default=None, repr=False)
    aggregates: List[Aggregate] = field(default_factory=list)
    services: List[Service] = field(default_factory=list)

    def get_subdomain(self, subdomain_name: str) -> Optional[Subdomain]:
        return next((s for s in self.implements if s.name == subdomain_name), None)

    def get_aggregate(self, aggregate_name: str) -> Optional[Aggregate]:
        return next((a for a in self.aggregates if a.name == aggregate_name), None)

    def get_service(self, service_name: str) -> Optional[Service]:
        return next((s for s in self.services if s.name == service_name), None)

    def __repr__(self):
        return f"<BoundedContext({self.name})>"

@dataclass
class Relationship:
    left: Context
    right: Context
    type: str = "Unknown"
    roles: List[str] = field(default_factory=list)
    raw_model: Optional[Any] = field(default=None, repr=False) # The underlying textX object for detailed inspection if needed

    def __repr__(self):
        return f"<Relationship({self.left.name} -> {self.right.name} [{self.type}])>"

@dataclass
class ContextMap:
    name: str
    type: str
    state: str
    contexts: List[Context] = field(default_factory=list)
    relationships: List[Relationship] = field(default_factory=list)

    def get_context(self, context_name: str) -> Optional[Context]:
        return next((c for c in self.contexts if c.name == context_name), None)

    def get_context_relationships(self, context_name: str) -> List[Relationship]:
        return [
            r for r in self.relationships
            if r.left.name == context_name or r.right.name == context_name
        ]

    def get_relationships_by_type(self, relationship_type: Union[str, RelationshipType]) -> List[Relationship]:
        if isinstance(relationship_type, RelationshipType):
            rtype = relationship_type.value
        else:
            rtype = str(relationship_type)
        
        # Normalize for comparison (simple case-insensitive check)
        rtype = rtype.upper()
        
        results = []
        for r in self.relationships:
            # Check primary type
            if r.type.upper() == rtype:
                results.append(r)
                continue
            
            # Check roles
            if rtype in [role.upper() for role in r.roles]:
                results.append(r)
                continue
                
        return results

    def get_relationship(self, context1: str, context2: str) -> Optional[Relationship]:
        return next(
            (r for r in self.relationships 
             if {r.left.name, r.right.name} == {context1, context2}),
            None
        )

    def __repr__(self):
        return f"<ContextMap({self.name})>"

@dataclass
class UseCase:
    name: str
    # Add other fields

    def __repr__(self):
        return f"<UseCase({self.name})>"

from pathlib import Path

@dataclass
class CML:
    domains: List[Domain] = field(default_factory=list)
    context_maps: List[ContextMap] = field(default_factory=list)
    use_cases: List[UseCase] = field(default_factory=list)
    parse_results: Optional['ParseResult'] = field(default=None, repr=False)

    def get_domain(self, domain_name: str) -> Optional[Domain]:
        return next((d for d in self.domains if d.name == domain_name), None)

    def get_context_map(self, map_name: str) -> Optional[ContextMap]:
        return next((cm for cm in self.context_maps if cm.name == map_name), None)

    def get_use_case(self, use_case_name: str) -> Optional[UseCase]:
        return next((uc for uc in self.use_cases if uc.name == use_case_name), None)

    def __repr__(self):
        filename = self.parse_results.filename if self.parse_results else "unknown"
        
        cm_names = ", ".join(cm.name for cm in self.context_maps)
        d_names = ", ".join(d.name for d in self.domains)
        uc_names = ", ".join(uc.name for uc in self.use_cases)
        
        return (f"<CML file={filename} "
                f"context_maps=[{cm_names}] "
                f"domains=[{d_names}] "
                f"use_cases=[{uc_names}]>")
