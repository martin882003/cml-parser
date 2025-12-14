import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_domain_event_flags(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Ordering {
        DomainEvent Shipped {
          aggregateRoot
          persistent
          belongsTo Logistics
          validate = "checked"
          databaseTable = "events"
          String orderId
        }
      }
    }
    """
    path = tmp_path / "event_flags.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    event = cml.get_context("Demo").get_aggregate("Ordering").get_domain_event("Shipped")
    assert event.belongs_to == "Logistics"
    assert event.validate == "checked"
    assert event.database_table == "events"
    assert event.persistent is True
