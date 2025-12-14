
import pytest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser.parser import parse_text as parse_cml
from cml_parser.parser import CmlSyntaxError
from cml_parser.cml_objects import Attribute

def test_coverage_attribute_options():
    cml_str = """
    ContextMap {
        contains MyContext
    }
    BoundedContext MyContext {
        Aggregate MyAgg {
            Entity MyEntity {
                String myAttr
                String otherAttr 
                
                // Opposite with identifier
                // Syntax: <-> name 
                // OR opposite = "name"
                // OR opposite name
                // cml_model_builder lines 107-112: if opt.oppositeHolder... if name()...
                // oppositeHolder : ( 'opposite' | '<->' ) ( STRING | name )
                
                - List<MyEntity> children <-> parent
                
                // Various validation/db flags
                // Syntax: key [= value]
                
                String creditCard creditCardNumber
                String trueField assertTrue
                String falseField assertFalse
                String cascadeField cascade="ALL"
                String fetchField fetch="EAGER"
                String dbCol databaseColumn="col_name"
                String dbType databaseType="VARCHAR(255)"
                String dbJoinTable databaseJoinTable="join_table_name"
                String dbJoinCol databaseJoinColumn="join_col_name"
                String customHint hint="some hint"
                String validField valid
                String validFieldMsg valid="must be valid"
                String pastField past="must be past"
                String futureField future="must be future"
                String emailField email="must be email"
                String notBlankField notBlank="must not be blank"
                String notEmptyField notEmpty="must not be empty"
                String nullableField nullable="can be null"
                
                // Coverage items:
                // unique, index, changeable, pattern, size, min, max
                // decimalMax, decimalMin, digits, length, range, scriptAssert, url
                // orderColumn, orderby, cache, inverse, transient
                
                String patternField pattern=".*"
            }
        }
    }
    """
    model = parse_cml(cml_str)
    ctx = model.contexts[0]
    agg = ctx.aggregates[0]
    entity = agg.entities[0]
    
    # Check opposite with ID
    children = next(a for a in entity.attributes if a.name == "children")
    assert children.opposite == "parent"
    
    # Check flags
    cc = next(a for a in entity.attributes if a.name == "creditCard")
    # Coverage check: lines 175-176 hit?
    
    hint = next(a for a in entity.attributes if a.name == "customHint")
    assert hint.hint == "some hint"
    
    valid_msg = next(a for a in entity.attributes if a.name == "validFieldMsg")
    assert valid_msg.valid_message == "must be valid"
    
    pat = next(a for a in entity.attributes if a.name == "patternField")
    assert pat.pattern == ".*"

def test_coverage_subdomain_supports_user_story_and_missing():
    # Covers _link_references lines 262-266
    # Grammar: Subdomain name ('supports' idList)? body...
    cml_str = """
    Domain MyDomain {
        Subdomain MySubdomain supports US1, NonExistentReq {
        }
    }
    UserStory US1 {
        As a "user" I want to "do" so that "benefit"
    }
    """
    model = parse_cml(cml_str)
    domain = model.domains[0]
    subdomain = domain.subdomains[0]
    
    assert len(subdomain.supported_requirements) == 2
    
    req_names = {r.name for r in subdomain.supported_requirements}
    assert "US1" in req_names
    assert "NonExistentReq" in req_names
    
    # Check that NonExistentReq was added to use_cases as fallback
    # Note: parse_cml creates CML object and runs _link_references
    assert any(uc.name == "NonExistentReq" for uc in model.use_cases)

def test_coverage_context_implements_domain():
    # Covers _link_references lines 252-255 (linking Domain instead of Subdomain)
    cml_str = """
    Domain MyDomain {}
    BoundedContext MyContext implements MyDomain
    """
    model = parse_cml(cml_str)
    ctx = model.contexts[0]
    dom = model.domains[0]
    
    assert dom in ctx.implements
    assert ctx in dom.implementations

def test_coverage_service_cutter_all_characteristics():
    # Grammar: Compatibilities { characteristicName { characteristic "id" "N1", "N2" } }
    # Try ID for name
    cml_str = """
    Compatibilities {
        AvailabilityCriticality {
            characteristic HighAvail
            "N1"
        }
        ConsistencyCriticality {
            characteristic Strong
            "N3"
        }
        ContentVolatility {
            characteristic Rare
            "N4"
        }
        SecurityCriticality {
            characteristic HighSec
            "N5"
        }
        StorageSimilarity {
            characteristic Shared
            "N6"
        }
        StructuralVolatility {
            characteristic Stable
            "N7"
        }
    }
    """
    model = parse_cml(cml_str)
    sc = model.service_cutter
    assert sc is not None
    assert len(sc.characteristics) == 6

def test_coverage_visit_definitions_exception(monkeypatch):
    # Test line 213 check: except Exception as e: raise e
    # We need to mock visitChildren to raise an exception
    def mock_visit_children(self, ctx):
        raise ValueError("Boom")
    
    from cml_parser.cml_model_builder import CMLModelBuilder
    monkeypatch.setattr(CMLModelBuilder, "visitChildren", mock_visit_children)
    
    cml_str = "Domain D {}"
    with pytest.raises(CmlSyntaxError, match="Boom"):
        parse_cml(cml_str)

