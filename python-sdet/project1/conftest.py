import logging
import uuid
from pathlib import Path

import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/api_tests.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    force=True
)

logger = logging.getLogger("api_tests")

@pytest.fixture
def api():
    session = requests.Session()
    yield session
    session.close()

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def unique_user():
    return {
        "name": "Test User",
        "email": f"user-{uuid.uuid4().hex}@example.test"
    }    

@pytest.fixture
def created_user(api, base_url, unique_user):
    response = api.post(
        f"{BASE_URL}/users",
        json=unique_user,
        timeout=5
    )

    assert response.status_code == 201, response.text
    user = response.json()

    yield user

    cleanup = api.delete(
        f"{base_url}/users/{user['id']}",
        timeout=5
    )
    assert cleanup.status_code in (200, 404)

@pytest.fixture(autouse=True)
def log_test(request):
    logger.info("START: %s", request.node.nodeid)
    yield
    logger.info("FINISH: %s", request.node.nodeid)    



