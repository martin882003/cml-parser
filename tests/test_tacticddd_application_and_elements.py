import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe
from cml_parser.cml_objects import BasicType


def test_tacticdddapplication_collects_services_and_domain_objects(tmp_path):
    content = """
    TacticDDDApplication App {
      basePackage = com.example.app
      Service PingService {
        void ping();
      }
      BasicType Money {
        hint = "amount"
        immutable
        String value;
      }
    }
    """
    path = tmp_path / "tactic_app.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    assert len(cml.tactic_applications) == 1
    app = cml.tactic_applications[0]
    assert app.name == "App"
    assert app.base_package == "com.example.app"
    assert [s.name for s in app.services] == ["PingService"]

    basic_types = [o for o in app.domain_objects if isinstance(o, BasicType)]
    assert [b.name for b in basic_types] == ["Money"]
    money = basic_types[0]
    assert money.hint == "amount"
    assert money.immutable is True
    assert money.get_attribute("value").type == "String"


def test_resource_modifiers_and_operations(tmp_path):
    content = """
    BoundedContext Demo {
      Resource Customers {
        path = "/customers"
        hint = "REST"
        scaffold
        void list();
      }
    }
    """
    path = tmp_path / "resource.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    res = cml.get_context("Demo").get_resource("Customers")
    assert res.path == "/customers"
    assert res.hint == "REST"
    assert res.scaffold is True
    assert res.get_operation("list") is not None


def test_consumer_modifiers(tmp_path):
    content = """
    BoundedContext Demo {
      Consumer BillingConsumer {
        hint = "kafka"
        queueName = billing/in
        subscribe to billing/in eventBus = kafkaBus
        unmarshall to @BillingEvent
        inject com.example.Service
      }
    }
    """
    path = tmp_path / "consumer.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    consumer = cml.get_context("Demo").get_consumer("BillingConsumer")
    assert consumer.hint == "kafka"
    assert consumer.queue_name == "billing/in"
    assert consumer.subscribe_to == "billing/in"
    assert consumer.subscribe_event_bus == "kafkaBus"
    assert consumer.unmarshall_to == "BillingEvent"
    assert consumer.dependencies == ["com.example.Service"]


def test_service_modifiers_inside_body(tmp_path):
    content = """
    BoundedContext Demo {
      Service Notifications {
        gap
        webservice
        subscribe to "events/notifications" eventBus = busSvc
        hint = "REST"
        void send();
      }
    }
    """
    path = tmp_path / "service_body_mods.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    svc = cml.get_context("Demo").get_service("Notifications")
    assert svc.gap_class is True
    assert svc.webservice is True
    assert svc.subscribe_to == "events/notifications"
    assert svc.subscribe_event_bus == "busSvc"
    assert svc.hint == "REST"
    assert svc.get_operation("send") is not None


def test_repository_modifiers_inside_body(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Sales {
        Repository OrderRepo {
          gap
          hint = "JPA"
          subscribe to "db/events" eventBus = bus1
          inject com.example.Helper
          Order find();
        }
      }
    }
    """
    path = tmp_path / "repo_body_mods.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    repo = cml.get_context("Demo").get_aggregate("Sales").get_repository("OrderRepo")
    assert repo.gap_class is True
    assert repo.hint == "JPA"
    assert repo.subscribe_to == "db/events"
    assert repo.subscribe_event_bus == "bus1"
    assert repo.dependencies == ["com.example.Helper"]
    assert repo.get_operation("find") is not None


def test_basic_type_attaches_to_aggregate_basic_types(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Types {
        BasicType Money {
          immutable
          String value;
        }
      }
    }
    """
    path = tmp_path / "basic_type_agg.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    agg = cml.get_context("Demo").get_aggregate("Types")
    assert [bt.name for bt in agg.basic_types] == ["Money"]
    assert agg.basic_types[0].immutable is True
