def register(username,email):
    if not username:
        return "Username required"
    if "@" not in email:
        return "Invalid email"
    return "Registered"

def test_valid_registration():
    assert register("dhinesh", "d@gmail.com") == "Registered"

def test_empty_username():
    assert register("","d@gmail.com") == "Username required"

def test_invalid_email():
    assert register("dhinesh","invalid") == "Invalid email"

# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ python -m pytest -v tests/validate_a_registered_function.py
# ==================== test session starts =====================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet
# plugins: metadata-3.1.1, html-4.2.0
# collected 3 items                                            

# tests/validate_a_registered_function.py::test_valid_registration PASSED [ 33%]
# tests/validate_a_registered_function.py::test_empty_username PASSED [ 66%]
# tests/validate_a_registered_function.py::test_invalid_email PASSED [100%]

# ===================== 3 passed in 0.02s ======================