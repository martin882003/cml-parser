import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_supplier_customer_keyword(tmp_path):
    content = """
    ContextMap Demo {
      A Supplier-Customer B {
        downstreamRights = INFLUENCER
      }
    }
    BoundedContext A {}
    BoundedContext B {}
    """
    path = tmp_path / "supplier_customer.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    rel = cml.get_context_map("Demo").relationships[0]
    assert rel.type in ("Supplier-Customer", "SUPPLIER-CUSTOMER")
    assert rel.downstream_rights == "INFLUENCER"
