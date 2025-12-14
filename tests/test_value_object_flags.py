import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_value_object_flags(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Identity {
        ValueObject Address {
          belongsTo UserContext
          validate = "valid"
          immutable
          persistent
          databaseTable = "address"
          String line1
        }
      }
    }
    """
    path = tmp_path / "vo_flags.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    vo = cml.get_context("Demo").get_aggregate("Identity").get_value_object("Address")
    assert vo.belongs_to == "UserContext"
    assert vo.validate == "valid"
    assert vo.immutable is True
    assert vo.persistent is True
    assert vo.database_table == "address"
