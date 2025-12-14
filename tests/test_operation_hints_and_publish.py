import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_operation_hint_and_state_transition(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Sales {
        Service Billing {
          void charge(Order order) : write[PAID] throws PaymentFailed;
          void getStatus() : read-only;
        }
      }
    }
    """
    path = tmp_path / "op_hints.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    svc = cml.get_context("Demo").get_aggregate("Sales").get_service("Billing")
    charge = svc.get_operation("charge")
    assert charge.hint == "write"
    assert charge.state_transition == "[PAID]"
    assert charge.publishes_to is None  # publish tail is a separate statement below
    readonly = svc.get_operation("getStatus")
    assert readonly.hint in ("read-only", "read")
    # publish tail should be captured on the standalone 'publish to' operation tail statement (raw op)


def test_operation_string_hint_option(tmp_path):
    content = """
    BoundedContext Demo {
      Service Billing {
        void ping() hint = "idempotent";
        void charge(Order order) hint = "billing" : write[PAID];
      }
    }
    """
    path = tmp_path / "op_string_hint.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    svc = cml.get_context("Demo").get_service("Billing")

    ping = svc.get_operation("ping")
    assert ping.hint_text == "idempotent"
    assert ping.hint is None

    charge = svc.get_operation("charge")
    assert charge.hint_text == "billing"
    assert charge.hint == "write"
    assert charge.state_transition == "[PAID]"


def test_service_publish_tail(tmp_path):
    content = """
    BoundedContext Demo {
      Service Notifications {
        void send() publish to "topic/notifications";
      }
    }
    """
    path = tmp_path / "op_publish.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    svc = cml.get_context("Demo").get_service("Notifications")
    op = svc.get_operation("send")
    assert op.publishes_to == "topic/notifications"
