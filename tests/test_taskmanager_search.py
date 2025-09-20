import pytest
from src.models.taskmanager import TaskManager
from src.models.task import Task

@pytest.fixture
def manager(tmp_path, monkeypatch):
    # Patch file ops to avoid disk I/O
    class DummyFileOps:
        def __init__(self):
            self.data = []
        def ensure_json_file(self, filepath):
            pass
        def read_json_file(self, filepath):
            return self.data
        def write_json_file(self, filepath, data):
            self.data = data
    dummy = DummyFileOps()
    monkeypatch.setattr("src.models.taskmanager.ensure_json_file", dummy.ensure_json_file)
    monkeypatch.setattr("src.models.taskmanager.read_json_file", dummy.read_json_file)
    monkeypatch.setattr("src.models.taskmanager.write_json_file", dummy.write_json_file)
    return TaskManager("dummy.json")

def test_search_tasks_regex(manager):
    t1 = Task("Buy groceries")
    t2 = Task("Call Alice")
    t3 = Task("Email Bob")
    t4 = Task("Buy milk")
    manager.add_task(t1)
    manager.add_task(t2)
    manager.add_task(t3)
    manager.add_task(t4)
    # Search for tasks containing 'Buy'
    results = manager.search_tasks(r"Buy")
    assert t1 in results
    assert t4 in results
    assert t2 not in results
    assert t3 not in results
    # Search for tasks ending with 'Bob'
    results = manager.search_tasks(r"Bob$")
    assert t3 in results
    assert t1 not in results
    assert t2 not in results
    assert t4 not in results
    # Case-insensitive search
    results = manager.search_tasks(r"call")
    assert t2 in results
    # No match
    results = manager.search_tasks(r"xyz")
    assert results == []
