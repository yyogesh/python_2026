import argparse

from todo.storage import load_tasks, save_tasks
from todo.tasks import add_task, complete_task, remove_task, list_tasks


def build_parser():
    parser = argparse.ArgumentParser(prog='todo', description='A simple command-line to-do list manager.')

    subparsers  = parser.add_subparsers(dest='command', required=True) # add/list/remove

    add_parser= subparsers.add_parser('add', help='Add a new task.')
    add_parser.add_argument('title', type=str, help='The title of the task.')
    add_parser.add_argument('--priority', type=str, default='medium', choices=['high', 'medium', 'low'], help='The priority of the task.')
    add_parser.add_argument('--due_date', type=str, default=None, help='Due date in YYYY-MM-DD format')

    list_parser = subparsers.add_parser('list', help='List tasks.')
    list_parser.add_argument('--sort_by', type=str, default=None, choices=['priority', 'due_date'], help='Sort tasks by priority or due date.')

    remove_parser = subparsers.add_parser('remove', help='Remove a task.')
    remove_parser.add_argument('index', type=int, help='The index of the task to remove.')

    complete_parser = subparsers.add_parser('complete', help='Mark a task as done.')
    complete_parser.add_argument('index', type=int, help='The index of the task to mark as done.')

    return parser

def show_menu():
    print("Options:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. List tasks")
    print("4. Mark task as done")
    print("5. Quit")

def main():
   tasks = load_tasks()

   parser = build_parser()

   args = parser.parse_args()

   if args.command == 'add':
       add_task(tasks, args.title, args.priority, args.due_date)
       save_tasks(tasks)
   elif args.command == 'list':
       list_tasks(tasks, args.sort_by)
   elif args.command == 'remove':
       remove_task(tasks, args.index)
       save_tasks(tasks)
   elif args.command == 'complete':
       complete_task(tasks, args.index)
       save_tasks(tasks)

    # while True:
    #     show_menu()

    #     choice = input("Enter your choice (1-4): ")

    #     if choice == '1':
    #         title = input("Enter the task title: ").strip()
    #         priority = input("Enter the task priority (high, medium, low): ").strip().lower()
    #         if priority not in ['high', 'medium', 'low']:
    #             priority = 'medium'
    #         due_date = input("Due date (YYYY-MM-DD) [optional, press Enter to skip]: ").strip()
    #         due_date = None if not due_date else due_date
    #         add_task(tasks, title, priority, due_date)
    #         save_tasks(tasks)
            
    #     elif choice == '2':
    #         index = int(input("Enter the task index to remove: "))
    #         remove_task(tasks, index)
    #         save_tasks(tasks)

    #     elif choice == '3':
    #         if not tasks:
    #             print("No tasks yet!")
    #             continue
    #         sort_choice = input("Sort by (priority, due_date) [optional, press Enter to skip]: ").strip().lower()
    #         sort_by = sort_choice if sort_choice in ("priority", "due_date") else None
    #         list_tasks(tasks, sort_by)

    #     elif choice == '4':
    #         index = int(input("Task number to complete: "))
    #         complete_task(tasks, index)
    #         save_tasks(tasks)

    #     elif choice == '5':
    #         print("Goodbye!")
    #         break
    #     else:
    #         print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()