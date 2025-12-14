import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_value_cluster_relations_and_elicitation(tmp_path):
    content = """
    BoundedContext Demo {}
    Stakeholders of Demo {
      Stakeholder Dev {}
    }
    ValueRegister VR for Demo {
      ValueCluster VC {
        core = "AUTONOMY"
        demonstrator "D1"
        relatedValue = "Speed"
        opposingValue "Cost"

        Stakeholders Dev {
          priority HIGH
          impact MEDIUM
          consequences good "fast" action "optimize" ACT neutral "tradeoff"
        }

        Value V1 {
          demonstrator = "vD"
          relatedValue "Quality"
          opposingValue = "Risk"
          Stakeholder Dev {
            priority = LOW
            consequences
              good "faster delivery"
              action "optimize" ACT
          }
        }
      }
    }
    """
    path = tmp_path / "values_elicitation.cml"
    path.write_text(content, encoding="utf-8")
    model = parse_file_safe(str(path))
    assert model.parse_results.errors == []

    dev = next(s for s in model.stakeholders if s.name == "Dev")

    vr = model.value_registers[0]
    cluster = vr.clusters[0]
    assert cluster.core_value == "AUTONOMY"
    assert cluster.demonstrator == "D1"
    assert cluster.related_values == ["Speed"]
    assert cluster.opposing_values == ["Cost"]

    dev_elic = next(e for e in cluster.elicitations if e.stakeholder == "Dev")
    assert dev_elic.stakeholder_ref is dev
    assert dev_elic.priority == "HIGH"
    assert dev_elic.impact == "MEDIUM"
    assert dev_elic.consequences[0].kind == "good"
    assert dev_elic.consequences[0].consequence == "fast"
    assert dev_elic.consequences[0].action is not None
    assert dev_elic.consequences[0].action.action == "optimize"
    assert dev_elic.consequences[0].action.type == "ACT"
    assert any(c.kind == "neutral" and c.consequence == "tradeoff" for c in dev_elic.consequences)

    v1 = cluster.values[0]
    assert v1.demonstrator == "vD"
    assert v1.related_values == ["Quality"]
    assert v1.opposing_values == ["Risk"]
    assert any(s.name == "Dev" for s in v1.stakeholders)
    v1_elic = v1.elicitations[0]
    assert v1_elic.stakeholder_ref is dev
    assert v1_elic.priority == "LOW"
    assert v1_elic.consequences[0].kind == "good"
    assert v1_elic.consequences[0].action is not None
    assert v1_elic.consequences[0].action.type == "ACT"
