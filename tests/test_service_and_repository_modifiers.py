import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_service_modifiers_and_subscribe(tmp_path):
    content = """
    BoundedContext Demo {
      Service Notifications gap webservice subscribe to "events/notifications" hint = "REST" {
        void send();
      }
    }
    """
    path = tmp_path / "service_modifiers.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    svc = cml.get_context("Demo").get_service("Notifications")
    assert svc.gap_class is True
    assert svc.webservice is True
    assert svc.subscribe_to == "events/notifications"
    assert svc.hint == "REST"


def test_repository_method_metadata(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Sales {
        Repository OrderRepo gap hint = "JPA" subscribe to "db/events" {
          Order find() query = "select o" condition = "where o.id = :id" cache construct build map groupBy = "x" orderBy = "y";
        }
      }
    }
    """
    path = tmp_path / "repo_meta.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    repo = cml.get_context("Demo").get_aggregate("Sales").get_repository("OrderRepo")
    assert repo.gap_class is True
    assert repo.hint == "JPA"
    assert repo.subscribe_to == "db/events"
    op = repo.get_operation("find")
    assert op.query == "select o"
    assert op.condition == "where o.id = :id"
    assert op.cache is True
    assert op.construct is True
    assert op.build is True
    assert op.map_flag is True
    assert op.group_by == "x"
    assert op.order_by == "y"
