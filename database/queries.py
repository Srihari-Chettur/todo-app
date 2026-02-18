from models.subject import Subject
from database.db import get_db_connection
from models.task import Task

def add_subject(name):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO subjects (name) VALUES (?)", (name,))
    con.commit()
    con.close()

def get_all_subjects():
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT id, name FROM subjects")
    rows = cur.fetchall()
    con.close()
    return [Subject(id=row[0], name=row[1]) for row in rows]


    