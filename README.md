# Task Management Discord Bot

This is a simple Discord bot built using Python and `discord.py` for managing tasks. The bot allows you to add, delete, show, and mark tasks as completed. It uses SQLite for storing the tasks and their statuses.

## Features
- **Add Task**: Adds a new task with a description.
- **Delete Task**: Deletes a task by its ID.
- **Show Tasks**: Lists all the tasks with their current status (completed or not).
- **Complete Task**: Marks a task as completed.

## Installation and Setup

### Prerequisites
1. **Python 3.8+** is required.
2. **discord.py** library to interact with the Discord API.
3. **SQLite** for task storage.

### Steps to Set Up

#### 1. Clone this Repository

Clone the repository to your local machine.

```bash
git clone https://github.com/joanitolopo/task-management-bot.git
cd task-management-bot
```

### 2. Install Dependencies
Install the required Python packages using pip.

```bash
pip install -r requirements.txt
```

`requirements.txt` should include discord.py:
```
discord.py>=2.0
```

### 3. Set Up Your Discord Bot Token
- Create a bot on the Discord Developer Portal.
- Obtain the Bot Token and save it in a text file named token.txt in the root directory of your project.

### 4. Database Setup
- The bot will automatically create a database file (tasks.db) if it doesn’t already exist.
- The database contains a table for storing tasks with columns for the task description, completion status, and task ID.

### 5. Run the Bot
Once the setup is complete, you can run the bot with:

```bash
python bot.py
```


## Commands
The bot supports the following commands:
- `!add_task <description>`: Adds a task with the provided description.
- `!delete_task <task_id>`: Deletes a task with the specified task ID.
- `!show_tasks`: Displays all tasks with their status (completed or not).
- `!complete_task <task_id>`: Marks a task as completed.

## Example Usage
- To add a task:
```python
!add_task play_football
```
- To delete a task:
```python
!delete_task 1
```
- To view all tasks:
```python
!show_tasks
```
- To mark a task as completed:
```python
!complete_task 1
```
