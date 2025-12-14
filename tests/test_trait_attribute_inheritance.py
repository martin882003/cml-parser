import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_entity_inherits_attributes_from_trait(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Core {
        Trait Auditable {
          String createdBy;
        }
        Entity Order with @Auditable {
          String orderNumber;
        }
      }
    }
    """
    path = tmp_path / "trait_inheritance.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    ctx = cml.get_context("Demo")
    agg = ctx.get_aggregate("Core")
    entity = agg.get_entity("Order")
    assert "Auditable" in entity.traits
    # Inherited attribute from trait should be present
    assert entity.get_attribute("createdBy") is not None
