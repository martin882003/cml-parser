import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_application_accepts_command_and_domain_events(tmp_path):
    content = """
    BoundedContext Demo {
      Application {
        Command Simple;

        CommandEvent CreateCustomer {
          - String name;
        }

        DomainEvent CustomerCreated {
          String customerId;
        }
      }
    }
    """
    path = tmp_path / "app_cmd_events.cml"
    path.write_text(content, encoding="utf-8")

    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    app = cml.get_context("Demo").application
    assert [c.name for c in app.commands] == ["Simple"]
    # `Command Foo` is treated as a shorthand `CommandEvent Foo` (Xtext-like)
    assert sorted([c.name for c in app.command_events]) == sorted(["CreateCustomer", "Simple"])
    assert [e.name for e in app.domain_events] == ["CustomerCreated"]

    cmd = app.command_events[0]
    assert cmd.get_attribute("name") is not None
    ev = app.domain_events[0]
    assert ev.get_attribute("customerId") is not None
