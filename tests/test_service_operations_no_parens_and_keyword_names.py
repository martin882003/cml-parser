import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_text


def test_service_operation_without_parentheses_is_parsed():
    cml = parse_text(
        """
        BoundedContext BC {
          Aggregate A {
            Service S {
              createCustomerProfile;
            }
          }
        }
        """
    )
    svc = cml.get_context("BC").get_aggregate("A").get_service("S")
    assert svc is not None
    assert svc.get_operation("createCustomerProfile") is not None


def test_keyword_like_names_can_be_used_as_identifiers():
    cml = parse_text(
        """
        BoundedContext BC {
          Aggregate A {
            Entity E {
              String characteristic
            }
            ValueObject V {
              String risk
            }
            Service S {
              @SolverResult generateDecomposition(@ServiceCutterContext context);
            }
          }
        }
        """
    )

    agg = cml.get_context("BC").get_aggregate("A")
    ent = agg.get_entity("E")
    assert ent is not None
    assert ent.get_attribute("characteristic") is not None

    vo = agg.get_value_object("V")
    assert vo is not None
    assert vo.get_attribute("risk") is not None

    svc = agg.get_service("S")
    assert svc is not None
    op = svc.get_operation("generateDecomposition")
    assert op is not None
    assert op.return_type == "@SolverResult"
    assert len(op.parameters) == 1
    assert op.parameters[0].name == "context"
    assert op.parameters[0].type == "ServiceCutterContext"
    assert op.parameters[0].is_reference is True
