import pytest
from datetime import datetime, timedelta
from src.models.task import Task

def test_task_initialization_defaults():
    t = Task("Test Task")
    assert t.title == "Test Task"
    assert t.priority == "medium"
    assert t.deadline is None
    assert not t.completed

def test_task_initialization_with_deadline():
    deadline = datetime.now() + timedelta(days=1)
    t = Task("Deadline Task", deadline=deadline)
    assert t.deadline == deadline

def test_set_deadline_with_str():
    t = Task("String Deadline")
    t.set_deadline("2025-09-21 12:00")
    assert t.deadline == datetime(2025, 9, 21, 12, 0)

def test_set_deadline_with_invalid_str():
    t = Task("Bad Deadline")
    with pytest.raises(ValueError):
        t.set_deadline("bad-format")

def test_mark_completed():
    t = Task("Complete Me")
    t.mark_completed()
    assert t.completed

def test_is_overdue_false_if_completed():
    t = Task("Not Overdue", deadline=datetime.now() - timedelta(days=1), completed=True)
    assert not t.is_overdue()

def test_is_overdue_true_if_not_completed_and_past_deadline():
    t = Task("Overdue", deadline=datetime.now() - timedelta(days=1))
    assert t.is_overdue()

def test_to_dict_and_from_dict():
    deadline = datetime(2025, 9, 21, 12, 0)
    t = Task("Dict Task", priority="high", deadline=deadline, completed=True)
    d = t.to_dict()
    assert d["title"] == "Dict Task"
    assert d["priority"] == "high"
    assert d["deadline"] == deadline.isoformat()
    assert d["completed"] is True

    t2 = Task.from_dict(d)
    assert t2.title == t.title
    assert t2.priority == t.priority
    assert t2.deadline == t.deadline
    assert t2.completed == t.completed
