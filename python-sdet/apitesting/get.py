import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user():
    response = requests.get(
        f"{BASE_URL}/users/1",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] != ""
    assert "email" in data
    assert response.headers["Content-Type"].startswith(
        "application/json"
    )

# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ python -m pytest -v apitesting/get.py
# ====================== test session starts ======================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet
# plugins: metadata-3.1.1, html-4.2.0
# collected 1 item                                                

# apitesting/get.py::test_get_user PASSED                   [100%]

# ======================= 1 passed in 0.93s =======================