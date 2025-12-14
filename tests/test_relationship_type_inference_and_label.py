import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_relationship_type_inference_and_label(tmp_path):
    content = """
    ContextMap Demo {
      A <-> B
      [P] C <-> [P] D : PartnerRel
      E -> F : UpDownRel
      G <- H
      [U,S] Svc -> [D,C] Cust
      X Customer-Supplier Y
      M Supplier-Customer N
    }
    """
    path = tmp_path / "rel_inference.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    cm = cml.get_context_map("Demo")
    assert cm is not None
    assert len(cm.relationships) == 7

    shared = cm.relationships[0]
    assert shared.connection == "<->"
    assert shared.type == "Shared-Kernel"
    assert shared.upstream is None and shared.downstream is None

    partnership = cm.relationships[1]
    assert partnership.connection == "<->"
    assert partnership.type == "Partnership"
    assert partnership.name == "PartnerRel"

    updown = cm.relationships[2]
    assert updown.connection == "->"
    assert updown.type == "Upstream-Downstream"
    assert updown.name == "UpDownRel"
    assert updown.upstream and updown.upstream.name == "E"
    assert updown.downstream and updown.downstream.name == "F"

    downup = cm.relationships[3]
    assert downup.connection == "<-"
    assert downup.type == "Downstream-Upstream"
    assert downup.upstream and downup.upstream.name == "H"
    assert downup.downstream and downup.downstream.name == "G"

    cs_arrow = cm.relationships[4]
    assert cs_arrow.connection == "->"
    assert cs_arrow.type == "Customer-Supplier"
    assert cs_arrow.upstream and cs_arrow.upstream.name == "Svc"
    assert cs_arrow.downstream and cs_arrow.downstream.name == "Cust"

    cs_keyword = cm.relationships[5]
    assert cs_keyword.connection == "Customer-Supplier"
    assert cs_keyword.type == "Customer-Supplier"
    assert cs_keyword.upstream and cs_keyword.upstream.name == "Y"
    assert cs_keyword.downstream and cs_keyword.downstream.name == "X"

    sc_keyword = cm.relationships[6]
    assert sc_keyword.connection == "Supplier-Customer"
    assert sc_keyword.type == "Supplier-Customer"
    assert sc_keyword.upstream and sc_keyword.upstream.name == "M"
    assert sc_keyword.downstream and sc_keyword.downstream.name == "N"

