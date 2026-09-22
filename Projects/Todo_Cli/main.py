from todo.storage import load_tasks, save_tasks
from todo.tasks import add_task, complete_task, remove_task, list_tasks

def show_menu():
    print("Options:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. List tasks")
    print("4. Mark task as done")
    print("5. Quit")

def run():
    tasks = load_tasks()

    while True:
        show_menu()

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            title = input("Enter the task title: ")
            add_task(tasks, title)
            save_tasks(tasks)
            
        elif choice == '2':
            index = int(input("Enter the task index to remove: "))
            remove_task(tasks, index)
            save_tasks(tasks)

        elif choice == '3':
            list_tasks(tasks)

        elif choice == '4':
            index = int(input("Task number to complete: "))
            complete_task(tasks, index)
            save_tasks(tasks)

        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    run()