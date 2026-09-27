from todo.storage import load_tasks, save_tasks

def test_load_tasks_returns_empty_list_when_file_missing(tmp_path):
    """tmp_path is a built-in pytest fixture: a fresh temp directory for this test only."""

    fake_file = tmp_path / "does_not_exist.json"

    result = load_tasks(str(fake_file))

    assert result == []


def test_save_and_load_round_trip(tmp_path):
    # tmp_path is another built-in pytest fixture: a real, unique, temporary directory (a pathlib.Path object)
    #  created fresh for each test, and automatically cleaned up afterward.
    fake_file = tmp_path / "tasks.json"

    original_tasks = [
        {"title": "Test task", "done": False, "priority": "high", "due_date": None}
    ]

    save_tasks(original_tasks, str(fake_file))

    loaded_tasks = load_tasks(str(fake_file))

    assert loaded_tasks == original_tasks



def test_load_tasks_handles_corrupted_file(tmp_path):
    fake_file = tmp_path / "broken.json"
    fake_file.write_text("this is not valid json {{{")

    result = load_tasks(str(fake_file))

    assert result == []