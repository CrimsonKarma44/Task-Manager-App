import pytest
from src.models.task import Task
from src.models.taskmanager import TaskManager

class DummyFileOps:
    """Dummy file operations to avoid actual disk I/O."""
    def __init__(self):
        self.data = []

    def ensure_json_file(self, filepath):
        pass

    def read_json_file(self, filepath):
        return self.data

    def write_json_file(self, filepath, data):
        self.data = data

@pytest.fixture
def patch_file_ops(monkeypatch):
    dummy = DummyFileOps()
    monkeypatch.setattr("src.models.taskmanager.ensure_json_file", dummy.ensure_json_file)
    monkeypatch.setattr("src.models.taskmanager.read_json_file", dummy.read_json_file)
    monkeypatch.setattr("src.models.taskmanager.write_json_file", dummy.write_json_file)
    return dummy

@pytest.fixture
def manager(patch_file_ops):
    return TaskManager("dummy.json")

@pytest.fixture
def sample_tasks():
    t1 = Task("Task 1")
    t2 = Task("Task 2", completed=True)
    t3 = Task("Task 3", priority="High")
    return t1, t2, t3

def test_add_task(manager, sample_tasks):
    t1, _, _ = sample_tasks
    manager.add_task(t1)
    assert t1 in manager.get_all_tasks()

def test_remove_task(manager, sample_tasks):
    t1, _, _ = sample_tasks
    manager.add_task(t1)
    manager.remove_task(t1)
    assert t1 not in manager.get_all_tasks()

def test_get_all_tasks(manager, sample_tasks):
    for t in sample_tasks:
        manager.add_task(t)
    assert manager.get_all_tasks() == list(manager.tasks)


def test_get_completed_tasks(manager, sample_tasks):
    t1, t2, t3 = sample_tasks
    manager.add_task(t1)
    manager.add_task(t2)
    manager.add_task(t3)
    completed = manager.get_completed_tasks()
    assert t2 in completed
    assert t1 not in completed

def test_get_priority_tasks(manager, sample_tasks):
    t1, t2, t3 = sample_tasks
    manager.add_task(t1)
    manager.add_task(t2)
    manager.add_task(t3)
    high_priority = manager.get_priority_tasks("High")
    assert t3 in high_priority
    assert t1 not in high_priority

def test_clear_tasks(manager, sample_tasks):
    for t in sample_tasks:
        manager.add_task(t)
    manager.clear_tasks()
    assert manager.get_all_tasks() == []

def test_to_json_and_from_json(manager, sample_tasks):
    for t in sample_tasks:
        manager.add_task(t)
    json_str = manager.to_json()
    import json
    parsed = json.loads(json_str)
    assert isinstance(parsed, list)
    assert parsed[0]["title"] == sample_tasks[0].title
    restored = manager.from_json(parsed)
    assert isinstance(restored[0], Task)
    assert restored[0].title == sample_tasks[0].title
