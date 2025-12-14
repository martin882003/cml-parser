import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe

def test_relationship_with_role_markers_and_shared_kernel(tmp_path):
    content = """
    ContextMap Demo {
      [SK] A <-> [SK] B
      [P]  C <-> [P]  D
      A [U] -> [D] E
    }
    BoundedContext A {}
    BoundedContext B {}
    BoundedContext C {}
    BoundedContext D {}
    BoundedContext E {}
    """
    path = tmp_path / "relationship_roles.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    cm = cml.get_context_map("Demo")
    assert cm
    assert len(cm.relationships) == 3
    sk = cm.relationships[0]
    assert "SK" in sk.roles
    partner = cm.relationships[1]
    assert "P" in partner.roles
    ud = cm.relationships[2]
    assert "U" in ud.roles and "D" in ud.roles
    assert ud.type in ("Upstream-Downstream", "UPSTREAM-DOWNSTREAM", "->")
