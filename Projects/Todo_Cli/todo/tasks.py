# Lower number = higher urgency, so "high" tasks show up first.
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}

def add_task(tasks, title, priority="medium", due_date=None):
    """Add a new task with an optional priority and due date."""
    tasks.append({"title": title, "done": False, "priority": priority, "due_date": due_date})
    print(f"Added: {title} (priority: {priority}, due: {due_date or 'none'})")


def list_tasks(tasks, sort_by=None):
    """List tasks, optionally sorted by 'priority' or 'due_date'."""
    if not tasks:
        print("No tasks yet!")
        return

    task_to_show = tasks

    if sort_by == "priority":
        tasks.sort(key=lambda task: PRIORITY_ORDER[task["priority"]], reverse=True)

        # task_to_show = sorted(tasks, key=lambda task: PRIORITY_ORDER[task["priority"]], reverse=True)
    elif sort_by == "due_date":
        tasks.sort(key=lambda task: task["due_date"])

    for index, task in enumerate(tasks):
        status = "✔" if task["done"] else "✗"
        print(f"{index}. [{status}] {task['title']} — priority: {task['priority']}, due: {task['due_date'] or 'none'}")


def remove_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Invalid index.")
        return

    task = tasks.pop(index)
    print(f"Removed: {task['title']}")


def complete_task(tasks, index):
    """mark a task as done."""
    if index < 0 or index >= len(tasks):
        print("Invalid index.")
        return

    print(f"Marked as done: {tasks[index - 1]['title']}")
    tasks[index]["done"] = True