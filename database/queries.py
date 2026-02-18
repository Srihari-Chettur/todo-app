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

def delete_subject(subject_id):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM tasks WHERE subject_id = ?", (subject_id,))
    cur.execute("DELETE FROM subjects WHERE id = ?", (subject_id,))
    con.commit()
    con.close()

def add_task(subject_id, description, due_date=None):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO tasks (subject_id, description, done, due_date) VALUES (?, ?, 0, ?)", (subject_id, description, due_date))
    con.commit()
    con.close()

def get_tasks_by_subject(subject_id):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT id, description, done, due_date FROM tasks WHERE subject_id = ?", (subject_id,))
    rows = cur.fetchall()
    con.close()
    return [Task(id=row[0], title="", subject_id=subject_id, done=bool(row[2]), description=row[1], due_date=row[3]) for row in rows]                   

def toggle_task_done(task_id):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT done FROM tasks WHERE id = ?", (task_id,))
    row = cur.fetchone()
    cur.execute("UPDATE tasks SET done = ? WHERE id = ?", (0 if row[0] else 1, task_id))
    con.commit()
    con.close()

def delete_task(task_id):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    con.commit()
    con.close()