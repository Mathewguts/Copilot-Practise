import sqlite3
from typing import Any


def lookup_user_by_name(
    connection: sqlite3.Connection, name: str
) -> tuple[Any, ...] | None:
    """Return the first user whose name exactly matches, or None if not found.

    Expects a `users` table with a `name` column. The name is passed as a
    parameter so it is treated as data, not SQL.
    """
    cursor = connection.execute(
        "SELECT * FROM users WHERE name = ? LIMIT 1",
        (name,),
    )
    return cursor.fetchone()
