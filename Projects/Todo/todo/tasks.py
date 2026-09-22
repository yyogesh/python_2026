
from asyncio import tasks


PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}

def add_task(tasks, title, priority="medium", due_date=None):
    task = {"title": title, "done": False, "priority": priority, "due_date": due_date}
    tasks.append(task)


def list_tasks(tasks, sort_by = None):
    """List tasks, optionally sorted by 'priority' or 'due_date'."""
    if not tasks:
        print("No tasks available.")
        return

    tasks_to_show = tasks

    if sort_by == "priority":
        tasks_to_show =sorted(tasks, key=lambda x: PRIORITY_ORDER.get(x["priority"], 1))
    elif sort_by == "due_date":
        tasks_to_show = sorted(tasks, key=lambda x: x["due_date"] or "9999-99-99")

    for index, task in enumerate(tasks_to_show, start=1):
        status = "✔" if task["done"] else "✗"
        due = task.get("due_date", "No due date")
        print(f"{index}. [{status}] {task['title']} — priority: {task['priority']}, due: {due}")


def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Removed task: {removed_task['title']}")
    else:
        print("Invalid task index.")


def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print(f"Marked task as done: {tasks[index]['title']}")
    else:
        print("Invalid task index.")