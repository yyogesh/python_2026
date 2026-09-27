import argparse

from todo.display import print_message, render_tasks
from todo.storage import load_tasks, save_tasks
from todo.tasks import add_task, complete_task, get_sorted_tasks, remove_task, search_tasks

def parse_tags(tags_string):
    """Convert a comma-separated string like 'work,urgent' into ['work', 'urgent']."""
    if not tags_string:
        return []
    return [tag.strip() for tag in tags_string.split(",")]

def build_parser():
    parser = argparse.ArgumentParser(prog='todo', description='A simple command-line to-do list manager.')

    subparsers  = parser.add_subparsers(dest='command', required=True) # add/list/remove

     # --- add ---
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")
    add_parser.add_argument(
        "--priority", choices=["high", "medium", "low"], default="medium",
        help="Task priority (default: medium)"
    )
    add_parser.add_argument("--due", dest="due_date", default=None, help="Due date YYYY-MM-DD")
    add_parser.add_argument(
        "--tags", default=None,
        help="Comma-separated tags, e.g. --tags work,urgent"
    )

     # --- list ---
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument(
        "--sort", dest="sort_by", choices=["priority", "due_date"], default=None
    )

    # --- search ---
    search_parser = subparsers.add_parser("search", help="Search tasks by keyword (title or tags)")
    search_parser.add_argument("keyword", help="Keyword to search for")


    remove_parser = subparsers.add_parser('remove', help='Remove a task.')
    remove_parser.add_argument('index', type=int, help='The index of the task to remove.')

    complete_parser = subparsers.add_parser('complete', help='Mark a task as done.')
    complete_parser.add_argument('index', type=int, help='The index of the task to mark as done.')

    return parser

# def show_menu():
#     print("Options:")
#     print("1. Add a task")
#     print("2. Remove a task")
#     print("3. List tasks")
#     print("4. Mark task as done")
#     print("5. Quit")

def main():
   tasks = load_tasks()

   parser = build_parser()

   args = parser.parse_args()

   if args.command == 'add':
       tags = parse_tags(args.tags)
       add_task(tasks, args.title, args.priority, args.due_date, tags)
       save_tasks(tasks)
       print_message(f"Added task: {args.title}")

   elif args.command == 'list':
      # list_tasks(tasks, args.sort_by)
      render_tasks(get_sorted_tasks(tasks, args.sort_by))

   elif args.command == 'search':
       render_tasks(search_tasks(tasks, args.keyword))

   elif args.command == 'remove':
       removed = remove_task(tasks, args.index)
       if removed:
            save_tasks(tasks)
            print_message(f"Removed: {removed['title']}", style="red")
       else:
            print_message("Invalid index.", style="red")

   elif args.command == 'complete':
       completed = complete_task(tasks, args.index)
       if completed:
            save_tasks(tasks)
            print_message(f"Marked as done: {completed['title']}")
       else:
            print_message("Invalid task number.", style="red")

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