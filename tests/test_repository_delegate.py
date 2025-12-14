import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_repository_method_delegate(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Sales {
        Repository OrderRepo {
          Order find() delegates to AccessObject;
        }
      }
    }
    """
    path = tmp_path / "repo_delegate.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    repo = cml.get_context("Demo").get_aggregate("Sales").get_repository("OrderRepo")
    op = repo.get_operation("find")
    assert op.delegate_target == "AccessObject"
