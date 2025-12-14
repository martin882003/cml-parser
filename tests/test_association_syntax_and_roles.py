import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_association_declaration(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Sales {
        Entity Order {
          -- Customer customer
        }
        Entity Customer {}
      }
    }
    """
    path = tmp_path / "association.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    order = cml.get_context("Demo").get_aggregate("Sales").get_entity("Order")
    assoc = order.get_attribute("customer")
    assert assoc is not None
    assert assoc.is_reference is True


def test_unnamed_association_is_modeled(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Sales {
        Entity Order {
          -- Customer;
        }
        Entity Customer {}
      }
    }
    """
    path = tmp_path / "unnamed_association.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    order = cml.get_context("Demo").get_aggregate("Sales").get_entity("Order")
    assert order is not None
    assert len(order.associations) == 1
    assert order.associations[0].target == "Customer"


def test_customer_supplier_roles_variants(tmp_path):
    content = """
    ContextMap Demo {
      [U,S] A -> [D,C] B {
        downstreamRights = OPINION_LEADER
      }
    }
    BoundedContext A {}
    BoundedContext B {}
    """
    path = tmp_path / "cs_roles.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    cm = cml.get_context_map("Demo")
    rel = cm.relationships[0]
    assert "U" in rel.roles and "S" in rel.roles and "D" in rel.roles and "C" in rel.roles
    assert rel.downstream_rights == "OPINION_LEADER"
