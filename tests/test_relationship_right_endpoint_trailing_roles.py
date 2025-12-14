import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_relationship_right_endpoint_trailing_roles(tmp_path):
    content = """
    ContextMap Demo {
      A <-> B
      [P] C <-> [P] D : PartnerLeading
      E [P] <-> F [P] : PartnerTrailing
      G [SK] <-> H [SK] : KernelTrailing
    }
    """
    path = tmp_path / "rel_right_endpoint_roles.cml"
    path.write_text(content, encoding="utf-8")

    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    cm = cml.get_context_map("Demo")
    assert cm is not None
    assert len(cm.relationships) == 4

    assert cm.relationships[0].type == "Shared-Kernel"
    assert cm.relationships[1].type == "Partnership"

    partner_trailing = cm.relationships[2]
    assert partner_trailing.type == "Partnership"
    assert partner_trailing.name == "PartnerTrailing"
    assert "P" in partner_trailing.roles

    kernel_trailing = cm.relationships[3]
    assert kernel_trailing.type == "Shared-Kernel"
    assert kernel_trailing.name == "KernelTrailing"
    assert "SK" in kernel_trailing.roles

