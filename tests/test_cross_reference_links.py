import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_context_realizes_refines_and_owner_and_value_register_context_refs(tmp_path):
    content = """
    BoundedContext Base {}
    BoundedContext OwnerTeam {}
    BoundedContext Core realizes Legacy, Reports refines Base {
      Aggregate Agg {
        owner OwnerTeam
      }
    }
    ValueRegister VR for Core {}
    """
    path = tmp_path / "cross_refs.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    core = cml.get_context("Core")
    assert core.refines_ref is cml.get_context("Base")
    assert {c.name for c in core.realizes_refs} == {"Legacy", "Reports"}
    assert cml.get_context("Legacy") is not None
    assert cml.get_context("Reports") is not None

    agg = core.get_aggregate("Agg")
    assert agg.owner_ref is cml.get_context("OwnerTeam")

    vr = cml.value_registers[0]
    assert vr.context_ref is core

