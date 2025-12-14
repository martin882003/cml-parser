import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_domain_event_discriminator_and_inheritance(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Ordering {
        DomainEvent Delivered {
          inheritanceType = "SINGLE_TABLE"
          discriminatorColumn = "dtype"
          discriminatorValue = "DLV"
          discriminatorType = "STRING"
          discriminatorLength = "3"
          databaseTable = "events"
        }
      }
    }
    """
    path = tmp_path / "event_disc.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    ev = cml.get_context("Demo").get_aggregate("Ordering").get_domain_event("Delivered")
    assert ev.inheritance_type == "SINGLE_TABLE"
    assert ev.discriminator_column == "dtype"
    assert ev.discriminator_value == "DLV"
    assert ev.discriminator_type == "STRING"
    assert ev.discriminator_length == "3"
    assert ev.database_table == "events"
