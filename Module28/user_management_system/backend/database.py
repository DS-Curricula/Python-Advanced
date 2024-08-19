import sqlite3
from passlib.context import CryptContext

DATABASE_NAME = "users.db"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def seed_users():
    conn = get_db_connection()
    try:
        # Hash the passwords before storing them
        admin_password = pwd_context.hash("adminpass")
        user_password = pwd_context.hash("userpass")

        conn.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', ('admin', admin_password, 'admin'))
        conn.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', ('user', user_password, 'user'))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Users already exist
    conn.close()

# Initialize and seed the database when the app starts
init_db()
seed_users()
