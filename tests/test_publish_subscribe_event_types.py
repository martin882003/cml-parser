import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_publish_subscribe_capture_event_type(tmp_path):
    content = """
    BoundedContext Demo {
      Service Billing {
        void send() publish @OrderCreated to "topic/orders" eventBus = bus1;
        void listen() subscribe @OrderCreated to Orders eventBus = bus2;
        void delegate() delegates to @Repo.sync;
      }

      Aggregate Sales {
        Repository OrderRepo {
          Order find() publish @OrderCreated to "topic/orders" eventBus = busA;
          Order consume() subscribe @OrderCreated to Orders eventBus = busB;
          Order delegated() delegates to @AccessObject;
        }
      }
    }
    """
    path = tmp_path / "event_types.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    svc = cml.get_context("Demo").get_service("Billing")
    send = svc.get_operation("send")
    assert send.publishes_to == "topic/orders"
    assert send.publishes_event_type == "OrderCreated"
    assert send.publishes_event_bus == "bus1"

    listen = svc.get_operation("listen")
    assert listen.subscribes_to == "Orders"
    assert listen.subscribes_event_type == "OrderCreated"
    assert listen.subscribes_event_bus == "bus2"

    delegate = svc.get_operation("delegate")
    assert delegate.delegate_target == "@Repo.sync"

    repo = cml.get_context("Demo").get_aggregate("Sales").get_repository("OrderRepo")
    find = repo.get_operation("find")
    assert find.publishes_to == "topic/orders"
    assert find.publishes_event_type == "OrderCreated"
    assert find.publishes_event_bus == "busA"

    consume = repo.get_operation("consume")
    assert consume.subscribes_to == "Orders"
    assert consume.subscribes_event_type == "OrderCreated"
    assert consume.subscribes_event_bus == "busB"

    delegated = repo.get_operation("delegated")
    assert delegated.delegate_target == "@AccessObject"

