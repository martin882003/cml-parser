import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_flow_links_commands_events_operations_and_aggregates(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate OrderAgg {}

      Application {
        Command PlaceOrder;

        DomainEvent OrderPlaced {}

        Service OrderService {
          void ship();
        }

        Flow F {
          event OrderPlaced triggers command PlaceOrder x operation ship;
          command PlaceOrder delegates to OrderAgg aggregate [ -> Done ] emits event OrderPlaced;
        }
      }
    }
    """
    path = tmp_path / "flow_linking.cml"
    path.write_text(content, encoding="utf-8")

    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    ctx = cml.get_context("Demo")
    app = ctx.application
    assert [c.name for c in app.command_events] == ["PlaceOrder"]
    assert [e.name for e in app.domain_events] == ["OrderPlaced"]

    flow = app.flows[0]
    ev_step = flow.steps[0]
    cmd_step = flow.steps[1]

    assert ev_step.trigger_refs and ev_step.trigger_refs[0].name == "OrderPlaced"
    assert ev_step.invocation_command_refs and ev_step.invocation_command_refs[0] is not None
    assert ev_step.invocation_command_refs[0].name == "PlaceOrder"
    assert ev_step.invocation_operation_refs and ev_step.invocation_operation_refs[1] is not None
    assert ev_step.invocation_operation_refs[1].name == "ship"

    assert cmd_step.command_ref is not None and cmd_step.command_ref.name == "PlaceOrder"
    assert cmd_step.delegate_ref is not None and cmd_step.delegate_ref.name == "OrderAgg"
    assert cmd_step.emit_refs and cmd_step.emit_refs[0].name == "OrderPlaced"

