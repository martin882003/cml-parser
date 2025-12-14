import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_state_transition_accepts_end_state_marker(tmp_path):
    content = """
    BoundedContext Demo {
      Application {
        Flow F {
          command Ship delegates to Order aggregate [ -> Packed x Shipped* ];
        }
      }
    }
    """
    path = tmp_path / "state_transition_star.cml"
    path.write_text(content, encoding="utf-8")

    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    step = cml.get_context("Demo").application.flows[0].steps[0]
    assert step.delegate_state_transition is not None
    assert "Shipped*" in step.delegate_state_transition

