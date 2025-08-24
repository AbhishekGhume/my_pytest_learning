import pytest


@pytest.fixture()  # scope = function(default), class, module, package, session          autouse = "True"
def setup_and_teardown(browser_selector):
    if browser_selector == "chrome":
        print("Opening amazon website on chrome")
    elif browser_selector == "ff":
        print("Opening amazon website on fire fox")
    else:
        print("Opening amazon website on edge")
    print("Login to amazon")
    yield
    print("Logout from amazon")
    print("Closing amazon website")



# def setup_and_teardown(request):           # without using extra fixture browser_selector
#     if request.config.getoption("--browser") == "chrome":
#         print("Opening amazon website on chrome")
#     elif request.config.getoption("--browser") == "ff":
#         print("Opening amazon website on fire fox")
#     else:
#         print("Opening amazon website on edge")
#     print("Login to amazon")
#     yield
#     print("Logout from amazon")
#     print("Closing amazon website")


# ---------------------------------------------------


# parameterizing fixtures and functions:
# parameterization means running the same test (or fixture) multiple times with different input values.
# There are 2 ways to do that:

# 1.@pytest.fixture

@pytest.fixture(params=["a", "b", "c"])   # This fixture is used in test login, so for test login for each parameter first that parameter is printed and then that function is executed.
def parem_fixture(request):
    print(request.param)




# 2.@pytest.mark.parametrize
# In this type we are passing parameters through markers. This is used in test_logout.py file in test_sum function



# ----------------------------------------------------



# addoption hook
# # pytest_addoption is a special pytest hook used to define custom CLI options.

def pytest_addoption(parser):
    # parser.addoption("--browser")
    parser.addoption("--browser", action="store", default="chrome")





# This fixture retrieves the value of the --browser option at runtime.
# request.config.getoption("--browser") fetches the browser value provided via CLI.

@pytest.fixture()
def browser_selector(request):
    return request.config.getoption("--browser")