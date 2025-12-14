import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_attribute_pattern_and_size(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Identity {
        Entity User {
          String email email pattern = "[^@]+@[^@]+";
          String nick size = "3..20" notBlank;
        }
      }
    }
    """
    path = tmp_path / "attr_meta.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    user = cml.get_context("Demo").get_aggregate("Identity").get_entity("User")
    email_attr = user.get_attribute("email")
    assert email_attr.email is True
    assert email_attr.pattern == "[^@]+@[^@]+"
    nick_attr = user.get_attribute("nick")
    assert nick_attr.size == "3..20"
    assert nick_attr.not_blank is True
