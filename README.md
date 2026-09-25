# 🐍 Python CLI Automation & Productivity Suite

A lightweight, robust, and modular command-line interface (CLI) application built with Python. Designed to automate local productivity workflows by combining a persistent JSON-backed Task Manager with a smart Automated File Organizer.

---

## 🚀 Features

### 1. Persistent Task Manager (`task_manager.py`)
* **JSON Storage:** Automatically saves and loads tasks persistently using a local `tasks.json` file.
* **CRUD Capabilities:** Add new tasks, view existing items with visual completion statuses (`✓ [DONE]` / `✗ [PENDING]`), mark tasks as completed, and remove items cleanly.
* **Error Handling:** Robust input validation preventing crashes on invalid index entries or non-numeric inputs.

### 2. Smart File Organizer (`file_organizer.py`)
* **Automated Categorization:** Scans any target directory and segregates files into structured folders based on their extensions (`Images`, `Documents`, `Archives`, `Code`, `Media`, and `Others`).
* **Safe Directory Management:** Automatically creates category subdirectories on-the-fly (`os.makedirs`) only when matching files are found.
* **Flexibility:** Allows users to specify a custom target path or run directly on the current working directory.

---

## 🛠️ Tech Stack & Core Libraries
* **Language:** Python 3.x
* **Standard Libraries Used:** 
  * `os` & `shutil` (File system operations and path manipulation)
  * `json` (Persistent lightweight data serialization)
  * `sys` (Process management and safe exits)

---

## 📂 Project Structure
```text
python-cli-automation-suite/
│
├── main.py              # Central entry point and master CLI menu
├── task_manager.py      # Task management logic and JSON persistence
├── file_organizer.py    # Automated file sorting and categorization logic
└── README.md            # Project documentation
