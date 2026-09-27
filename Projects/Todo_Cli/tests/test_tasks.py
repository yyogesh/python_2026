from todo.tasks import (
    add_task, remove_task, complete_task, get_sorted_tasks, search_tasks, PRIORITY_ORDER
)


def test_add_task_creates_correct_structure():
    tasks = []
    add_task(tasks, "Buy milk", priority="high", due_date="2026-09-10", tags=["errand"])

    assert len(tasks) == 1
    assert tasks[0]["title"] == "Buy milk"
    assert tasks[0]["priority"] == "high"
    assert tasks[0]["due_date"] == "2026-09-10"
    assert tasks[0]["tags"] == ["errand"]
    assert tasks[0]["done"] is False


def test_add_task_defaults():
    tasks = []
    add_task(tasks, "Simple task")

    assert tasks[0]["priority"] == "medium"
    assert tasks[0]["due_date"] is None
    assert tasks[0]["tags"] == []


def test_remove_task_removes_and_returns_correct_item():
    tasks = []
    add_task(tasks, "Task A")
    add_task(tasks, "Task B")

    removed = remove_task(tasks, 1)  # remove "Task A" (1-indexed)

    assert removed["title"] == "Task B"
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Task A"


def test_remove_task_invalid_index_returns_none():
    tasks = []
    add_task(tasks, "Task A")

    result = remove_task(tasks, 5)  # out of range

    assert result is None
    assert len(tasks) == 1  # nothing was removed


def test_complete_task_marks_done_and_returns_it():
    tasks = []
    add_task(tasks, "Task A")

    completed = complete_task(tasks, 1)

    assert completed["done"] is True
    assert tasks[0]["done"] is True


def test_priority_order_values():
    assert PRIORITY_ORDER["high"] < PRIORITY_ORDER["medium"] < PRIORITY_ORDER["low"]


def test_get_sorted_tasks_by_priority():
    tasks = []
    add_task(tasks, "Low task", priority="low")
    add_task(tasks, "High task", priority="high")

    sorted_tasks = get_sorted_tasks(tasks, sort_by="priority")

    assert sorted_tasks[0]["title"] == "High task"
    assert sorted_tasks[1]["title"] == "Low task"


def test_get_sorted_tasks_does_not_mutate_original_list():
    tasks = []
    add_task(tasks, "Low task", priority="low")
    add_task(tasks, "High task", priority="high")

    get_sorted_tasks(tasks, sort_by="priority")

    # the original list's order should be untouched
    assert tasks[0]["title"] == "Low task"
    assert tasks[1]["title"] == "High task"


def test_search_tasks_matches_title():
    tasks = []
    add_task(tasks, "Buy milk")
    add_task(tasks, "Walk the dog")

    results = search_tasks(tasks, "milk")

    assert len(results) == 1
    assert results[0]["title"] == "Buy milk"


def test_search_tasks_matches_tags():
    tasks = []
    add_task(tasks, "Finish report", tags=["work", "urgent"])
    add_task(tasks, "Buy milk", tags=["errand"])

    results = search_tasks(tasks, "urgent")

    assert len(results) == 1
    assert results[0]["title"] == "Finish report"


def test_search_tasks_is_case_insensitive():
    tasks = []
    add_task(tasks, "Buy Milk")

    results = search_tasks(tasks, "MILK")

    assert len(results) == 1


def test_search_tasks_returns_empty_list_when_no_match():
    tasks = []
    add_task(tasks, "Buy milk")

    results = search_tasks(tasks, "nonexistent")

    assert results == []
