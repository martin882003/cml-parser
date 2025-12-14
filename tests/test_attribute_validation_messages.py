import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_attribute_extended_validations(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Identity {
        Entity User {
          String card creditCardNumber = "invalid card";
          String nick length = "3..10" range = "1..2" scriptAssert = "script" url = "http://example.com";
          String ok assertTrue = "must be true" assertFalse = "must be false";
        }
      }
    }
    """
    path = tmp_path / "attr_validation_msgs.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    user = cml.get_context("Demo").get_aggregate("Identity").get_entity("User")
    card = user.get_attribute("card")
    assert card.credit_card == "invalid card"
    nick = user.get_attribute("nick")
    assert nick.length == "3..10"
    assert nick.range == "1..2"
    assert nick.script_assert == "script"
    assert nick.url == "http://example.com"
    ok = user.get_attribute("ok")
    assert ok.assert_true == "must be true"
    assert ok.assert_false == "must be false"
