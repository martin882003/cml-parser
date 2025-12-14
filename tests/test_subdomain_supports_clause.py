import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_subdomain_supports_user_requirements(tmp_path):
    content = """
    UseCase UC1 {}
    UseCase UC2 {}
    Domain Commerce {
      Subdomain Catalog supports UC1, UC2 {
        type = CORE_DOMAIN
        Entity Product {}
        Service Pricing {}
      }
    }
    """
    path = tmp_path / "subdomain_supports.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    domain = cml.get_domain("Commerce")
    assert domain is not None
    sub = domain.get_subdomain("Catalog")
    assert sub is not None
    assert getattr(sub, "supported_requirements", None) is not None
    assert sorted(req.name for req in sub.supported_requirements) == ["UC1", "UC2"]
