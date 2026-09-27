import json
import os


DATA_FILE = "tasks.json"


def load_tasks(file_path = DATA_FILE):
    """Read tasks from the JSON file. Return an empty list if the file doesn't exist yet."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # File exists but is empty or corrupted — start fresh instead of crashing
            return []

def save_tasks(tasks, file_path = DATA_FILE):
    """Write the current tasks list to the JSON file."""
    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=4)