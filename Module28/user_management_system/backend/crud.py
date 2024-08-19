from backend.auth import hash_password
from backend.database import get_db_connection
from backend.models import  UserCreate, UserUpdate

def get_all_users():
    conn = get_db_connection()
    users = conn.execute('SELECT id, username, role FROM users').fetchall()
    conn.close()
    return [dict(user) for user in users]

def get_user_by_username(username: str):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    return user

def create_user(user: UserCreate):
    conn = get_db_connection()
    hashed_password = hash_password(user.password)  # Hash the password
    try:
        conn.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (user.username, hashed_password, user.role))
        conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError("User already exists")
    conn.close()

def update_user(user_id: int, user: UserUpdate):
    conn = get_db_connection()
    conn.execute('UPDATE users SET username = ?, role = ? WHERE id = ?', (user.username, user.role, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id: int):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
