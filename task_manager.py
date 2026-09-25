# =====================================================================
# Module: Task Manager (JSON-backed CLI Todo App)
# Description: Add, view, complete, and delete tasks persistently.
# =====================================================================

import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def run_task_manager():
    while True:
        print("\n--- TASK MANAGER MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option (1-5): ").strip()
        tasks = load_tasks()
        
        if choice == '1':
            if not tasks:
                print("\n[i] No tasks found. Your list is empty!")
            else:
                print("\nYour Tasks:")
                for idx, task in enumerate(tasks, 1):
                    status = "✓ [DONE]" if task["completed"] else "✗ [PENDING]"
                    print(f"{idx}. {task['title']} - {status}")
                    
        elif choice == '2':
            title = input("Enter task description: ").strip()
            if title:
                tasks.append({"title": title, "completed": False})
                save_tasks(tasks)
                print(f"\n[+] Task added successfully!")
            else:
                print("\n[!] Task description cannot be empty.")
                
        elif choice == '3':
            if not tasks:
                print("\n[i] No tasks to complete.")
                continue
            try:
                idx = int(input("Enter task number to mark complete: "))
                if 1 <= idx <= len(tasks):
                    tasks[idx - 1]["completed"] = True
                    save_tasks(tasks)
                    print(f"\n[+] Task {idx} marked as completed!")
                else:
                    print("\n[!] Invalid task number.")
            except ValueError:
                print("\n[!] Please enter a valid number.")
                
        elif choice == '4':
            if not tasks:
                print("\n[i] No tasks to delete.")
                continue
            try:
                idx = int(input("Enter task number to delete: "))
                if 1 <= idx <= len(tasks):
                    removed = tasks.pop(idx - 1)
                    save_tasks(tasks)
                    print(f"\n[-] Deleted task: {removed['title']}")
                else:
                    print("\n[!] Invalid task number.")
            except ValueError:
                print("\n[!] Please enter a valid number.")
                
        elif choice == '5':
            break
        else:
            print("\n[!] Invalid option. Choose between 1 to 5.")
