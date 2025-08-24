import pytest

age = 16

@pytest.mark.smoke
def test_login(parem_fixture):
    print("Logged in successfully")

@pytest.mark.skipif(age<18, reason="You are under age!!")
def test_age():
    assert age>18