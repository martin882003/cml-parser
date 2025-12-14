import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_servicecutter_configuration_parsing(tmp_path):
    content = """
    UseCase Checkout {
      isLatencyCritical = true
      reads "Cart", "User"
      writes "Order"
    }
    Aggregate "Orders" {
      "Order", "OrderLine"
    }
    SecurityAccessGroup "Public" {
      "Catalog"
    }
    Compatibilities {
      AvailabilityCriticality {
        characteristic HIGH // highly available
        "Order", "Payment"
      }
    }
    """
    path = tmp_path / "servicecutter.sccd"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    assert hasattr(cml, "service_cutter")
