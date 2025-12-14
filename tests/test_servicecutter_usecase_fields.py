import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_servicecutter_usecase_reads_writes_latency(tmp_path):
    content = """
    UseCase Checkout {
      isLatencyCritical = true
      reads "Cart", "User"
      writes "Order"
    }
    """
    path = tmp_path / "sc_uc.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    sc = cml.service_cutter
    assert sc is not None
    uc = sc.use_cases[0]
    assert uc.name == "Checkout"
    assert uc.is_latency_critical is True
    assert "Cart" in uc.reads and "User" in uc.reads
    assert "Order" in uc.writes
