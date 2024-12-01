import sqlite3
import pandas as pd
import os

# Define the database path
DATABASE_PATH = "data/merged_data.db"

# Utility: Connect to SQLite database
def connect_db():
    """
    Establish a connection to the SQLite database.
    If the database does not exist, it will be created.
    """
    if not os.path.exists(DATABASE_PATH):
        os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

# Utility: Create required tables
def create_tables():
    """
    Create tables in the SQLite database if they do not exist.
    """
    conn = connect_db()
    cursor = conn.cursor()

    # Create density_table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS density_table (
        census_tract TEXT PRIMARY KEY,
        branch_count INTEGER,
        PM25 REAL
    )
    """)
    conn.commit()
    conn.close()

# Utility: Populate the database
def populate_data(density_df: pd.DataFrame):
    """
    Populate the SQLite database with data.
    :param density_df: DataFrame containing 'census_tract', 'branch_count', and 'PM25' columns
    """
    conn = connect_db()
    density_df.to_sql('density_table', conn, if_exists='replace', index=False)
    conn.close()

# Utility: Query data from the database
def query_data(query: str, params=None):
    """
    Query data from the SQLite database.
    :param query: SQL query string
    :param params: Query parameters (optional)
    :return: DataFrame containing the query results
    """
    conn = connect_db()
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df

# Utility: Check if the database is initialized
def is_initialized():
    """
    Check if the database has been initialized with required tables.
    :return: Boolean indicating whether tables are initialized
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='density_table';
    """)
    result = cursor.fetchone()
    conn.close()
    return result is not None
