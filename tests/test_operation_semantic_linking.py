import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_operation_delegate_and_event_type_refs(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Sales {
        DomainEvent OrderCreated {}
        Repository Repo {
          void sync();
        }
      }

      Service Api {
        void call() delegates to Repo.sync;
        void send() publish @OrderCreated to "topic/orders";
      }
    }
    """
    path = tmp_path / "op_linking.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    ctx = cml.get_context("Demo")
    assert ctx is not None
    agg = ctx.get_aggregate("Sales")
    repo = agg.get_repository("Repo")
    event = agg.get_domain_event("OrderCreated")
    assert repo is not None
    assert event is not None

    svc = ctx.get_service("Api")
    call = svc.get_operation("call")
    assert call.delegate_target == "Repo.sync"
    assert call.delegate_holder_ref is repo
    assert call.delegate_operation_ref is repo.get_operation("sync")

    send = svc.get_operation("send")
    assert send.publishes_event_type == "OrderCreated"
    assert send.publishes_event_type_ref is event

