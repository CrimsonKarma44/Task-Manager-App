# Task Manager App

NITDA Cohort 28 Python advanced project work

## 📌 Project Overview

-  \*Task Manager with Deadlines\*\*  
   This project is a simple task manager application that allows users to create tasks, set priorities and deadlines, and keep track of progress. The app highlights overdue tasks, supports sorting and filtering, and helps users stay on top of their goals.

## 🎯 Goals & Objectives

-  Implement **task management (CRUD)** with deadlines and priorities.
-  Learn and apply **classes & exception handling** (especially for invalid dates).
-  Use **regex** for quick search and filtering of tasks.
-  Build a **GUI application** and package it for distribution.
-  Provide **local notifications** for overdue tasks (stretch goal).
-  Explore additional features like **calendar export (.ics)** and drag-and-drop reordering.

---

## ✅ Minimum Viable Product (MVP)

-  Add new tasks with a **title, deadline, and priority**.
-  View tasks in a **sorted list** (by due date/priority).
-  Mark tasks as complete.
-  Highlight overdue tasks.

---

## ✨ Stretch Goals

-  Local notifications for overdue tasks.
-  Export tasks to a **calendar file (.ics)**.
-  Drag-and-drop task reordering in the UI.

---

## �️ Demo Video

<p align="center">
<video controls width="600">
  <source src="asserts/vid/final%20video%20project%20recording2.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
</p>

## 🖼️ Screenshots

Below are some screenshots of the Task Manager App in action:

<p align="center">
  <figure align="center">
    <figcaption align="center">Main Dashboard: Overview of all tasks and deadlines.</figcaption>
    <img src="asserts/img/Screenshot%202025-09-22%20194719.png" alt="Main Dashboard" />
  </figure>
  <figure align="center">
    <figcaption align="center">Add Task Modal: Create a new task with priority and deadline.</figcaption>
    <img src="asserts/img/Screenshot%202025-09-22%20194858.png" alt="Task List Sorted" width="400"/>
  </figure>
  <figure align="center">
    <figcaption align="center">Task List: Sorted by due date and priority.</figcaption>
    <img src="asserts/img/Screenshot%202025-09-22%20194817.png" alt="Add Task Modal" />
  </figure>
  <figure align="center">
    <figcaption align="center">Overdue Highlight: Tasks past their deadline are marked.</figcaption>
    <img src="asserts/img/Screenshot%202025-09-22%20195029.png" alt="Overdue Highlight" />
  </figure>
  <figure align="center">
    <figcaption align="center">Task Completion: Mark tasks as done and track progress.</figcaption>
    <img src="asserts/img/Screenshot%202025-09-22%20195042.png" alt="Task Completion" />
  </figure>
  <figure align="center">
    <figcaption align="center">Filter Options: Filter tasks by status or priority.</figcaption>
    <img src="asserts/img/Screenshot%202025-09-22%20200438.png" alt="Search Feature" />
  </figure>
  <figure align="center">
    <figcaption align="center">Search Feature: Quickly find tasks using keywords.</figcaption>
    <img src="asserts/img/Screenshot%202025-09-22%20200456.png" alt="Filter Options" />
  </figure>
  <figure align="center">
    <figcaption align="center">Settings Panel: Clearing of task.</figcaption>
    <img src="asserts/img/Screenshot%202025-09-22%20200504.png" alt="Settings Panel" />
  </figure>
</p>

---

## 👥 Roles Division

-  **Backend / Logic** → Implement task model, exception handling, regex filters.
-  **Frontend / GUI** → Build the task list UI, modals, progress bar, highlighting.
-  **Notifications / Extras** → Local notifications, calendar export, drag-and-drop.
-  **Testing & Packaging** → Unit tests (sorting/filtering), packaging the app for use.
-  **Documentation** → Maintain README, usage guide, and developer notes.

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

- **Mutman Tapleh Emmanuel (Mutm4)** – *Documentation Specialist*  
  - Maintained project documentation.  
  - Help implement backend storage logic.
  - Ensured clarity in setup instructions, usage guides, and contribution notes.

- **Emmanuel Ogbon (Emmanuel-bee)** – *Backend & Documenter*  
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

-  **Language:** Python
-  **Modules:**
   -  `datetime` → handling deadlines
   -  `re` → regex for quick search
   -  `tkinter` / PyQt (or similar) → GUI
-  **Version Control:** GitHub (collaboration + issues tracking)

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/group10/task-manager.git
cd task-manager

# download packages in the pipenv
pipenv sync
```
To Run the app
```
pipenv run python -m src.main
```
