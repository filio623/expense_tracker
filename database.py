import sqlite3
import os

DATABASE_FILE = "expenses.db"

def get_db_connection():
    """
    Establishes a connection to the SQLite database file.
    Creates the file if it doesn't exist.

    Returns:c
        sqlite3.Connection: The connection object, or None if connection fails.
    """
    conn = None
    try:
        # Construct the full path to the database file in the current directory
        db_path = os.path.join(os.path.dirname(__file__), DATABASE_FILE)
        print(f"Connecting to database at: {db_path}") # Debug print
        conn = sqlite3.connect(db_path)
        print(f"SQLlite version: {sqlite3.sqlite_version}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    
def create_table(conn):
    """
    Creates the 'expenses' table if it doesn't already exist.

    Args:
        conn (sqlite3.Connection): The database connection object.

    Returns:
        bool: True if table creation was successful or table already exists, False otherwise.
    """
    if conn is None:
        print(f"Cannot create table: No database connection.")
        return False
    
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        description TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL
    );
    """
    try:
        cursor =conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
        print("Table 'expenses' checked/created successfully.")
        return True
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
        return False
    
def init_database():
    """
    Initializes the database: connects and creates the table if necessary.
    """
    print("Initializing database...")
    conn = get_db_connection()
    if conn:
        if create_table(conn):
            print("Database initialization successful.")
        else:
            print("Database initialization Failed.")
        conn.close()
        print("Database connection closed")
    else:
        print("Database initialization failed (connection error).")

        #Test Block
if __name__ == "__main__":
    init_database()
    # You can optionally add code here to check if the expenses.db file
    # was created in the same directory as database.py
    db_file_path = os.path.join(os.path.dirname(__file__), DATABASE_FILE)
    if os.path.exists(db_file_path):
        print(f"Database file '{DATABASE_FILE}' found.")
    else:
        print(f"Database file '{DATABASE_FILE}' NOT found.")