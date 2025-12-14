import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_value_object_discriminator_and_inheritance(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Identity {
        ValueObject Money {
          inheritanceType = "SINGLE_TABLE"
          discriminatorColumn = "dtype"
          discriminatorValue = "MNY"
          discriminatorType = "STRING"
          discriminatorLength = "3"
          databaseTable = "money"
        }
      }
    }
    """
    path = tmp_path / "vo_disc.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    vo = cml.get_context("Demo").get_aggregate("Identity").get_value_object("Money")
    assert vo.inheritance_type == "SINGLE_TABLE"
    assert vo.discriminator_column == "dtype"
    assert vo.discriminator_value == "MNY"
    assert vo.discriminator_type == "STRING"
    assert vo.discriminator_length == "3"
    assert vo.database_table == "money"
