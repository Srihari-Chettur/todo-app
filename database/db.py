import sqlite3
import os

def get_db_connection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "todo.db")
    return sqlite3.connect(db_path)

def init_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "todo.db")
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS subjects (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS " \
    "tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, subject_id INTEGER, description TEXT NOT NULL,done INTEGER NOT NULL DEFAULT 0, FOREIGN KEY(subject_id) REFERENCES subjects(id))")
    con.commit()
    return con