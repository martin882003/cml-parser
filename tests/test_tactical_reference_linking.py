import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_text


def test_extends_belongs_to_and_association_target_refs():
    cml = parse_text(
        """
        BoundedContext Demo {
          Aggregate A {
            Entity Base {}
            Entity Derived extends @Base {}
            Entity Container {}
            Entity Item {
              belongsTo Container
              -- Container;
            }

            Trait AssocTrait {
              -- Container;
            }
            Entity WithTrait with @AssocTrait {}
          }
        }
        """
    )

    agg = cml.get_context("Demo").get_aggregate("A")
    base = agg.get_entity("Base")
    derived = agg.get_entity("Derived")
    container = agg.get_entity("Container")
    item = agg.get_entity("Item")
    with_trait = agg.get_entity("WithTrait")

    assert derived.extends == "Base"
    assert derived.extends_ref is base

    assert item.belongs_to == "Container"
    assert item.belongs_to_ref is container
    assert len(item.associations) == 1
    assert item.associations[0].target == "Container"
    assert item.associations[0].target_ref is container

    assert any(a.target == "Container" for a in with_trait.associations)
    assert any(a.target_ref is container for a in with_trait.associations)

