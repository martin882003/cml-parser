import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_entity_with_trait_and_validated_attributes(tmp_path):
    content = """
    BoundedContext Sales {
      Aggregate Ordering {
        Trait Auditable {}
        Entity Order with @Auditable {
          String orderNumber required notEmpty;
          - Customer customer;
        }
        Entity Customer {}
      }
    }
    """
    path = tmp_path / "tactical_flags.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    ctx = cml.get_context("Sales")
    assert ctx is not None
    agg = ctx.get_aggregate("Ordering")
    assert agg is not None
    entity = agg.get_entity("Order")
    assert entity is not None
    attr = entity.get_attribute("orderNumber")
    assert attr is not None
    assert getattr(entity, "traits", None) and "Auditable" in entity.traits
    assert getattr(attr, "required", False) is True
    assert getattr(attr, "not_empty", False) is True
