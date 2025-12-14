import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_value_narrative_supports_promote_protect_or_create_phrase(tmp_path):
    content = """
    BoundedContext Demo {}
    ValueRegister VR for Demo {
      ValueNarrative VN {
        When the SOI executes "Checkout",
        stakeholders expect it to promote, protect or create "Speed",
        possibly degrading or prohibiting "Cost"
        with the following externally observable and/or internally auditable behavior: "Logs"
      }
    }
    """
    path = tmp_path / "value_narrative_phrase.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    narrative = cml.value_registers[0].narratives[0]
    assert narrative.feature == "Checkout"
    assert narrative.promoted == "Speed"
    assert narrative.harmed == "Cost"
    assert "Logs" in narrative.behavior

