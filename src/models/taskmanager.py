class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_all_tasks(self):
        return self.tasks
    
    def get_pending_tasks(self):
         return [task for task in self.tasks if not task.completed]
    
    def get_completed_tasks(self):
         return [task for task in self.tasks if task.completed]

    def get_priority_tasks(self, priority):
         return [task for task in self.tasks if task.priority == priority]
    
    def clear_tasks(self):
        self.tasks = []
   
    def to_json(self):
        import json
        return json.dumps([task.to_dict() for task in self.tasks], indent=4)
    
    def from_json(self, json_str):
         import json
         from .task import Task
         
         data = json.loads(json_str)
         self.tasks = [Task.from_dict(item) for item in data]