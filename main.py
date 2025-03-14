import sqlite3
from contextlib import closing

db_path = "test.db"

try:
    with closing(sqlite3.connect(db_path)) as db_conn:
        db_conn.row_factory = sqlite3.Row
        with closing(db_conn.cursor()) as cursor:
            try:
                query_1 = "SELECT * FROM demo WHERE id > 14"
                cursor.execute(query_1)
                rows = cursor.fetchall()  # Fetching all rows
                print("Names of rows with id > 14")
                for row in rows:
                    print(row["name"])
            except Exception as e:
                print(f"Error executing query 1: {e}")
except sqlite3.Error as e:
    print(f"Database Connection Error: {e}")
