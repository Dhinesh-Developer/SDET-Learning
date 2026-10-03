def login(username,password):
    if username == "admin" and password == "admin123":
        return "success"
    return "Invalid credentials"

def test_valid_login():
    assert login("admin","admin123") == "success"

def test_invalid_password():
    assert login("admin","wrong") == "Invalid credentials"

def test_invalid_username():
    assert login("user","admin123") == "Invalid credentials"


# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ python -m pytest -v tests/validate_a_login_function.py
# ==================== test session starts =====================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet
# plugins: metadata-3.1.1, html-4.2.0
# collected 3 items                                            

# tests/validate_a_login_function.py::test_valid_login PASSED [33%]
# tests/validate_a_login_function.py::test_invalid_password PASSED [ 66%]
# tests/validate_a_login_function.py::test_invalid_username PASSED [100%]

# ===================== 3 passed in 0.01s ======================