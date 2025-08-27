from pytest_bdd import scenarios, given, when, then, parsers
import pytest

scenarios("../features")

@given("calculator is open")
def check_calculator_open():
    print("Calculator is open")

@when("user enters numbers 2 and 3 with + sign between them")
def perform_addition():
    print("performing addition")

@then("the result should be 5")
def check_addition_result():
    a = 2
    b = 3
    result = a+b
    assert result == 5



@given("user enters 10")
def first_number_for_subtraction():
    print("10 entered by user")

@when("user subtracts 5 from it")
def second_number_for_subtraction():
    print("subtracting 5 from 10")

@then("the result should be 5")
def check_subraction_result():
    a = 10
    b = 5
    result = a-b
    assert result == 5







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











pytest.AMT = 0

@given("the account balance is 100")
def curr_balance():
    pytest.AMT = 100

@when("the account holder withdraws 30")
def withdraw_amt():
    pytest.AMT = pytest.AMT - 30

@then("the account balance should be 70")
def final_balance():
    assert pytest.AMT == 70