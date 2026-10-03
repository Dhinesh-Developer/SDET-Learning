import pytest

@pytest.mark.smoke
def test_health_endpoint(api, base_url):
    response = api.get(
        f"{base_url}/health",
        timeout=5
    )
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}

@pytest.mark.smoke
def test_create_and_get_user(api, base_url, unique_user):
    response = api.post(
        f"{base_url}/users",
        json = unique_user,
        timeout=5
    )       

    assert response.status_code == 201
    user = response.json()

    assert user["name"] == unique_user["name"]
    assert user["email"] == unique_user["email"]

    get_response = api.get(
        f"{base_url}/users/{user['id']}",
        timeout=5
    )

    assert get_response.status_code == 200
    assert get_response.json() == user

    delete_response = api.delete(
        f"{base_url}/users/{user['id']}",
        timeout=5
    )

    assert delete_response.status_code == 200

@pytest.mark.regression
def test_update_user(api, base_url, created_user):
    payload = {
        "name" : "Updated user",
        "email": " updated-"+created_user["email"]
    }    

    response = api.put(
        f"{base_url}/users/{created_user['id']}",
        json=payload,
        timeout=5
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"
    assert response.json()["email"] == payload["email"]


@pytest.mark.negative
@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"name":"","email":"valid@example.test"},
        {"name":"Dhinesh","email":"invalid"},
        {"name":"Dhinesh", "email":""},
    ]
)
def test_invalid_user_creation(api, base_url, payload):
    response = api.post(
        f"{base_url}/users",
        json = payload,
        timeout = 5
    )

    assert response.status_code == 400
    assert "error" in response.json()

@pytest.mark.negative
def test_nonexistent_user(api, base_url):
    response = api.get(
        f"{base_url}/users/99999999",
        timeout=5
    )

    assert response.status_code == 404
    assert response.json()["error"] == "User not found"


@pytest.mark.regression
def test_delete_user(api, base_url, created_user):
    response = api.delete(
        f"{base_url}/users/{created_user['id']}",
        timeout=5
    )

    assert response.status_code == 200

    get_response = api.get(
        f"{base_url}/users/{created_user['id']}",
        timeout=5
    )

    assert get_response.status_code == 404  



