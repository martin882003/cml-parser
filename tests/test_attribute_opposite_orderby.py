import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_attribute_opposite_and_orderby(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Library {
        Entity Book {
          - Author author opposite = "books" orderby = "title";
        }
      }
    }
    """
    path = tmp_path / "attr_opposite_orderby.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    book = cml.get_context("Demo").get_aggregate("Library").get_entity("Book")
    author_attr = book.get_attribute("author")
    assert author_attr.opposite == "books"
    assert author_attr.order_by == "title"
