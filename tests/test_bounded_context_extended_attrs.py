import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_bounded_context_business_model_and_evolution(tmp_path):
    content = """
    BoundedContext Sales {
      domainVisionStatement = "Sell more"
      type = FEATURE
      responsibilities = "e-commerce"
      implementationTechnology = "Java"
      knowledgeLevel = CONCRETE
      businessModel = "SaaS"
      evolution = PRODUCT
    }
    """
    path = tmp_path / "bc_attrs.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    ctx = cml.get_context("Sales")
    assert ctx is not None
    assert getattr(ctx, "business_model", None) == "SaaS"
    assert getattr(ctx, "evolution", None) == "PRODUCT"
