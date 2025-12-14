import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_value_register_with_epic_and_weighting(tmp_path):
    content = """
    BoundedContext Demo {}
    Stakeholders of Demo {
      Stakeholder User {}
    }
    ValueRegister VR for Demo {
      ValueEpic VE {
        As a User I value "Speed" as demonstrated in
        realization of "Fast delivery" reduction of "Slow shipping"
      }
      ValueWeigthing VW {
        In the context of the SOI,
        stakeholder User values "Speed" more than "Cost"
        expecting benefits such as "Retention"
        running the risk of harms such as "Outages"
      }
    }
    """
    path = tmp_path / "value_register_ext.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    vr = cml.value_registers[0]
    assert vr is not None
    assert any(epic.name == "VE" for epic in getattr(vr, "epics", []))
    assert any(weight.name == "VW" for weight in getattr(vr, "weightings", []))
