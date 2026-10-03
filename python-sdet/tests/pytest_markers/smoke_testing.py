import pytest 

@pytest.mark.smoke
def test_application_launch():
    assert 1+1 == 2

@pytest.mark.smoke 
def test_login_page():
    assert "login".lower() == "login"

def test_optional_feature():
    assert True



# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet/tests$ python -m pytest -v pytest_markers/smoke_testing.py
# ====================== test session starts ======================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet/tests/pytest_markers
# configfile: pytest.ini
# plugins: metadata-3.1.1, html-4.2.0
# collected 3 items                                               

# pytest_markers/smoke_testing.py::test_application_launch PASSED [ 33%]
# pytest_markers/smoke_testing.py::test_login_page PASSED   [ 66%]
# pytest_markers/smoke_testing.py::test_optional_feature PASSED [100on%]

# ======================= 3 passed in 0.01s =======================