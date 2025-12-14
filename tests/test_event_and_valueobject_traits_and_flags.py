import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_valueobject_domain_event_command_event_traits_and_flags(tmp_path):
    content = """
    BoundedContext Demo {
      Aggregate Core {
        Trait Auditable {
          String createdBy;
        }

        abstract ValueObject Money with @Auditable {
          package = com.example.vo
          aggregateRoot
          cache
          optimisticLocking
          String amount;
        }

        abstract DomainEvent Shipped with @Auditable {
          aggregateRoot
          persistent
          package = com.example.events
          cache
          String orderId;
        }

        abstract CommandEvent CreateOrder with @Auditable {
          persistent
          aggregateRoot
          package = com.example.commands
          cache
          String orderId;
        }
      }
    }
    """
    path = tmp_path / "tactic_traits_flags.cml"
    path.write_text(content, encoding="utf-8")

    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []
    agg = cml.get_context("Demo").get_aggregate("Core")

    vo = agg.get_value_object("Money")
    assert vo.is_abstract is True
    assert vo.package == "com.example.vo"
    assert vo.is_aggregate_root is True
    assert vo.cache is True
    assert vo.optimistic_locking is True
    assert "Auditable" in vo.traits
    assert vo.get_attribute("createdBy") is not None

    ev = agg.get_domain_event("Shipped")
    assert ev.is_abstract is True
    assert ev.is_aggregate_root is True
    assert ev.persistent is True
    assert ev.package == "com.example.events"
    assert ev.cache is True
    assert ev.get_attribute("createdBy") is not None

    cmd = next((c for c in agg.command_events if c.name == "CreateOrder"), None)
    assert cmd is not None
    assert cmd.is_abstract is True
    assert cmd.is_aggregate_root is True
    assert cmd.persistent is True
    assert cmd.package == "com.example.commands"
    assert cmd.cache is True
    assert cmd.get_attribute("createdBy") is not None

