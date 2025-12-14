import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_resource_operation_http_method_path_return_and_hint(tmp_path):
    content = """
    BoundedContext Demo {
      Resource Customers {
        String getById(String id) GET path = "/customers/{id}" return = "200" hint = "idempotent";
      }
    }
    """
    path = tmp_path / "resource_op_http.cml"
    path.write_text(content, encoding="utf-8")
    cml = parse_file_safe(str(path))
    assert cml.parse_results.errors == []

    res = cml.get_context("Demo").get_resource("Customers")
    op = res.get_operation("getById")
    assert op.http_method == "GET"
    assert op.path == "/customers/{id}"
    assert op.return_string == "200"
    assert op.hint_text == "idempotent"

