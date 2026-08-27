import sqlite3
from pathlib import Path


class Memory:
    """Small local SQLite-backed memory store for history and settings."""

    def __init__(self, db_path: str = "data/nova.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                command TEXT NOT NULL,
                response TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            )
            """
        )
        conn.commit()
        conn.close()

    def add_history(self, command: str, response: str):
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO history (command, response) VALUES (?, ?)",
            (command, response),
        )
        conn.commit()
        conn.close()

    def get_history(self):
        conn = sqlite3.connect(self.db_path)
        rows = conn.execute("SELECT id, command, response, created_at FROM history ORDER BY id DESC").fetchall()
        conn.close()
        return rows

    def clear_history(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("DELETE FROM history")
        conn.commit()
        conn.close()

    def set_setting(self, key: str, value: str):
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO settings (key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
            (key, value),
        )
        conn.commit()
        conn.close()

    def get_setting(self, key: str, default: str = "") -> str:
        conn = sqlite3.connect(self.db_path)
        row = conn.execute("SELECT value FROM settings WHERE key = ?", (key,)).fetchone()
        conn.close()
        return row[0] if row else default

    def clear_all(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("DELETE FROM history")
        conn.execute("DELETE FROM settings")
        conn.commit()
        conn.close()
