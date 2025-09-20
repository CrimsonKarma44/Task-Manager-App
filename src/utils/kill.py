from src.utils.setup import write_json_file
from src.models.taskmanager import TaskManager
from src.utils.setup import load_config

def on_close(manager: TaskManager):
    """Handle cleanup on application exit."""
    manager.save()
    # Optionally: exit the app
    import sys
    sys.exit()