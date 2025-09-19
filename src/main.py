import tkinter as tk
import sys
import os
# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Now import from the src directory
from ui.GUI import TaskManagerApp
from utils.kill import on_close
from models.taskmanager import TaskManager
from utils.setup import load_config

if __name__ == "__main__":
    root = tk.Tk()
    task = TaskManager(filepath=load_config())
    app = TaskManagerApp(root, task)
    app.tasks = task
    root.protocol("WM_DELETE_WINDOW", lambda: on_close(task))  # <-- Use lambda to defer call
    root.mainloop()