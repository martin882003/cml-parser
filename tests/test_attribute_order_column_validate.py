import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_attribute_order_column_and_validate(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Storage {
        Entity Document {
          - Tag tags orderColumn = "pos";
          String name validate = "notEmpty";
        }
      }
    }
    """
    path = tmp_path / "attr_order_validate.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    ent = cml.get_context("Demo").get_aggregate("Storage").get_entity("Document")
    tags = ent.get_attribute("tags")
    assert tags.order_column == "pos"
    name = ent.get_attribute("name")
    assert name.validate == "notEmpty"
