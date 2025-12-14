import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_entity_belongs_to_and_discriminator(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Billing {
            Entity Invoice {
              aggregateRoot
              belongsTo OrderContext
              discriminatorColumn = "dtype"
              discriminatorValue = "INV"
              discriminatorType = "STRING"
              discriminatorLength = "3"
              databaseTable = "invoices"
          validate = "checked"
          optimisticLocking
          immutable
        }
      }
    }
    """
    path = tmp_path / "entity_flags.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    ent = cml.get_context("Demo").get_aggregate("Billing").get_entity("Invoice")
    assert ent.belongs_to == "OrderContext"
    assert ent.discriminator_column == "dtype"
    assert ent.discriminator_value == "INV"
    assert ent.discriminator_type == "STRING"
    assert ent.discriminator_length == "3"
    assert ent.database_table == "invoices"
    assert ent.validate == "checked"
    assert ent.optimistic_locking is True
    assert ent.immutable is True
