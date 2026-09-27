from rich.console import Console
from rich.table import Table


console = Console()

PRIORITY_COLORS = {"high": "red", "medium": "yellow", "low": "green"}

def render_tasks(tasks):
    """Render a list of tasks as a colored table."""

    if not tasks:
        console.print("[dim]No tasks found.[/dim]")
        return

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("#", width=3)
    table.add_column("Status", width=8)
    table.add_column("Title")
    table.add_column("Priority")
    table.add_column("Due")
    table.add_column("Tags")

    for i, task in enumerate(tasks, start=1):
        status = "[green]✔ done[/green]" if task["done"] else "[red]✗ open[/red]"
        color = PRIORITY_COLORS.get(task["priority"], "white")
        priority_display = f"[{color}]{task['priority']}[/{color}]"
        title_display = f"[strike]{task['title']}[/strike]" if task["done"] else task["title"]
        due = task.get("due_date") or "-"
        tags = ", ".join(task.get("tags", [])) or "-"

        table.add_row(str(i), status, title_display, priority_display, due, tags)

    console.print(table)


def print_message(message, style="green"):
    """Print a simple styled status message (e.g. after add/remove/done)."""
    console.print(f"[{style}]{message}[/{style}]")