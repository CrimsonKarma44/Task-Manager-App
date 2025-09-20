import threading

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from win10toast import ToastNotifier

from src.models.task import Task
from src.models.taskmanager import TaskManager
from src.utils.lib import add_placeholder
from src.utils.setup import load_config

notifier = ToastNotifier()

class TaskManagerApp:
    def __init__(self, root: tk.Tk, manager: TaskManager):
        self.root:tk.Tk = root
        self.tasks:TaskManager = manager
        self.root.title("Task Manager")

        self.setup_ui()
        self.update_task_list()
        self.start_notification_thread()

    def setup_ui(self):
        # Controls
        control_frame:tk.Frame = tk.Frame(self.root)
        control_frame.pack(pady=10)

        tk.Button(control_frame, text="Add Task", command=self.open_add_modal).pack(side=tk.LEFT, padx=5)

        self.filter_var = tk.StringVar(value="All")
        ttk.Combobox(control_frame, textvariable=self.filter_var, values=["All", "Completed", "Overdue", "Pending"], state="readonly").pack(side=tk.LEFT)
        tk.Button(control_frame, text="Apply Filter", command=self.update_task_list).pack(side=tk.LEFT, padx=5)

        # --- Add Search Entry ---
        tk.Label(control_frame, text="Search:").pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(control_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Search", command=self.update_task_list).pack(side=tk.LEFT, padx=5)
        # ------------------------

        # --- Add Clear Buttons ---
        tk.Button(control_frame, text="Clear All Tasks", command=self.clear_all_tasks).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Clear Selected Task", command=self.clear_selected_task).pack(side=tk.LEFT, padx=5)
    # -------------------------

        # Progress Bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(fill=tk.X, padx=10, pady=5)

        # Task List
        self.tree = ttk.Treeview(self.root, columns=("Title", "Priority", "Deadline", "Status"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.tree.bind("<Double-1>", self.toggle_complete)


    def open_add_modal(self):
        modal = tk.Toplevel(self.root)
        modal.title("Add Task")

        tk.Label(modal, text="Title").grid(row=0, column=0, sticky="W", padx=10, pady=5)
        title_entry = tk.Entry(modal)
        title_entry.grid(row=0, column=1, sticky="e", padx=10, pady=5)
        add_placeholder(title_entry, 'Name of Task')

        tk.Label(modal, text="Priority").grid(row=1, column=0, sticky="W", padx=10, pady=5)
        priority_var = tk.StringVar(value="Medium")
        ttk.Combobox(modal, textvariable=priority_var, values=["Low", "Medium", "High"], state="readonly").grid(row=1, column=1, sticky="e", padx=10, pady=5)

        tk.Label(modal, text="Deadline").grid(row=2, column=0, sticky="W", padx=10, pady=5)
        deadline_entry = tk.Entry(modal)
        deadline_entry.grid(row=2, column=1, sticky="e", padx=10, pady=5)
        add_placeholder(deadline_entry, 'YYYY-MM-DD HH:MM')

        def save_task():
            try:
                deadline = datetime.strptime(deadline_entry.get(), "%Y-%m-%d %H:%M")
                task = Task(title_entry.get(), priority_var.get(), deadline)
                self.tasks.add_task(task)
                modal.destroy()
                self.update_task_list()
            except ValueError:
                messagebox.showerror("Invalid Date", "Please enter deadline in correct format.")

        tk.Button(modal, text="Save ", command=save_task, width=10).grid(row=3, column=0, columnspan=2, pady=10)

    def update_task_list(self):
        self.tree.delete(*self.tree.get_children())
        filtered = self.get_filtered_tasks()
        filter_priority = sorted(filtered, key=lambda x: {"High": 1, "Medium": 2, "Low": 3}[x.priority])
        for task in filter_priority:
            status = "Completed" if task.completed else "Pending"
            deadline_str = task.deadline.strftime("%Y-%m-%d %H:%M")
            row = (task.title, task.priority, deadline_str, status)
            tag = ""
            if task.is_overdue():
                tag = "overdue"
            elif task.priority == "High":
                tag = "high"
            self.tree.insert("", tk.END, values=row, tags=(tag,))
        
        self.tree.tag_configure("overdue", background="tomato")
        self.tree.tag_configure("high", background="orange")

        self.update_progress()

    def get_filtered_tasks(self):
        filter_type = self.filter_var.get()
        search_pattern = self.search_var.get().strip()
        if filter_type == "Completed":
            filtered = self.tasks.get_completed_tasks()
        elif filter_type == "Overdue":
            filtered = self.tasks.get_overdue_tasks()
        elif filter_type == "Pending":
            filtered = self.tasks.get_pending_tasks()
        else:
            filtered = self.tasks.get_all_tasks()

        if search_pattern:
            filtered = [task for task in filtered if task in self.tasks.search_tasks(search_pattern)]
        return filtered

    def toggle_complete(self, event):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            title = item["values"][0]
            for task in self.tasks.get_all_tasks():
                if task.title == title:
                    task.completed = not task.completed
                    break
            self.update_task_list()

    def update_progress(self):
        if not self.tasks.get_all_tasks():
            self.progress_var.set(0)
            return
        completed = sum(1 for t in self.tasks.get_all_tasks() if t.completed)
        percent = (completed / len(self.tasks.get_all_tasks())) * 100
        self.progress_var.set(percent)

    # adjusted notification thread to use after method for messagebox by Vince 
    def start_notification_thread(self):
        def notify():
            notified_deadlines = set()
            while True:
                now = datetime.now()
                for task in self.tasks.get_all_tasks():
                    # Overdue warning
                    if task.is_overdue():
                        self.root.after(
                            0,
                            lambda t=task: messagebox.showwarning("Overdue Task", f"'{t.title}' is overdue!")
                        )

                    # Deadline reached notification
                    if not task.completed and task.deadline <= now <= task.deadline + timedelta(minutes=1):
                        if task.title not in notified_deadlines:
                            # Run toast directly in background thread
                            notifier.show_toast(
                                "Task Deadline Reached",
                                f"'{task.title}' deadline is now!",
                                duration=10,
                                threaded=True  # <--- important
                            )
                            notified_deadlines.add(task.title)

                # wait once per loop
                threading.Event().wait(180)

        threading.Thread(target=notify, daemon=True).start()

    def clear_all_tasks(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            self.tasks.clear_tasks()
            self.tasks.save()
            self.update_task_list()

    def clear_selected_task(self):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            title = item["values"][0]
            for task in self.tasks.get_all_tasks():
                if task.title == title:
                    self.tasks.remove_task(task)
                    break
            self.update_task_list()
        else:
            messagebox.showinfo("No Selection", "Please select a task to clear.")
