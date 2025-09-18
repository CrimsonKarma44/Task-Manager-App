class Task:
   def __init__(self, name, priority="medium", deadline=None, completed=False):
      self.name = name
      self.priority = priority
      self.deadline = None
      self.completed = completed
      if deadline:
         self.set_deadline(deadline)

   def __repr__(self):
      return f"Task(name={self.name}, priority={self.priority})"
   
   def set_deadline(self, deadline):
      if isinstance(deadline, str):
         from datetime import datetime
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
         "name": self.name,
         "priority": self.priority,
         "deadline": self.deadline.isoformat() if self.deadline else None,
         "completed": self.completed
      }
   
   @classmethod
   def from_dict(cls, data):
      deadline = data.get("deadline")
      if deadline:
         from datetime import datetime
         deadline = datetime.fromisoformat(deadline)
      return cls(
         name=data["name"],
         priority=data["priority"],
         deadline=deadline,
         completed=data.get("completed", False)
      )