import sqlite3
import os

def get_db_connection(db_name="todo.db"):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, db_name) 
    if not os.path.exists(db_path):
        init_db(db_name)
    return sqlite3.connect(db_path)
def init_db(db_name="todo.db"):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, db_name)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS subjects (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS " \
    "tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, subject_id INTEGER, title TEXT NOT NULL,done INTEGER NOT NULL DEFAULT 0, due_date TEXT, FOREIGN KEY(subject_id) REFERENCES subjects(id))")
    con.commit()
    return con