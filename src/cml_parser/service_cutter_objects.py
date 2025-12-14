from dataclasses import dataclass, field
from typing import List


@dataclass
class SCAggregate:
    name: str
    nanoentities: List[str] = field(default_factory=list)


@dataclass
class SCSecurityAccessGroup:
    name: str
    nanoentities: List[str] = field(default_factory=list)


@dataclass
class SCEntity:
    name: str
    nanoentities: List[str] = field(default_factory=list)


@dataclass
class SCPredefinedService:
    name: str
    nanoentities: List[str] = field(default_factory=list)


@dataclass
class SCSeparatedSecurityZone:
    name: str
    nanoentities: List[str] = field(default_factory=list)


@dataclass
class SCSharedOwnerGroup:
    name: str
    nanoentities: List[str] = field(default_factory=list)


@dataclass
class SCCompatibilities:
    raw: str


@dataclass
class ServiceCutterConfig:
    aggregates: List[SCAggregate] = field(default_factory=list)
    security_access_groups: List[SCSecurityAccessGroup] = field(default_factory=list)
    entities: List[SCEntity] = field(default_factory=list)
    predefined_services: List[SCPredefinedService] = field(default_factory=list)
    separated_security_zones: List[SCSeparatedSecurityZone] = field(default_factory=list)
    shared_owner_groups: List[SCSharedOwnerGroup] = field(default_factory=list)
    compatibilities: SCCompatibilities | None = None
    use_cases: List["SCUseCase"] = field(default_factory=list)
    characteristics: List["SCCharacteristic"] = field(default_factory=list)


@dataclass
class SCUseCase:
    name: str
    raw: str
    is_latency_critical: bool = False
    reads: list[str] = field(default_factory=list)
    writes: list[str] = field(default_factory=list)


@dataclass
class SCCharacteristic:
    type: str
    characteristic: str | None
    nanoentities: List[str] = field(default_factory=list)
