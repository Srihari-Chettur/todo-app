from database.db import get_db_connection, init_db
import os
import sqlite3
from database.queries import add_subject, get_all_subjects, delete_subject, add_task, get_tasks_by_subject, toggle_task_done
import pytest
import gc

TEST_DB = "test_todo.db"

@pytest.fixture(autouse=True)
def setup_teardown():
    """Runs before and after each test"""
    # Setup: create fresh test database
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    # You'll need to init tables here or modify your code to use TEST_DB
    
    yield  # test runs here
    
    # Teardown: clean up
    gc.collect()  # Ensure all connections are closed
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

def test_add_and_get_subjects():
    add_subject("Math",TEST_DB)
    subjects = get_all_subjects(TEST_DB)
    assert len(subjects) == 1
    assert subjects[0].name == "Math"

def test_add_and_get_tasks():
    add_subject("Math",TEST_DB)
    subjects = get_all_subjects(TEST_DB)
    add_task(subjects[0].id, "Do homework", "2026-03-01", TEST_DB)
    tasks = get_tasks_by_subject(subjects[0].id, db_name=TEST_DB)
    assert len(tasks) == 1
    assert tasks[0].title == "Do homework"