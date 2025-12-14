import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_flow_with_event_and_command_invocations(tmp_path):
    content = """
    BoundedContext Demo {
      Application {
        Flow OrderFlow {
          event OrderPlaced triggers command createInvoice + command notify;
          command ship delegates to Order aggregate emits event OrderShipped;
        }
      }
    }
    """
    path = tmp_path / "flow_detail.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    app = cml.get_context("Demo").application
    flow = app.flows[0]
    assert len(flow.steps) == 2


def test_coordination_paths(tmp_path):
    content = """
    BoundedContext Demo {
      Application {
        Coordination Sync {
          Billing::InvoiceService::create;
          Shipping::DeliveryService::ship;
        }
      }
    }
    """
    path = tmp_path / "coordination.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    app = cml.get_context("Demo").application
    coord = app.coordinations[0]
    assert coord.steps == ["Billing::InvoiceService::create", "Shipping::DeliveryService::ship"]
