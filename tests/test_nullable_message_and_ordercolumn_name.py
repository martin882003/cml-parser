import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_nullable_with_message_and_ordercolumn_name(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Identity {
        Entity User {
          String email nullable = "must allow nulls";
          - List<Role> roles orderColumn = "pos" orderby = "name";
        }
      }
    }
    """
    path = tmp_path / "attr_nullable_ordercolname.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    user = cml.get_context("Demo").get_aggregate("Identity").get_entity("User")
    email = user.get_attribute("email")
    assert email.nullable is True
    assert email.nullable_message == "must allow nulls"
    roles = user.get_attribute("roles")
    assert roles.order_column == "pos"
    assert roles.order_by == "name"
