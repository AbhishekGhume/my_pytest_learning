# from pytest_bdd import scenario, scenarios, given, when, then
# import pytest

# scenarios("../features/transaction.feature")


# pytest.AMT = 0

# @given("the account balance is 100")
# def curr_balance():
#     pytest.AMT = 100

# @when("the account holder withdraws 30")
# def withdraw_amt():
#     pytest.AMT = pytest.AMT - 30

# @then("the account balance should be 70")
# def final_balance():
#     assert pytest.AMT == 70