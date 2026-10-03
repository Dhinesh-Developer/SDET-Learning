import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_update_user():
    response = requests.put(
        f"{BASE_URL}/users/1",
        json={
            "id":1,
            "name":"Dhinesh Updated",
            "email":"updated@example.com"
        },
        timeout=10
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Dhinesh Updated"

def test_delete_user():
    response = requests.delete(
        f"{BASE_URL}/users/1",
        timeout=10
    )
    assert response.status_code == 200

# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ python -m pytest -v apitesting/put_delete.py
# ====================== test session starts ======================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet
# plugins: metadata-3.1.1, html-4.2.0
# collected 2 items                                               

# apitesting/put_delete.py::test_update_user PASSED         [ 50%]
# apitesting/put_delete.py::test_delete_user PASSED         [100%]

# ======================= 2 passed in 2.05s =======================



