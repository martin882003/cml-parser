import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_text


def test_service_cutter_use_case_reads_writes_any_order():
    content = """
    UseCase UC1 {
      writes "w1", "w2"
      reads "r1" "r2", "r3"
      isLatencyCritical = true
    }
    """
    cml = parse_text(content, strict=True)
    sc = cml.service_cutter
    assert sc is not None
    assert len(sc.use_cases) == 1
    uc = sc.use_cases[0]
    assert uc.name == "UC1"
    assert uc.is_latency_critical is True
    assert uc.reads == ["r1", "r2", "r3"]
    assert uc.writes == ["w1", "w2"]


def test_service_cutter_groups_parse():
    content = """
    Aggregate "Agg" { "n1", "n2" }
    Entity "Ent" { "e1" }
    PredefinedService "Pre" { "p1" }
    SeparatedSecurityZone "Zone" { "z1" }
    SharedOwnerGroup "Group" { "g1" }
    SecurityAccessGroup "Sec" { "s1" }
    """
    cml = parse_text(content, strict=True)
    sc = cml.service_cutter
    assert sc is not None
    assert [a.name for a in sc.aggregates] == ["Agg"]
    assert [e.name for e in sc.entities] == ["Ent"]
    assert [p.name for p in sc.predefined_services] == ["Pre"]
    assert [z.name for z in sc.separated_security_zones] == ["Zone"]
    assert [g.name for g in sc.shared_owner_groups] == ["Group"]
    assert [s.name for s in sc.security_access_groups] == ["Sec"]


def test_service_cutter_rejects_unquoted_group_names():
    content = """
    Aggregate Orders { "n1" }
    """
    cml = parse_text(content, strict=False)
    assert cml.parse_results.errors


def test_service_cutter_rejects_characteristic_outside_compatibilities():
    content = """
    AvailabilityCriticality { characteristic HIGH "n1" }
    """
    cml = parse_text(content, strict=False)
    assert cml.parse_results.errors


def test_service_cutter_rejects_characteristic_without_name():
    content = """
    Compatibilities { AvailabilityCriticality { "n1" } }
    """
    cml = parse_text(content, strict=False)
    assert cml.parse_results.errors


def test_service_cutter_rejects_multiple_compatibilities():
    content = """
    Compatibilities { AvailabilityCriticality { characteristic HIGH "n1" } }
    Compatibilities { AvailabilityCriticality { characteristic LOW "n2" } }
    """
    cml = parse_text(content, strict=False)
    assert cml.parse_results.errors
