import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_value_epic_multiple_realization_reduction_clauses(tmp_path):
    content = """
    BoundedContext Demo {}
    Stakeholders of Demo {
      Stakeholder User {}
    }
    ValueRegister VR for Demo {
      ValueEpic VE {
        As a User I value "Speed" as demonstrated in reduction of "Slow" realization of "Fast" realization of "Quality" reduction of "Waste"
      }
    }
    """
    path = tmp_path / "value_epic_multi.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    epic = cml.value_registers[0].epics[0]
    assert epic.name == "VE"
    assert epic.stakeholder == "User"
    assert epic.value == "Speed"
    assert epic.realized == ["Fast", "Quality"]
    assert epic.reduced == ["Slow", "Waste"]

