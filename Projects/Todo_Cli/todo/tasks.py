# Lower number = higher urgency, so "high" tasks show up first.
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}

def add_task(tasks, title, priority="medium", due_date=None, tags=None):
    """Add a new task with an optional priority, due date, and tags."""
    tasks.append({
        "title": title,
        "done": False,
        "priority": priority,
        "due_date": due_date,
        "tags": tags or [],
    })


def get_sorted_tasks(tasks, sort_by=None):
    """Return a NEW list of tasks, optionally sorted. Does not modify the original list."""
    if sort_by == "priority":
        return sorted(tasks, key=lambda t: PRIORITY_ORDER.get(t["priority"], 1))
    elif sort_by == "due_date":
        return sorted(tasks, key=lambda t: t["due_date"] or "9999-99-99")
    return tasks

def search_tasks(tasks, keyword):
    """Return tasks whose title or tags contain the keyword (case-insensitive)."""
    keyword = keyword.lower()
    return [
        t for t in tasks
        if keyword in t["title"].lower()
        or any(keyword in tag.lower() for tag in t.get("tags", []))
    ]



# def list_tasks(tasks, sort_by=None):
#     """List tasks, optionally sorted by 'priority' or 'due_date'."""
#     if not tasks:
#         print("No tasks yet!")
#         return

#     task_to_show = tasks

#     if sort_by == "priority":
#         tasks.sort(key=lambda task: PRIORITY_ORDER[task["priority"]], reverse=True)

#         # task_to_show = sorted(tasks, key=lambda task: PRIORITY_ORDER[task["priority"]], reverse=True)
#     elif sort_by == "due_date":
#         tasks.sort(key=lambda task: task["due_date"])

#     for index, task in enumerate(tasks):
#         status = "✔" if task["done"] else "✗"
#         print(f"{index}. [{status}] {task['title']} — priority: {task['priority']}, due: {task['due_date'] or 'none'}")


def remove_task(tasks, index):
    """Remove a task and return it, or return None if the index was invalid."""
    if index < 0 or index >= len(tasks):
        print("Invalid index.")
        return None

    return tasks.pop(index)
   # print(f"Removed: {task['title']}")


def complete_task(tasks, index):
    """Mark a task done and return it, or return None if the index was invalid."""
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        return tasks[index - 1]
    return None