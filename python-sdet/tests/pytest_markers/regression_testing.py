import pytest

@pytest.mark.regression
def test_add_to_cart():
    cart = [100,200]
    assert sum(cart) == 300

@pytest.mark.regression
def test_remove_from_cart():
    cart = [100,200]
    cart.remove(100)
    assert cart == [200]


