import unittest
from src.models.taskmanager import TaskManager
from src.models.task import Task

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.task1 = Task("Task 1")
        self.task2 = Task("Task 2", completed=True)
        self.task3 = Task("Task 3", priority="High")
        self.manager.add_task(self.task1)
        self.manager.add_task(self.task2)
        self.manager.add_task(self.task3)

    def test_add_task(self):
        task = Task("New Task", priority="low")
        self.manager.add_task(task)
        self.assertIn(task, self.manager.get_all_tasks())

    def test_remove_task(self):
        self.manager.remove_task(self.task1)
        self.assertNotIn(self.task1, self.manager.get_all_tasks())

    def test_get_all_tasks(self):
        tasks = self.manager.get_all_tasks()
        self.assertEqual(len(tasks), 3)

    def test_get_pending_tasks(self):
        pending = self.manager.get_pending_tasks()
        self.assertIn(self.task1, pending)
        self.assertIn(self.task3, pending)
        self.assertNotIn(self.task2, pending)

    def test_get_completed_tasks(self):
        completed = self.manager.get_completed_tasks()
        self.assertIn(self.task2, completed)
        self.assertNotIn(self.task1, completed)

    def test_get_priority_tasks(self):
        priority = self.manager.get_priority_tasks("medium")
        self.assertIn(self.task1, priority)
        self.assertNotIn(self.task3, priority)

    def test_clear_tasks(self):
        self.manager.clear_tasks()
        self.assertEqual(len(self.manager.get_all_tasks()), 0)

    def test_to_json_and_from_json(self):
        json_str = self.manager.to_json()
        new_manager = TaskManager()
        new_manager.from_json(json_str)
        self.assertEqual(len(new_manager.get_all_tasks()), 3)
        self.assertEqual(new_manager.get_all_tasks()[0].title, "Task 1")

if __name__ == "__main__":
    unittest.main()
