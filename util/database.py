import sqlite3
from typing import Any, List


class SQLiteDatabase:

    def __init__(self, db_name: str) -> None:
        self.db_name = db_name

    def execute(self, query: str, params: tuple[Any, ...] = (), fetch: str = None) -> None | list[Any] | int | Any:
        """Execute an SQL query and return results if applicable."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()

        if fetch == "one":
            return cursor.fetchone() if cursor.description else None
        elif fetch == "all":
            return cursor.fetchall() if cursor.description else []
        return cursor.rowcount

    def create_table(self, table_name: str, column_names: list[str]) -> list[tuple[Any, ...]]:
        """Create a table with the specified columns."""
        columns_definition = ", ".join(column_names)
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition})"
        return self.execute(query)

    def insert(self, table_name: str, column_names: list[str], values: tuple[Any, ...]) -> list[tuple[Any, ...]]:
        """Insert a row into the specified table."""
        placeholders = ", ".join(["?"] * len(values))
        query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({placeholders})"
        return self.execute(query, values)

    def update(self, table_name: str,
               column_names: list[str], column_name: str, values: tuple[Any, ...]) -> list[tuple[Any, ...]]:
        """Update rows in the specified table."""
        columns_definition = "=?, ".join(column_names).join(["", "=?"])
        placeholder = "?"
        query = f"UPDATE {table_name} SET {columns_definition} WHERE {column_name}={placeholder}"
        return self.execute(query, values)

    def delete(self, table_name: str, column_name: str, value: tuple[Any, ...]) -> list[tuple[Any, ...]]:
        """Delete rows from the specified table."""
        placeholder = "?"
        query = f"DELETE FROM {table_name} WHERE {column_name}={placeholder}"
        return self.execute(query, value)

    def select(self, column_names: list,
               table_name: str, column_name: str, value: tuple[Any, ...], fetch: str) -> list[tuple[Any, ...]]:
        """Select rows from the specified table."""
        columns = ", ".join(column_names)
        placeholder = "?"
        query = f"SELECT {columns} FROM {table_name} WHERE {column_name}={placeholder}"
        return self.execute(query, value, fetch)

    # TODO: Verify values being passed as tuples
