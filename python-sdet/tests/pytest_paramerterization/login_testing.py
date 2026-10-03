import pytest

@pytest.mark.parametrize(
    "username,password,excepted",
    [
        ("admin","admin123",True),
        ("admin","wrong",False),
        ("guest","guest123", False),
        ("","",False),
    ]
)

def test_login(username, password, excepted):
    valid = (
        username == "admin"
        and password == "admin123"
    )
    assert valid == excepted


#  python -m pytest -q pytest_paramerterization/login_testing.py
# ....                                                      [100%]
# 4 passed in 0.04s