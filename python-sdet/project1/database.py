import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "app.db"

def get_connection():
    con = sqlite3.connect(DB_PATH, timeout=10)
    con.row_factory = sqlite3.Row
    return con

def init_db():
    with get_connection() as con:
        con.execute(
            """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
"""
        )

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")



