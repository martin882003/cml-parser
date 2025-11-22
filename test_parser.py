import os
import pytest
import sys
import runpy
import importlib

# Add src to path for testing without installing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from cml_parser import parse_file_safe
from cml_parser import parser as parser_mod

EXAMPLES_DIR = os.path.join(os.path.dirname(__file__), "examples")

def get_cml_files():
    cml_files = []
    for root, dirs, files in os.walk(EXAMPLES_DIR):
        for file in files:
            if file.endswith(".cml"):
                cml_files.append(os.path.join(root, file))
    return cml_files

@pytest.mark.parametrize("file_path", get_cml_files())
def test_parse_cml_safe(file_path):
    print(f"Testing {file_path}")
    result = parse_file_safe(file_path)
    assert result.errors == []
    assert result.model is not None


def test_main_without_args(capsys):
    exit_code = parser_mod.main([])
    captured = capsys.readouterr().err
    assert exit_code == 1
    assert "usage:" in captured.lower()


def test_main_with_file(capsys):
    from pathlib import Path

    tmp = Path(EXAMPLES_DIR) / "tmp_main_test.cml"
    tmp.write_text("ContextMap Demo {}\n", encoding="utf-8")

    exit_code = parser_mod.main([str(tmp)])
    captured = capsys.readouterr().out
    assert exit_code == 0
    assert "Successfully parsed" in captured
    tmp.unlink(missing_ok=True)


def test_main_with_bad_file(capsys, tmp_path):
    tmp = tmp_path / "tmp_main_bad.cml"
    tmp.write_text("ContextMap { invalid", encoding="utf-8")
    exit_code = parser_mod.main([str(tmp)])
    captured = capsys.readouterr().err
    assert exit_code == 1
    assert "Error parsing" in captured


def test_module_cli_guard(monkeypatch):
    # Simulate running as a script without args to exercise the __main__ block.
    monkeypatch.setattr(sys, "argv", ["parser.py"])
    # Remove the module to avoid runpy warning about existing entry.
    sys.modules.pop("cml_parser.parser", None)
    importlib.invalidate_caches()
    with pytest.raises(SystemExit) as excinfo:
        runpy.run_module("cml_parser.parser", run_name="__main__")
    assert excinfo.value.code == 1


def test_parse_file_safe_success():
    from pathlib import Path

    tmp = Path(EXAMPLES_DIR) / "tmp_safe_ok.cml"
    tmp.write_text("ContextMap Demo {}\n", encoding="utf-8")
    result = parse_file_safe(str(tmp))
    assert result.errors == []
    assert result.model is not None
    tmp.unlink(missing_ok=True)


def test_parse_file_safe_failure(tmp_path):
    bad_file = tmp_path / "bad.cml"
    bad_file.write_text("ContextMap { invalid", encoding="utf-8")
    result = parse_file_safe(str(bad_file))
    assert result.model is None
    assert result.errors
    assert "ContextMap" in (result.source or "")


def test_bounded_context_realizes(tmp_path):
    model_file = tmp_path / "bc_realizes.cml"
    model_file.write_text("BoundedContext A implements X realizes Y {}", encoding="utf-8")
    result = parse_file_safe(str(model_file))
    assert result.errors == []
    assert result.model is not None


def test_user_story_and_stakeholders(tmp_path):
    content = """
    BoundedContext Demo {}
    UserStory Demo {
        As a "User"
            I want to do "X"
        so that "I achieve Y"
    }
    Stakeholders of Demo {
        StakeholderGroup Team {
            Stakeholder Dev {
                influence HIGH
                interest HIGH
            }
        }
    }
    ValueRegister VR for Demo {
        ValueCluster VC {
            Value Speed {
                Stakeholder Dev {
                    consequences
                        good "faster delivery"
                        action "optimize" ACT
                }
            }
        }
    }
    """
    model_file = tmp_path / "user_story.cml"
    model_file.write_text(content, encoding="utf-8")
    result = parse_file_safe(str(model_file))
    assert result.errors == []
    assert result.model is not None
