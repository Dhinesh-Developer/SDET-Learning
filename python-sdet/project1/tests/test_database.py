import sqlite3
import pytest

from database import get_connection

@pytest.mark.regression
def test_api_user_is_saved_in_database(created_user):
    with get_connection() as con:
        row = con.execute(
            "SELECT id, name, email FROM users WHERE id = ?",
            (created_user["id"],)
        ).fetchone()

    assert row is not None
    assert row["name"] == created_user["name"]
    assert row["email"] == created_user["email"]

@pytest.mark.regression
def test_duplicate_email_constraint():
    con = sqlite3.connect(":memory:")

    con.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE
)
""")    
    con.execute(
        "INSERT INTO users(email) VALUES (?)",
        ("test@example.test",)
    )

    with pytest.raises(sqlite3.IntegrityError):
        con.execute(
            "INSERT INTO users(email) VALUES (?)",
            ("test@example.test",)
        )

    con.close()    



