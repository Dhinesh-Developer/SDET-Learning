import pytest

@pytest.fixture
def sample_user():
    print("creating test user")
    user = {"name":"Dhinesh","role":"tester"}
    yield user
    print("Clearning up test user")

def test_user_name(sample_user):
    assert sample_user["name"] == "Dhinesh"

def test_user_role(sample_user):
    assert sample_user["role"] == "testing"    


# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ python -m pytest -v tests/fixture_intro.py
# ====================== test session starts ======================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet
# plugins: metadata-3.1.1, html-4.2.0
# collected 2 items                                               

# tests/fixture_intro.py::test_user_name PASSED             [ 50%]
# tests/fixture_intro.py::test_user_role FAILED             [100%]

# =========================== FAILURES ============================
# ________________________ test_user_role _________________________

# sample_user = {'name': 'Dhinesh', 'role': 'tester'}

#     def test_user_role(sample_user):
# >       assert sample_user["role"] == "testing"
# E       AssertionError: assert 'tester' == 'testing'
# E         
# E         - testing
# E         + tester

# tests/fixture_intro.py:14: AssertionError
# --------------------- Captured stdout setup ---------------------
# creating test user
# ------------------- Captured stdout teardown --------------------
# Clearning up test user
# ==================== short test summary info ====================
# FAILED tests/fixture_intro.py::test_user_role - AssertionError: assert 'tester' == 'testing'
# ================== 1 failed, 1 passed in 0.07s ==================
# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$     