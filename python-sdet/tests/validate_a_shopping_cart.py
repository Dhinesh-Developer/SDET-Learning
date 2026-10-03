def total_price(prices):
    if any(price < 0 for price in prices):
        raise ValueError("Negative price")
    return sum(prices)

def test_cart_total():
    assert total_price([100,200,300]) == 600

def test_empty_cart():
    assert total_price([]) == 0

def test_negative_price():
    import pytest 
    with pytest.raises(ValueError):
        total_price([100,-20])    


# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ python -m pytest -v tests/validate_a_shopping_cart.py
# ==================== test session starts =====================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet
# plugins: metadata-3.1.1, html-4.2.0
# collected 3 items                                            

# tests/validate_a_shopping_cart.py::test_cart_total PASSED [ 33%]
# tests/validate_a_shopping_cart.py::test_empty_cart PASSED [ 66%]
# tests/validate_a_shopping_cart.py::test_negative_price PASSED[100%]

# ===================== 3 passed in 0.01s ======================
