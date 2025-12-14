import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_flow_preserves_connectors_and_delegate_state_transition(tmp_path):
    content = """
    BoundedContext Demo {
      Application {
        Flow F {
          event A + B triggers command C x operation D;
          command Ship delegates to Order aggregate [ -> Packed x Shipped ] emits event E1 o E2;
        }
      }
    }
    """
    path = tmp_path / "flow_connectors.cml"
    path.write_text(content, encoding="utf-8")

    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    flow = cml.get_context("Demo").application.flows[0]
    assert len(flow.steps) == 2

    ev = flow.steps[0]
    assert ev.type == "event"
    assert ev.triggers == ["A", "B"]
    assert ev.trigger_connectors == ["+"]
    assert ev.invocations == ["C", "D"]
    assert ev.invocation_kinds == ["command", "operation"]
    assert ev.invocation_connectors == ["x"]
    assert ev.name == "C"

    cmd = flow.steps[1]
    assert cmd.type == "command"
    assert cmd.delegate == "Order"
    assert cmd.delegate_state_transition is not None
    assert "->" in cmd.delegate_state_transition
    assert "Packed" in cmd.delegate_state_transition
    assert "Shipped" in cmd.delegate_state_transition
    assert cmd.emits == ["E1", "E2"]
    assert cmd.emit_connectors == ["o"]

