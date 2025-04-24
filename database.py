import sqlite3
import os
import datetime

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
    
def add_expense(date, description, category, amount):
    """
    Adds a new expense record to the database.

    Args:
        date (str): The date of the expense (e.g., 'YYYY-MM-DD').
        description (str): A description of the expense.
        category (str): The category of the expense.
        amount (float): The amount of the expense.

    Returns:
        bool: True if the expense was added successfully, False otherwise.
    """
    conn = get_db_connection()
    if conn is None:
        print("No database connection exists: cannot add expense")
        return False
    
    # SQL command to insert data.
    # Using placeholders (?) is crucial to prevent SQL injection vulnerabilities.
    insert_sql = """
    INSERT INTO expenses (date, description, category, amount)
    VALUES (?, ?, ?, ?);
    """
    try:
        cursor = conn.cursor()
        cursor.execute(insert_sql, (date, description, category, amount))
        conn.commit() # Commit the changes to save them
        print("Successfully added expense")
        return True
    except sqlite3.Error as e:
        print(f"An error occurred adding expense: {e}")
        conn.rollback()
        return False
    finally:
        if conn:
            conn.close()
    
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
    print("-" * 20)
    init_database() # Make sure table exists
    print("-" * 20)

    # --- Test adding an expense ---
    print("Testing add_expense function...")
    today_date = datetime.date.today().strftime('%Y-%m-%d') # Get today's date as YYYY-MM-DD
    description = "Coffee"
    category = "Food & Drink"
    amount = 3.75

    if add_expense(today_date, description, category, amount):
        print(f"Successfully added test expense: {description}")
    else:
        print(f"Failed to add test expense: {description}")

    print("-" * 20)
    # Check if the database file exists
    db_file_path = os.path.join(os.path.dirname(__file__), DATABASE_FILE)
    if os.path.exists(db_file_path):
        print(f"Database file '{DATABASE_FILE}' found.")
    else:
        print(f"Database file '{DATABASE_FILE}' NOT found.")