import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cml_parser import parse_file_safe


def test_use_case_secondary_actors_and_interactions_features(tmp_path):
    content = """
    UseCase Checkout {
      actor = "Customer"
      secondaryActors = "Admin", "Support"
      interactions = create a "Order" in "Shop", read "Invoice" with its "id"
    }
    """
    path = tmp_path / "uc_secondary.cml"
    path.write_text(content, encoding="utf-8")
    model = parse_file_safe(str(path))
    assert model.parse_results.errors == []

    uc = model.get_use_case("Checkout")
    assert uc.actor == "Customer"
    assert uc.secondary_actors == ["Admin", "Support"]
    assert any("create" in i for i in uc.interactions)
    assert any("read" in i for i in uc.interactions)


def test_user_story_split_by_and_valuation(tmp_path):
    content = """
    UserStory US1 {}
    UserStory US2 split by US1 {
      As a "User"
      I want to "browse"
      so that "I save time"
      and that "Speed", "Quality" are promoted accepting that "Cost" is harmed
    }
    """
    path = tmp_path / "us_split_valuation.cml"
    path.write_text(content, encoding="utf-8")
    model = parse_file_safe(str(path))
    assert model.parse_results.errors == []

    us2 = next(us for us in model.user_stories if us.name == "US2")
    assert us2.split_by == "US1"
    assert us2.role == "User"
    assert us2.feature == "browse"
    assert us2.benefit == "I save time"
    assert us2.promoted_values == ["Speed", "Quality"]
    assert us2.harmed_values == ["Cost"]


def test_bounded_context_multiple_responsibilities(tmp_path):
    content = """
    BoundedContext Sales {
      responsibilities = "Payments", "Invoices"
    }
    """
    path = tmp_path / "bc_responsibilities.cml"
    path.write_text(content, encoding="utf-8")
    model = parse_file_safe(str(path))
    assert model.parse_results.errors == []
    ctx = model.get_context("Sales")
    assert ctx.responsibilities == "Payments, Invoices"


def test_stakeholders_of_multiple_contexts_with_description(tmp_path):
    content = """
    BoundedContext C1 {}
    BoundedContext C2 {}
    Stakeholders of C1, C2 {
      Stakeholder SH {
        description = "Main stakeholder"
      }
    }
    """
    path = tmp_path / "stakeholders_multi.cml"
    path.write_text(content, encoding="utf-8")
    model = parse_file_safe(str(path))
    assert model.parse_results.errors == []
    sh = model.stakeholders[0]
    assert sh.description == "Main stakeholder"
    assert len(model.stakeholder_sections) == 1
    section = model.stakeholder_sections[0]
    assert section.contexts == ["C1", "C2"]
    assert [c.name for c in section.contexts_refs] == ["C1", "C2"]
