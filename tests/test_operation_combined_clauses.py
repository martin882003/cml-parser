import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_operation_combines_publish_delegate_hint_throws_any_order(tmp_path):
    content = """
    BoundedContext Demo {
      Service Api {
        void sync()
          hint = "idempotent"
          publish @OrderCreated to "topic/orders" eventBus = bus
          delegates to @Repo.sync
          : write[PAID]
          throws Error;

        void reverse()
          : read-only
          delegates to Repo.sync
          publish to "topic/other"
          hint = "rev"
          throws E2;
      }
    }
    """
    path = tmp_path / "op_combined_clauses.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    svc = cml.get_context("Demo").get_service("Api")

    sync = svc.get_operation("sync")
    assert sync.hint_text == "idempotent"
    assert sync.publishes_event_type == "OrderCreated"
    assert sync.publishes_to == "topic/orders"
    assert sync.publishes_event_bus == "bus"
    assert sync.delegate_target == "@Repo.sync"
    assert sync.hint == "write"
    assert sync.state_transition == "[PAID]"
    assert sync.throws == ["Error"]

    reverse = svc.get_operation("reverse")
    assert reverse.hint in ("read-only", "read")
    assert reverse.delegate_target == "Repo.sync"
    assert reverse.publishes_to == "topic/other"
    assert reverse.publishes_event_type is None
    assert reverse.hint_text == "rev"
    assert reverse.throws == ["E2"]

