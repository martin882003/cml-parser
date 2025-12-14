import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_operation_publish_with_eventbus(tmp_path):
    content = """
    BoundedContext Demo {
      Service Billing {
        void send() publish to "topic/billing" eventBus = bus1;
        void listen() subscribe to BillingEvents eventBus = bus2;
      }
    }
    """
    path = tmp_path / "pubsub.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    svc = cml.get_context("Demo").get_service("Billing")
    send = svc.get_operation("send")
    assert send.publishes_to == "topic/billing"
    assert send.publishes_event_bus == "bus1"
    listen = svc.get_operation("listen")
    assert listen.subscribes_to == "BillingEvents"
    assert listen.subscribes_event_bus == "bus2"


def test_repo_method_publish_subscribe(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Sales {
        Repository OrderRepo {
          Order find() publish to "topic/orders" eventBus = busA;
          Order consume() subscribe to Orders eventBus = busB;
        }
      }
    }
    """
    path = tmp_path / "repo_pubsub.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    repo = cml.get_context("Demo").get_aggregate("Sales").get_repository("OrderRepo")
    find = repo.get_operation("find")
    assert find.publishes_to == "topic/orders"
    assert find.publishes_event_bus == "busA"
    consume = repo.get_operation("consume")
    assert consume.subscribes_to == "Orders"
    assert consume.subscribes_event_bus == "busB"


def test_service_subscribe_eventbus(tmp_path):
    content = """
    BoundedContext Demo {
      Service Notifications subscribe to "topic/notifications" eventBus = busSvc {
        void send();
      }
    }
    """
    path = tmp_path / "svc_subscribe.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    svc = cml.get_context("Demo").get_service("Notifications")
    assert svc.subscribe_to == "topic/notifications"
    assert svc.subscribe_event_bus == "busSvc"
