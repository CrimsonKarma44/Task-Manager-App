from src.models.taskmanager import TaskManager
from typing import Any


def to_save(manager: TaskManager, path) -> Any:
   with open(path, 'w') as f:
      data = manager.to_json()
      f.write(data)
      return data
   
def retrieve(path) -> TaskManager:
   with open(path, 'r') as f:
      data = f.read()
      manager = TaskManager()
      manager.from_json(data)
      return manager