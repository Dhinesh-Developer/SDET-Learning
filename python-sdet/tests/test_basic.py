def add(a,b):
    return a+b

def test_addition():
    assert add(10,20) == 30

def test_addition_with_zero():
    assert add(10,0) == 10

def test_addition_with_negative():
    assert add(-5,10) == 5    


# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ python -m pytest -v tests/test_basic.py
# ==================== test session starts =====================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet
# plugins: metadata-3.1.1, html-4.2.0
# collected 3 items                                            

# tests/test_basic.py::test_addition PASSED              [ 33%]
# tests/test_basic.py::test_addition_with_zero PASSED    [ 66%]
# tests/test_basic.py::test_addition_with_negative PASSED [100%]

# ===================== 3 passed in 0.02s ======================