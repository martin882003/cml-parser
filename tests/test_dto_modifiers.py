import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_dto_modifiers(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Billing {
        DataTransferObject InvoiceDTO gap hint = "dto" validate = "ok" {
          String id
        }
      }
    }
    """
    path = tmp_path / "dto_modifiers.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    dto = cml.get_context("Demo").get_aggregate("Billing").data_transfer_objects[0]
    assert dto.validate == "ok"
