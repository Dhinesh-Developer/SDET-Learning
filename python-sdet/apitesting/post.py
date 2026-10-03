import requests

def test_create_user():
    payload = {
        "name":"Dhinesh",
        "username":"dhinesh",
        "email":"dhinesh@example.com"
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=payload,
        timeout=10
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Dhinesh"
    assert data["email"] == "dhinesh@example.com"
    assert "id" in data


# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ python -m pytest -v apitesting/post.py
# ====================== test session starts ======================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet
# plugins: metadata-3.1.1, html-4.2.0
# collected 1 item                                                

# apitesting/post.py::test_create_user PASSED               [100%]

# ======================= 1 passed in 1.06s =======================