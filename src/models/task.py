from datetime import datetime

class Task:
   def __init__(self, title:str, priority:str="medium", deadline:datetime=None, completed:bool=False):
      
      self.title:str = title
      self.priority:str = priority
      self.deadline: datetime | str = None
      self.completed:bool = completed

      if deadline:
         self.set_deadline(deadline)

   def __repr__(self):
      return f"Task(name={self.title}, priority={self.priority})"
   
   def is_overdue(self):
      return not self.completed and datetime.now() > self.deadline


   def set_deadline(self, deadline: datetime | str):
      if isinstance(deadline, str):
         try:
            self.deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M")
         except ValueError:
            raise ValueError("Deadline must be in 'YYYY-MM-DD' format")
      else:
         self.deadline = deadline

   def mark_completed(self):
      self.completed = True

   def to_dict(self):
      return {
         "title": self.title,
         "priority": self.priority,
         "deadline": self.deadline.isoformat() if self.deadline else None,
         "completed": self.completed
      }
   
   @classmethod
   def from_dict(cls, data: dict):
      deadline = data.get("deadline")
      if deadline:
         deadline = datetime.fromisoformat(deadline)
      return cls(
         title=data["title"],
         priority=data["priority"],
         deadline=deadline,
         completed=data.get("completed", False)
      )