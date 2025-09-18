# Task Manager App
NITDA Cohort 28 Python advanced project work

## 📌 Project Overview  
**Task Manager with Deadlines**  
This project is a simple task manager application that allows users to create tasks, set priorities and deadlines, and keep track of progress. The app highlights overdue tasks, supports sorting and filtering, and helps users stay on top of their goals.  

---

## 🎯 Goals & Objectives  
- Implement **task management (CRUD)** with deadlines and priorities.  
- Learn and apply **classes & exception handling** (especially for invalid dates).  
- Use **regex** for quick search and filtering of tasks.  
- Build a **GUI application** and package it for distribution.  
- Provide **local notifications** for overdue tasks (stretch goal).  
- Explore additional features like **calendar export (.ics)** and drag-and-drop reordering.  

---

## ✅ Minimum Viable Product (MVP)  
- Add new tasks with a **title, deadline, and priority**.  
- View tasks in a **sorted list** (by due date/priority).  
- Mark tasks as complete.  
- Highlight overdue tasks.  

---

## ✨ Stretch Goals  
- Local notifications for overdue tasks.  
- Export tasks to a **calendar file (.ics)**.  
- Drag-and-drop task reordering in the UI.

---

## 👥 Roles Division  
- **Backend / Logic** → Implement task model, exception handling, regex filters.  
- **Frontend / GUI** → Build the task list UI, modals, progress bar, highlighting.  
- **Notifications / Extras** → Local notifications, calendar export, drag-and-drop.  
- **Testing & Packaging** → Unit tests (sorting/filtering), packaging the app for use.  
- **Documentation** → Maintain README, usage guide, and developer notes.  

---

## 🛠️ Tech & Tools  
- **Language:** Python  
- **Modules:**  
  - `datetime` → handling deadlines  
  - `re` → regex for quick search  
  - `tkinter` / PyQt (or similar) → GUI  
- **Version Control:** GitHub (collaboration + issues tracking)  

---

## 🚀 How to Run  
```bash
# Clone the repo
git clone https://github.com/group10/task-manager.git
cd task-manager

# download packages in the pipenv
pipenv sync

# Run the app
pipenv run python src/main.py
