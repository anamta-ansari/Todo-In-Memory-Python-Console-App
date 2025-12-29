"""
CLI interface with ANSI color styling utilities enhanced with terminal-ui-stylist.
"""

from typing import List, Optional
from ..models.task import Task


class CLI:
    """
    Command Line Interface with ANSI color styling utilities enhanced with terminal-ui-stylist.
    """

    # ANSI color codes
    COLORS = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'bright_red': '\033[91m',
        'bright_green': '\033[92m',
        'bright_yellow': '\033[93m',
        'bright_blue': '\033[94m',
        'bright_magenta': '\033[95m',
        'bright_cyan': '\033[96m',
        'reset': '\033[0m'
    }

    @staticmethod
    def print_colored(text: str, color: str = 'white'):
        """
        Print text in the specified color.

        Args:
            text (str): Text to print
            color (str): Color to use
        """
        color_code = CLI.COLORS.get(color, CLI.COLORS['white'])
        reset_code = CLI.COLORS['reset']
        print(f"{color_code}{text}{reset_code}")

    @staticmethod
    def print_success(message: str):
        """
        Print a success message in green.

        Args:
            message (str): Success message to print
        """
        CLI.print_colored(message, 'green')

    @staticmethod
    def print_error(message: str):
        """
        Print an error message in red.

        Args:
            message (str): Error message to print
        """
        CLI.print_colored(message, 'red')

    @staticmethod
    def print_warning(message: str):
        """
        Print a warning message in yellow.

        Args:
            message (str): Warning message to print
        """
        CLI.print_colored(message, 'yellow')

    @staticmethod
    def print_border(text: str = "", width: int = 60):
        """
        Print a bordered line with optional text.

        Args:
            text (str): Text to display in the border
            width (int): Width of the border
        """
        if text:
            # Add spaces around the text
            text = f" {text} "
            # Calculate how many '=' characters to add on each side
            remaining_width = width - len(text)
            left_side = remaining_width // 2
            right_side = remaining_width - left_side
            border = "=" * left_side + text + "=" * right_side
        else:
            border = "=" * width

        CLI.print_colored(border, 'cyan')

    @staticmethod
    def format_priority(priority: str) -> str:
        """
        Format priority with appropriate color coding.

        Args:
            priority (str): Priority level (High, Medium, Low)

        Returns:
            str: Colored priority string
        """
        priority = priority.capitalize()
        if priority == "High":
            color = CLI.COLORS['bright_red']
        elif priority == "Medium":
            color = CLI.COLORS['bright_yellow']
        elif priority == "Low":
            color = CLI.COLORS['bright_green']
        else:
            color = CLI.COLORS['white']

        reset = CLI.COLORS['reset']
        return f"{color}{priority}{reset}"

    @staticmethod
    def format_tags(tags: List[str]) -> str:
        """
        Format tags as cyan badges.

        Args:
            tags (List[str]): List of tags

        Returns:
            str: Formatted tags as cyan badges
        """
        if not tags:
            return ""

        reset = CLI.COLORS['reset']
        cyan = CLI.COLORS['cyan']
        tag_badges = [f"{cyan}[{tag}]{reset}" for tag in tags]
        return " " + " ".join(tag_badges)

    @staticmethod
    def format_task_row(task: Task, max_title_len: int = 25, max_desc_len: int = 20) -> str:
        """
        Format a task as a row in a table-like display.

        Args:
            task (Task): Task object to format
            max_title_len (int): Maximum length for title display
            max_desc_len (int): Maximum length for description display

        Returns:
            str: Formatted task row
        """
        # Format status
        status = "[✓]" if task.completed else "[ ]"
        status_color = 'green' if task.completed else 'yellow'
        status_str = f"{CLI.COLORS[status_color]}{status}{CLI.COLORS['reset']}"

        # Format title and description with truncation
        title = task.title[:max_title_len-2] + ".." if len(task.title) > max_title_len else task.title
        desc = task.description[:max_desc_len-2] + ".." if len(task.description) > max_desc_len else task.description

        # Format priority
        priority_str = CLI.format_priority(task.priority)

        # Format tags
        tags_str = CLI.format_tags(task.tags)

        # Create the row
        row = f"{task.id:<5} {status_str:<6} {title:<{max_title_len}} {priority_str:<10} {desc:<{max_desc_len}}{tags_str}"
        return row

    @staticmethod
    def display_tasks(tasks: List[Task]):
        """
        Display a list of tasks with proper formatting and colors.

        Args:
            tasks (List[Task]): List of tasks to display
        """
        if not tasks:
            CLI.print_warning("No tasks found.")
            return

        # Print header with border
        CLI.print_border("TASKS")

        # Print header row
        header = f"{'ID':<5} {'Status':<6} {'Title':<{25}} {'Priority':<10} {'Description':<{20}} Tags"
        CLI.print_colored(header, 'blue')

        # Print separator
        CLI.print_colored("-" * 80, 'blue')

        # Print each task
        for task in tasks:
            task_row = CLI.format_task_row(task)
            print(task_row)

        # Print footer border
        CLI.print_border()

    @staticmethod
    def get_task_input() -> tuple:
        """
        Get task input from the user.

        Returns:
            tuple: (title, description) entered by the user
        """
        title = input("Enter task title: ").strip()
        description = input("Enter task description (optional): ").strip()
        return title, description

    @staticmethod
    def get_task_input_with_priority_and_tags() -> tuple:
        """
        Get task input from the user including priority and tags.

        Returns:
            tuple: (title, description, priority, tags) entered by the user
        """
        title = input("Enter task title: ").strip()
        description = input("Enter task description (optional): ").strip()

        # Get priority with default
        priority_input = input("Enter priority (High/Medium/Low) [default: Medium]: ").strip()
        priority = priority_input if priority_input else "Medium"

        # Get tags as comma-separated list
        tags_input = input("Enter tags (comma-separated) [optional]: ").strip()
        tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()] if tags_input else []

        return title, description, priority, tags

    @staticmethod
    def get_task_id(prompt: str = "Enter task ID: ") -> Optional[int]:
        """
        Get a task ID from the user with validation.

        Args:
            prompt (str): Prompt to display to the user

        Returns:
            Optional[int]: Task ID if valid, None otherwise
        """
        try:
            task_id_str = input(prompt).strip()
            if not task_id_str:
                return None
            return int(task_id_str)
        except ValueError:
            CLI.print_error("Invalid ID. Please enter a number.")
            return None

    @staticmethod
    def confirm_action(prompt: str = "Are you sure? (y/n): ") -> bool:
        """
        Get confirmation from the user.

        Args:
            prompt (str): Confirmation prompt

        Returns:
            bool: True if user confirms, False otherwise
        """
        response = input(prompt).strip().lower()
        return response in ['y', 'yes', '1', 'true', 'ok']

    @staticmethod
    def display_menu():
        """
        Display the main menu with enhanced options.
        """
        CLI.print_border("TODO APPLICATION")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Exit")
        print("8. Search Tasks")
        print("9. Filter Tasks")
        print("10. Sort Tasks")
        print("11. Exit")
        CLI.print_border()