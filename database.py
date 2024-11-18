import sqlite3

DB_NAME = "tasks.db"

def init_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # create table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()
    print(f"INFO: database '{DB_NAME}' initialized successfully!")

def add_task_db(description):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    conn.commit()
    conn.close()

    info_task = f"Task added: {description}"
    return info_task

def delete_task_db(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    info_task = f"Task with ID {task_id} deleted."
    return info_task

def show_tasks_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    description = []
    if not tasks:
        details = {
            "ID": "unavailable",
            "Description": "unavailable",
            "Status": "unavailable"
        }
        description.append(details)
    else:
        for task in tasks:
            status = "completed" if task[2] else "not completed"
            details = {
                "ID": task[0],
                "Description": task[1],
                "Status": status
            }
            description.append(details)
    
    return description
        
def complete_task_db(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    info_task = f"Task with ID {task_id} marked as completed."
    return info_task


def check_task_exists(task_id: int) -> bool:
    """Check if a task with the given task_id exists in the database."""
    conn = sqlite3.connect(DB_NAME)  
    cursor = conn.cursor()
    
    # Query to check if the task exists in the database
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE ID = ?", (task_id,))
    result = cursor.fetchone()
    
    conn.close()
    
    # Return True if the task exists, False otherwise
    return result[0] > 0

def check_tasks_exist_noid() -> bool:
    """Check if there are any tasks in the database."""
    conn = sqlite3.connect('tasks.db')  # Adjust the database path if needed
    cursor = conn.cursor()
    
    # Query to check if there are any tasks in the database
    cursor.execute("SELECT COUNT(*) FROM tasks")
    result = cursor.fetchone()
    
    conn.close()
    
    # Return True if there are tasks in the database, False if there are none
    return result[0] > 0



