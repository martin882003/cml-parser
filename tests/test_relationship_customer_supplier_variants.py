import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_customer_supplier_keyword_variant(tmp_path):
    content = """
    ContextMap Demo {
      A Customer-Supplier B {
        downstreamRights = INFLUENCER
      }
    }
    BoundedContext A {}
    BoundedContext B {}
    """
    path = tmp_path / "cs_keyword.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    rel = cml.get_context_map("Demo").relationships[0]
    assert rel.type in ("Customer-Supplier", "CUSTOMER-SUPPLIER")
    assert rel.downstream_rights == "INFLUENCER"


def test_customer_supplier_roles_inline(tmp_path):
    content = """
    ContextMap Demo {
      [U,S] A -> [D,C] B
    }
    BoundedContext A {}
    BoundedContext B {}
    """
    path = tmp_path / "cs_roles_inline.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    rel = cml.get_context_map("Demo").relationships[0]
    assert set(rel.roles) >= {"U", "S", "D", "C"}
