import pytest


def test_logout():
    print("Logout successfully")


@pytest.mark.parametrize("a, b, sum", [(1, 2, 3), (4, 2, 6), (3, 3, 9)])
@pytest.mark.calculator
def test_sum(a, b, sum):
    assert a + b == sum