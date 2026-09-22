def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    print(f"Added: {title}")


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return

    for index, task in enumerate(tasks):
        status = "✔" if task["done"] else "✗"
        print(f"{index}. [{status}] {task['title']}")


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