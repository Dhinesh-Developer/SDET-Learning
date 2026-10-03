import sqlite3
import pytest

@pytest.fixture
def db():
    con = sqlite3.connect(":memory:")
    con.execute(
        "CREATE TABLE users (id Integer, name TEXT)"
    )
    yield con
    con.close()

def test_insert_user(db):
    db.execute(
        "INSERT INTO users VALUES (?,?)", (1, "Dhinesh")
    )

    res = db.execute(
        "SELECT name FROM users WHERE id = ?", (1,)
    ).fetchone()

    assert res[0] == "Dhinesh"


# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ python -m pytest -v tests/database_fixture.py
# ====================== test session starts ======================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet
# plugins: metadata-3.1.1, html-4.2.0
# collected 1 item                                                

# tests/database_fixture.py::test_insert_user PASSED        [100%]

# ======================= 1 passed in 0.02s =======================

