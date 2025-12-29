"""
CLI interface with ANSI color styling utilities.
"""

from typing import List, Optional
from ..models.task import Task


class CLI:
    """
    Command Line Interface with ANSI color styling utilities.
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
    def display_tasks(tasks: List[Task]):
        """
        Display a list of tasks with proper formatting and colors.
        
        Args:
            tasks (List[Task]): List of tasks to display
        """
        if not tasks:
            CLI.print_colored("No tasks found.", 'yellow')
            return
        
        # Print header with border
        CLI.print_border("TASKS")
        
        # Print header row
        header = f"{'ID':<5} {'Status':<8} {'Title':<25} {'Description':<20}"
        CLI.print_colored(header, 'blue')
        
        # Print separator
        CLI.print_colored("-" * 60, 'blue')
        
        # Print each task
        for task in tasks:
            status = "[✓]" if task.completed else "[ ]"
            status_color = 'green' if task.completed else 'yellow'
            
            # Truncate title and description if too long
            title = task.title[:23] + ".." if len(task.title) > 25 else task.title
            desc = task.description[:18] + ".." if len(task.description) > 20 else task.description
            
            task_line = f"{task.id:<5} {CLI.COLORS[status_color]}{status}{CLI.COLORS['reset']:<6} {title:<25} {desc:<20}"
            print(task_line)
        
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
        Display the main menu.
        """
        CLI.print_border("TODO APPLICATION")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Exit")
        CLI.print_border()