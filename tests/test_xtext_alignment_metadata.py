import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe
from cml_parser.cml_objects import SubdomainType


def test_bounded_context_refines_and_realizes_and_meta_level(tmp_path):
    content = """
    BoundedContext Core implements Sales realizes Legacy,Reports refines Base {
      knowledgeLevel = META
    }
    BoundedContext Base {}
    """
    path = tmp_path / "bc_refines.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    ctx = cml.get_context("Core")
    assert ctx.refines == "Base"
    assert ctx.realizes == ["Legacy", "Reports"]
    assert ctx.knowledge_level == "META"


def test_context_map_accepts_undefined_state_and_type(tmp_path):
    content = """
    ContextMap MapX {
      type UNDEFINED
      state UNDEFINED
    }
    """
    path = tmp_path / "cm_undefined.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    cm = cml.get_context_map("MapX")
    assert cm.type == "UNDEFINED"
    assert cm.state == "UNDEFINED"


def test_subdomain_type_undefined_and_application_named(tmp_path):
    content = """
    Domain Sales {
      Subdomain Billing type UNDEFINED {}
    }
    BoundedContext Demo {
      Application AppLayer {
        Command Foo;
      }
    }
    """
    path = tmp_path / "subdomain_app.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    sd = cml.get_subdomain("Billing")
    assert sd is not None and sd.type == SubdomainType.UNDEFINED
    app = cml.get_context("Demo").application
    assert app.name == "AppLayer"


def test_bounded_context_implements_domain_part(tmp_path):
    content = """
    Domain Sales {}
    BoundedContext Shop implements Sales {
    }
    """
    path = tmp_path / "implements_domain.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    ctx = cml.get_context("Shop")
    assert ctx is not None
    assert ctx.implements and ctx.implements[0].name == "Sales"
