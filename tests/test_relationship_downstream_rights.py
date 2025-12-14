import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_relationship_with_extended_downstream_rights(tmp_path):
    content = """
    ContextMap Demo {
      A [U] -> [D] B {
        downstreamRights = DECISION_MAKER
        exposedAggregates = Product
      }
    }
    BoundedContext A {}
    BoundedContext B {
      Aggregate Product {}
    }
    """
    path = tmp_path / "relationship_rights.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    cm = cml.context_maps[0]
    rels = cm.relationships
    assert rels
    assert rels[0].downstream_rights == "DECISION_MAKER"
