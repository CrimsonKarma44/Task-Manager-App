import json
from ..models.task import Task
from ..utils.setup import ensure_json_file, read_json_file, write_json_file

class TaskManager:
    def search_tasks(self, pattern: str):
        """Return tasks whose title matches the regex pattern."""
        import re
        regex = re.compile(pattern, re.IGNORECASE)
        return [task for task in self.tasks if regex.search(task.title)]
    def __init__(self, filepath: str):
        self.filepath: str = filepath
        ensure_json_file(filepath=self.filepath)
        self.tasks: list[Task] = self.from_json(read_json_file(self.filepath))

    def add_task(self, task: Task):
        self.tasks.append(task)
        self.save()  # <-- Save after adding

    def remove_task(self, task: Task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.save()  # <-- Save after removing

    def get_all_tasks(self):
        return self.tasks
    
    def get_pending_tasks(self):
         return [task for task in self.tasks if not task.completed and not task.is_overdue()]
    
    def get_completed_tasks(self):
         return [task for task in self.tasks if task.completed]
    
    def get_overdue_tasks(self):
         return [task for task in self.tasks if task.is_overdue()]

    def get_priority_tasks(self, priority: str):
         return [task for task in self.tasks if task.priority == priority]
    
    def clear_tasks(self):
        self.tasks = []
   
    def to_json(self):
        return json.dumps([task.to_dict() for task in self.tasks], indent=4)
    
    def from_json(self, json_list: list):
        return [Task.from_dict(item) for item in json_list if item]  # <-- Ignore empty dicts

    def save(self):
        write_json_file(self.filepath, [task.to_dict() for task in self.tasks])