import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_servicecutter_full_elements(tmp_path):
    content = """
    UseCase Checkout {
      isLatencyCritical = true
      reads "Cart", "User"
      writes "Order"
    }
    Compatibilities {
      AvailabilityCriticality {
        characteristic HIGH // comment
        "Order", "Payment"
      }
    }
    Aggregate "Orders" {
      "Order", "OrderLine"
    }
    SecurityAccessGroup "Public" {
      "Catalog"
    }
    """
    path = tmp_path / "servicecutter_full.sccd"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    sc = cml.service_cutter
    assert sc is not None
    assert sc.use_cases
    assert sc.compatibilities is not None
    assert sc.characteristics
    assert sc.aggregates
    assert sc.security_access_groups
