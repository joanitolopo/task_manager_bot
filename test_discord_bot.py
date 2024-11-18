import unittest
import sqlite3
from database import (
    init_database,
    add_task_db,
    delete_task_db,
    show_tasks_db,
    complete_task_db,
    check_task_exists,
    check_tasks_exist_noid,
)

TEST_DB_NAME = "tasks.db"

# Override DB_NAME for testing
DB_NAME = TEST_DB_NAME


class TestTaskDatabase(unittest.TestCase):
    def setUp(self):
        """Initialize the test database before each test."""
        global DB_NAME
        DB_NAME = TEST_DB_NAME
        init_database()

    def tearDown(self):
        """Clean up the test database after each test."""
        conn = sqlite3.connect(TEST_DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS tasks")
        conn.commit()
        conn.close()

    def test_init_database(self):
        """Test if the database is initialized successfully."""
        conn = sqlite3.connect(TEST_DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'")
        table = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(table, "Table 'tasks' should exist after initialization.")

    def test_add_task_db(self):
        """Test adding a task to the database."""
        description = "Test task"
        info = add_task_db(description)
        self.assertIn(description, info, "The task description should be included in the response.")
        
        conn = sqlite3.connect(TEST_DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT description FROM tasks WHERE description=?", (description,))
        task = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(task, "The task should be added to the database.")

    def test_delete_task_db(self):
        """Test deleting a task from the database."""
        add_task_db("Task to delete")
        conn = sqlite3.connect(TEST_DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM tasks WHERE description='Task to delete'")
        task_id = cursor.fetchone()[0]
        conn.close()

        info = delete_task_db(task_id)
        self.assertIn(str(task_id), info, "The response should include the task ID.")
        
        conn = sqlite3.connect(TEST_DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
        task = cursor.fetchone()
        conn.close()
        self.assertIsNone(task, "The task should be removed from the database.")

    def test_show_tasks_db(self):
        """Test retrieving all tasks."""
        add_task_db("Task 1")
        add_task_db("Task 2")
        tasks = show_tasks_db()
        self.assertEqual(len(tasks), 2, "There should be two tasks in the database.")
        self.assertEqual(tasks[0]["Description"], "Task 1")
        self.assertEqual(tasks[1]["Description"], "Task 2")

    def test_complete_task_db(self):
        """Test marking a task as completed."""
        add_task_db("Task to complete")
        conn = sqlite3.connect(TEST_DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM tasks WHERE description='Task to complete'")
        task_id = cursor.fetchone()[0]
        conn.close()

        info = complete_task_db(task_id)
        self.assertIn(str(task_id), info, "The response should include the task ID.")
        
        conn = sqlite3.connect(TEST_DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT completed FROM tasks WHERE id=?", (task_id,))
        status = cursor.fetchone()[0]
        conn.close()
        self.assertEqual(status, 1, "The task should be marked as completed.")

    def test_check_task_exists(self):
        """Test checking if a task exists."""
        add_task_db("Existing task")
        conn = sqlite3.connect(TEST_DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM tasks WHERE description='Existing task'")
        task_id = cursor.fetchone()[0]
        conn.close()

        self.assertTrue(check_task_exists(task_id), "The task should exist in the database.")
        self.assertFalse(check_task_exists(9999), "A non-existent task ID should return False.")

    def test_check_tasks_exist_noid(self):
        """Test checking if any tasks exist in the database."""
        self.assertFalse(check_tasks_exist_noid(), "There should be no tasks initially.")
        add_task_db("Sample task")
        self.assertTrue(check_tasks_exist_noid(), "There should be tasks in the database after adding one.")


if __name__ == "__main__":
    unittest.main()
