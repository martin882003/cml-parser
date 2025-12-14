import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_reference_cache_inverse_transient_valid_and_label(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Sales {
        Entity Order {
          - Customer customer cache inverse transient valid = "must be valid" -- "places";
          - Customer other not cache not inverse;
        }
        Entity Customer {}
      }
    }
    """
    path = tmp_path / "ref_flags_label.cml"
    path.write_text(content, encoding="utf-8")

    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    order = cml.get_context("Demo").get_aggregate("Sales").get_entity("Order")
    customer = order.get_attribute("customer")
    assert customer.is_reference is True
    assert customer.cache is True
    assert customer.inverse is True
    assert customer.transient is True
    assert customer.valid is True
    assert customer.valid_message == "must be valid"
    assert customer.association_label == "places"

    other = order.get_attribute("other")
    assert other.cache is False
    assert other.inverse is False
    assert other.transient is False
    assert other.valid is False

