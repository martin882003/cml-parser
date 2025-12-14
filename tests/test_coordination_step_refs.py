import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_coordination_step_refs_link_to_context_service_operation(tmp_path):
    content = """
    BoundedContext Demo {
      Application {
        Coordination Sync {
          Billing::InvoiceService::create;
        }
      }
    }

    BoundedContext Billing {
      Service InvoiceService {
        void create();
      }
    }
    """
    path = tmp_path / "coord_refs.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    coord = cml.get_context("Demo").application.coordinations[0]
    assert coord.steps == ["Billing::InvoiceService::create"]
    assert len(coord.step_refs) == 1
    step = coord.step_refs[0]
    assert (step.bounded_context, step.service, step.operation) == ("Billing", "InvoiceService", "create")
    assert step.bounded_context_ref and step.bounded_context_ref.name == "Billing"
    assert step.service_ref and step.service_ref.name == "InvoiceService"
    assert step.operation_ref and step.operation_ref.name == "create"

