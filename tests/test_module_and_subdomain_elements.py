import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_module_attributes_external_basepackage_hint(tmp_path):
    content = """
    BoundedContext Demo {
      Module Mod {
        external
        basePackage = com.example.mod
        hint = "ModuleHint"
      }
    }
    """
    path = tmp_path / "module_attrs.cml"
    path.write_text(content, encoding="utf-8")
    model = parse_file_safe(str(path))
    assert model.parse_results.errors == []
    mod = model.get_context("Demo").modules[0]
    assert mod.external is True
    assert mod.base_package == "com.example.mod"
    assert mod.hint == "ModuleHint"


def test_subdomain_contains_services(tmp_path):
    content = """
    Domain Commerce {
      Subdomain Catalog {
        Service Pricing {
          void ping();
        }
      }
    }
    """
    path = tmp_path / "subdomain_services.cml"
    path.write_text(content, encoding="utf-8")
    model = parse_file_safe(str(path))
    assert model.parse_results.errors == []
    sd = model.get_domain("Commerce").get_subdomain("Catalog")
    assert [s.name for s in sd.services] == ["Pricing"]

