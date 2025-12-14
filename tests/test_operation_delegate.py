import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_operation_delegates_to(tmp_path):
    content = """
    BoundedContext Demo {
      Service Api {
        void sync() delegates to Repo.sync;
      }
    }
    """
    path = tmp_path / "op_delegate.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    svc = cml.get_context("Demo").get_service("Api")
    op = svc.get_operation("sync")
    assert op.delegate_target == "Repo.sync"
