import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_bounded_context_unordered_implements_realizes_refines(tmp_path):
    content = """
    Domain D {
      Subdomain S {}
    }
    BoundedContext Base {}
    BoundedContext BC realizes Base implements S refines Base {}
    """
    path = tmp_path / "bounded_context_unordered_links.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    bc = cml.get_context("BC")
    assert bc is not None
    assert bc.realizes == ["Base"]
    assert bc.refines == "Base"
    assert any(getattr(p, "name", None) == "S" for p in bc.implements)

