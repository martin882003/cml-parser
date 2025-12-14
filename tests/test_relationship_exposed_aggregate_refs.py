import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_relationship_exposed_aggregates_are_linked_to_objects(tmp_path):
    content = """
    ContextMap Demo {
      A [U] -> [D] B {
        exposedAggregates SharedAgg, ModAgg
      }
    }
    BoundedContext A {
      Aggregate SharedAgg {}
    }
    BoundedContext B {
      Module M {
        Aggregate ModAgg {}
      }
    }
    """
    path = tmp_path / "rel_exposed_aggs.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    rel = cml.get_context_map("Demo").relationships[0]
    assert rel.exposed_aggregates == ["SharedAgg", "ModAgg"]
    assert [a.name for a in rel.exposed_aggregate_refs] == ["SharedAgg", "ModAgg"]

    ctx_a = cml.get_context("A")
    assert rel.exposed_aggregate_refs[0] is ctx_a.get_aggregate("SharedAgg")

    ctx_b = cml.get_context("B")
    mod_agg = ctx_b.modules[0].aggregates[0]
    assert rel.exposed_aggregate_refs[1] is mod_agg

