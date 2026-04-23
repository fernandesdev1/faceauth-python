import sqlite3
import os

DB_PATH = "data/users.db"

def connect():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)


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