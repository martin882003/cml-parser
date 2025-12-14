import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_flow_command_and_operation_initiated_by(tmp_path):
    content = """
    BoundedContext Demo {
      Application {
        Flow F {
          command PlaceOrder [ initiated by "Customer" ] emits event OrderPlaced;
          operation reserveStock [ initiated by "Admin" ] delegates to Inventory aggregate emits event StockReserved;
        }
      }
    }
    """
    path = tmp_path / "flow_initiated_by.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    flow = cml.get_context("Demo").application.flows[0]
    assert len(flow.steps) == 2
    assert flow.steps[0].type == "command"
    assert flow.steps[0].initiated_by == "Customer"
    assert flow.steps[1].type == "operation"
    assert flow.steps[1].initiated_by == "Admin"

