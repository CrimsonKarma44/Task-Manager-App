import unittest
from src.models.task import Task
from datetime import datetime

class TestTask(unittest.TestCase):
    def test_init(self):
        task = Task("Test Task", priority="High", completed=True)
        self.assertEqual(task.title, "Test Task")
        self.assertTrue(task.priority)
        self.assertTrue(task.completed)
        self.assertIsNone(task.deadline)

    def test_set_deadline_str(self):
        task = Task("Deadline Task")
        task.set_deadline("2025-09-18 12:00")
        self.assertIsNotNone(task.deadline)
        self.assertIsInstance(task.deadline, datetime)
      #   self.assertEqual(task.deadline.year, 2025)

    def test_set_deadline_datetime(self):
        dt = datetime(2025, 9, 18, 12, 0)
        task = Task("Deadline Task", deadline=dt)
        self.assertEqual(task.deadline, dt)

    def test_set_deadline_invalid(self):
        task = Task("Invalid Deadline")
        with self.assertRaises(ValueError):
            task.set_deadline("invalid-date")

    def test_mark_completed(self):
        task = Task("Incomplete Task")
        self.assertFalse(task.completed)
        task.mark_completed()
        self.assertTrue(task.completed)

    def test_to_dict(self):
        dt = datetime(2025, 9, 18, 12, 0)
        task = Task("Dict Task", priority="High", deadline=dt, completed=True)
        d = task.to_dict()
        self.assertEqual(d["name"], "Dict Task")
        self.assertTrue(d["priority"])
        self.assertEqual(d["deadline"], dt.isoformat())
        self.assertTrue(d["completed"])

    def test_from_dict(self):
        dt = datetime(2025, 9, 18, 12, 0)
        d = {
            "name": "FromDict Task",
            "priority": False,
            "deadline": dt.isoformat(),
            "completed": False
        }
        task = Task.from_dict(d)
        self.assertEqual(task.title, "FromDict Task")
        self.assertFalse(task.priority)
        self.assertEqual(task.deadline, dt)
        self.assertFalse(task.completed)

if __name__ == "__main__":
    unittest.main()
