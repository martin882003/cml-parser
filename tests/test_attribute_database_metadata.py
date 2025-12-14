import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_attribute_database_and_fetch_metadata(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Storage {
        Entity Document {
          - FileData data cascade = "ALL" fetch = "EAGER" databaseColumn = "doc_data";
          - List<Tag> tags databaseJoinTable = "doc_tags" databaseJoinColumn = "doc_id";
        }
      }
    }
    """
    path = tmp_path / "attr_db.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    ent = cml.get_context("Demo").get_aggregate("Storage").get_entity("Document")
    data = ent.get_attribute("data")
    assert data.cascade == "ALL"
    assert data.fetch == "EAGER"
    assert data.database_column == "doc_data"
    tags = ent.get_attribute("tags")
    assert tags.database_join_table == "doc_tags"
    assert tags.database_join_column == "doc_id"
