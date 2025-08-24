import pytest


@pytest.mark.cart
def test_buy_product(setup_and_teardown):
    print("Ordered the product")


@pytest.mark.cart
def test_remove_product(setup_and_teardown):
    print("Removed the product")