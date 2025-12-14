import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_aggregate_quality_attributes_and_user_requirements(tmp_path):
    content = """
    UseCase UC1 {}
    UseCase UC2 {}
    UseCase UC3 {}

    UserStory US1 {
      As a "User"
      I want to "buy"
      so that "value"
    }
    UserStory US2 {
      As a "User"
      I want to "return"
      so that "value"
    }

    BoundedContext Shop {
      Aggregate Checkout {
        responsibilities = "Payments", "Invoices"
        owner = Shop
        knowledgeLevel = META

        useCases = UC1, UC2
        userStories = US1
        features = UC3, US2

        structuralVolatility = OFTEN
        contentVolatility = RARELY
        availabilityCriticality = HIGH
        consistencyCriticality = LOW
        storageSimilarity = HUGE
        securityCriticality = NORMAL
        securityZone = "ZoneA"
        securityAccessGroup = "GroupA"
      }
    }
    """
    path = tmp_path / "aggregate_quality.cml"
    path.write_text(content, encoding="utf-8")
    model = parse_file_safe(str(path))
    assert model.parse_results.errors == []

    agg = model.get_context("Shop").get_aggregate("Checkout")
    assert agg.responsibilities == "Payments, Invoices"
    assert agg.owner == "Shop"
    assert agg.knowledge_level == "META"

    req_names = [getattr(r, "name", None) for r in agg.user_requirements]
    assert req_names == ["UC1", "UC2", "US1", "UC3", "US2"]

    assert agg.likelihood_for_change == "OFTEN"
    assert agg.content_volatility == "RARELY"
    assert agg.availability_criticality == "HIGH"
    assert agg.consistency_criticality == "LOW"
    assert agg.storage_similarity == "HUGE"
    assert agg.security_criticality == "NORMAL"
    assert agg.security_zone == "ZoneA"
    assert agg.security_access_group == "GroupA"

