from pytest_bdd import scenarios, given, when, then, parsers
import pytest

# Load feature file
scenarios("../features/login.feature")

# Fixture to hold shared state
@pytest.fixture
def user():
    return {}

@given("I am on the login page")
def login_page(user):
    user["page"] = "login"

@when("I enter valid credentials")
def enter_credentials(user):
    user["logged_in"] = True

@then("I should be redirected to the dashboard")
def redirected_to_dashboard(user):
    assert user.get("logged_in") is True
