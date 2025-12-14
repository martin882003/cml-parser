import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_value_epic_narrative_weighting_fields(tmp_path):
    content = """
    BoundedContext Demo {}
    Stakeholders of Demo {
      Stakeholder User {}
    }
    ValueRegister VR for Demo {
      ValueEpic VE {
        As a User I value "Speed" as demonstrated in realization of "Fast" reduction of "Slow"
      }
      ValueNarrative VN {
        When the SOI executes "Checkout", stakeholders expect it to promote "Speed", possibly degrading or prohibiting "Cost" with the following externally observable and/or internally auditable behavior: "Logs"
      }
      ValueWeigthing VW {
        In the context of the SOI, stakeholder User values "Speed" more than "Cost" expecting benefits such as "Retention" running the risk of harms such as "Outages"
      }
    }
    """
    path = tmp_path / "values_ext.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    vr = cml.value_registers[0]
    epic = vr.epics[0]
    assert epic.value == "Speed"
    assert epic.realized == ["Fast"]
    assert epic.reduced == ["Slow"]
    narrative = vr.narratives[0]
    assert narrative.feature == "Checkout"
    assert narrative.promoted == "Speed"
    assert narrative.harmed == "Cost"
    assert "Logs" in narrative.behavior
    weight = vr.weightings[0]
    assert weight.stakeholder == "User"
    assert weight.more_than == ("Speed", "Cost")
    assert "Retention" in weight.benefits
    assert "Outages" in weight.harms
