import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    """Read tasks from the JSON file. Return an empty list if the file doesn't exist yet."""

    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        try:
            tasks = json.load(file)
            return tasks
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    """Write the current tasks list to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file)