import sqlite3

# Path to your database file
DATABASE_NAME = "users.db"  # Make sure to use the correct path to your database

# Function to connect to the database
def connect_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

# Function to create the 'users' table if it doesn't already exist
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    # Create 'users' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Function to check if the account already exists
def check_account_exists(username):
    conn = connect_db()
    cursor = conn.cursor()

    # Query the 'users' table to see if the username exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    account = cursor.fetchone()
    
    conn.close()

    return account is not None

# Function to create a new account
def create_account(username, password):
    if check_account_exists(username):
        return False  # Account already exists

    conn = connect_db()
    cursor = conn.cursor()

    # Insert the new user's data into the 'users' table
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    return True  # Account created successfully
