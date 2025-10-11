# 代码生成时间: 2025-10-12 02:52:26
import pandas as pd
import sqlite3
from contextlib import closing
"""
Database Version Control System using Python and Pandas.
This script allows for versioning of database schema changes.
"""

class DatabaseVersionControl:
    """
    A class to handle database version control.
    """
    def __init__(self, db_name):
        """
        Initialize the DatabaseVersionControl class.
        :param db_name: The name of the SQLite database file.
        """
        self.db_name = db_name
        self.conn = None

    def connect(self):
        """
        Establish a connection to the SQLite database.
        """
        try:
            self.conn = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def close(self):
        """
        Close the connection to the database.
        """
        if self.conn:
            self.conn.close()

    def create_version_table(self):
        """
        Create a table to store version information.
        """
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS version_control (
                    version INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT,
                    executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def get_current_version(self):
        """
        Get the current database version.
        """
        with closing(self.conn.cursor()) as cursor:
            cursor.execute("SELECT version FROM version_control ORDER BY version DESC LIMIT 1")
            result = cursor.fetchone()
            return result[0] if result else None

    def record_version(self, description):
        """
        Record a new version in the version_control table.
        :param description: A description of the schema change.
        """
        with self.conn:
            self.conn.execute("INSERT INTO version_control (description) VALUES (?)", (description,))

    def apply_migration(self, migration_func):
        """
        Apply a migration function to the database.
        :param migration_func: A function that performs the migration.
        """
        try:
            migration_func(self.conn)
            self.record_version(migration_func.__name__)
        except Exception as e:
            print(f"Migration failed: {e}")

# Example usage
if __name__ == '__main__':
    dbc = DatabaseVersionControl('example.db')
    dbc.connect()
    dbc.create_version_table()

    # Define a migration function
    def add_user_table():
        """
        Create a new users table.
        """
        with dbc.conn:
            dbc.conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")

    # Apply the migration
    dbc.apply_migration(add_user_table)
    dbc.close()