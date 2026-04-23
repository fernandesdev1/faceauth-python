import sqlite3

def connect():
    return sqlite3.connect("data/users.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        face_encoding BLOB
    )
    """)

    conn.commit()
    conn.close()