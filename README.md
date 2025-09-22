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

## 👥 Contributions

Our team collaborated to build the Task Manager App, with each member focusing on specific areas:

- **Vincent Princewill (CrimsonKarma44)** – *Project Lead, Backend Developer, Unit tester & DevOps*  
  - Designed and implemented the task manager’s core logic (task creation, completion, deletion).  
  - Co-Developed sorting/filtering by deadline and priority.  
  - Wrote comprehensive unit tests for functionality and edge cases.  
  - Set up project infrastructure, including folder structure and configuration.  
  - Implemented GitHub Actions for CI/CD (automated testing and workflows).  
  - Managed repository structure and overall GitHub project setup.
  - Ensured clarity in setup instructions, usage guides, and contribution notes.

- **AHakeem-cpu** – *UI/UX Designer & Frontend Contributor*  
  - Designed and implemented the application’s user interface.
  - Co-Developed sorting/filtering by deadline and priority.  
  - Focused on usability and seamless integration with backend logic.  

- **Emmanuel Ogbon (Emmanuel-bee)** – *Documentation Specialist*  
  - Co-Authored and maintained project documentation.  
  - Ensured clarity in setup instructions, usage guides, and contribution notes.
  - Co-Created Demo Video
  - Refined the README and supplementary docs for accessibility.  

- **Zainab Abubakar (majesty244342)** – *Documentation Specialist*  
  - Co-Authored and maintained project documentation.  
  - Ensured clarity in setup instructions, usage guides, and contribution notes.
  - Co-Created Demo Video  
  - Refined the README and supplementary docs for accessibility. 

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
#### Commands
To clone the repo
```
git clone https://github.com/group10/Task-Manager-App.git
cd Task-Manager-App
```
To download packages in the pipenv
```
pipenv sync
```
To Run the app
```
pipenv run python -m src.main
```
To Run tests
```
pipenv run pytest
```
Recommended to run them sequentially. 
Thank you!
