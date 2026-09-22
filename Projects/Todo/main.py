import argparse

from todo.storage import load_tasks, save_tasks
from todo.tasks import add_task, complete_task, list_tasks, remove_task

def show_menu():
    print("\n1. Add task\n2. List tasks\n3. Remove task\n4. Mark task as done\n5. Exit")

def run():
    tasks = load_tasks()  # Load tasks from storage at the start

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            priority = input("Enter task priority (high, medium, low): ").strip().lower()
            if priority not in ["high", "medium", "low"]:
                print("Invalid priority. Defaulting to 'medium'.")
                priority = "medium"
            due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
            due_date = due_date if due_date else None
            add_task(tasks, title, priority, due_date)
            save_tasks(tasks)  # Save tasks after adding a new task
        elif choice == "2":
            if not tasks:
                print("No tasks available.")
                continue
            sort_choice = input("Sort by (priority/due_date/none) [default: none]: ").strip().lower()
            sort_by = sort_choice if sort_choice in ["priority", "due_date"] else None
            list_tasks(tasks, sort_by=sort_by)
        elif choice == "3":
            index = int(input("Enter task index to remove: ")) - 1
            remove_task(tasks, index)
            save_tasks(tasks)  # Save tasks after removing a task
        elif choice == "4":
            index = int(input("Task number to complete: ")) - 1
            complete_task(tasks, index)
            save_tasks(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()


# python main.py