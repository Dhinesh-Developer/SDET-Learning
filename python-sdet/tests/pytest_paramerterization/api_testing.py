import pytest
import requests

@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        (1, 200),
        (2, 200),
        (9999, 404)
    ]
)

def test_get_user(user_id, expected_status):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",timeout=10
    )
    assert response.status_code == expected_status


# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet/tests$ python -m pytest -v pytest_paramerterization/api_testing.py
# ====================== test session starts ======================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet/tests
# plugins: metadata-3.1.1, html-4.2.0
# collected 3 items                                               

# pytest_paramerterization/api_testing.py::test_get_user[1-200] PASSED [ 33%]
# pytest_paramerterization/api_testing.py::test_get_user[2-200] PASSED [ 66%]
# pytest_paramerterization/api_testing.py::test_get_user[9999-404]PASSED [100%]

# ======================= 3 passed in 1.15s =======================