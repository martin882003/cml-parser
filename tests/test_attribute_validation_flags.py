import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_attribute_additional_validation_flags(tmp_path):
    content = """
    BoundedContext Sales {
      Aggregate Ordering {
        Entity Order {
          String code key unique notBlank nullable;
          String status index;
          String ref changeable;
        }
      }
    }
    """
    path = tmp_path / "attr_flags.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    ctx = cml.get_context("Sales")
    agg = ctx.get_aggregate("Ordering")
    ent = agg.get_entity("Order")
    code = ent.get_attribute("code")
    assert code.is_key
    assert getattr(code, "unique", False) is True
    assert getattr(code, "not_blank", False) is True
    assert getattr(code, "nullable", False) is True
    status = ent.get_attribute("status")
    assert getattr(status, "index", False) is True
    ref = ent.get_attribute("ref")
    assert getattr(ref, "changeable", False) is True
