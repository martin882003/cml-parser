import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_flow_accepts_lowercase_x_o_connectors(tmp_path):
    content = """
    BoundedContext Demo {
      Application {
        Flow AltFlow {
          event OrderPlaced triggers command createInvoice x command notify;
          event OrderPlaced triggers operation op1 o operation op2;
          command ship delegates to Order aggregate [ -> Packed x Shipped ] emits event OrderShipped o OrderDelivered;
        }
      }
    }
    """
    path = tmp_path / "flow_lowercase_connectors.cml"
    path.write_text(content, encoding="utf-8")

    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    flow = cml.get_context("Demo").application.flows[0]
    assert len(flow.steps) == 3
    assert flow.steps[2].delegate == "Order"
    assert flow.steps[2].emits == ["OrderShipped", "OrderDelivered"]

