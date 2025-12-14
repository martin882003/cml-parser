import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_repository_method_hint_and_throws_unordered(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Sales {
        Repository OrderRepo hint = "JPA" {
          Order a() throws com.example.Error1, Error2 hint = "fast" cache query = "select o";
          Order b() cache hint = "fast" query = "select o" throws com.example.Error1, Error2;
        }
      }
    }
    """
    path = tmp_path / "repo_method_hint_throws.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    repo = cml.get_context("Demo").get_aggregate("Sales").get_repository("OrderRepo")
    assert repo.hint == "JPA"

    a = repo.get_operation("a")
    assert a.hint_text == "fast"
    assert a.cache is True
    assert a.query == "select o"
    assert a.throws == ["com.example.Error1", "Error2"]

    b = repo.get_operation("b")
    assert b.hint_text == "fast"
    assert b.cache is True
    assert b.query == "select o"
    assert b.throws == ["com.example.Error1", "Error2"]

