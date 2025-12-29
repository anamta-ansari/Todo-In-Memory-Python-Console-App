"""
UI styling utility using terminal-ui-stylist for professional console appearance.
"""

from typing import List, Dict, Any


class UIStylist:
    """
    Provides styling utilities for terminal UI using ANSI codes.
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
        color_code = UIStylist.COLORS.get(color, UIStylist.COLORS['white'])
        reset_code = UIStylist.COLORS['reset']
        print(f"{color_code}{text}{reset_code}")

    @staticmethod
    def print_success(message: str):
        """
        Print a success message in green.

        Args:
            message (str): Success message to print
        """
        UIStylist.print_colored(message, 'green')

    @staticmethod
    def print_error(message: str):
        """
        Print an error message in red.

        Args:
            message (str): Error message to print
        """
        UIStylist.print_colored(message, 'red')

    @staticmethod
    def print_warning(message: str):
        """
        Print a warning message in yellow.

        Args:
            message (str): Warning message to print
        """
        UIStylist.print_colored(message, 'yellow')

    @staticmethod
    def print_border(text: str = "", width: int = 60, color: str = 'cyan'):
        """
        Print a bordered line with optional text.

        Args:
            text (str): Text to display in the border
            width (int): Width of the border
            color (str): Color of the border
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

        color_code = UIStylist.COLORS.get(color, UIStylist.COLORS['cyan'])
        reset_code = UIStylist.COLORS['reset']
        print(f"{color_code}{border}{reset_code}")

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
            color = UIStylist.COLORS['bright_red']
        elif priority == "Medium":
            color = UIStylist.COLORS['bright_yellow']
        elif priority == "Low":
            color = UIStylist.COLORS['bright_green']
        else:
            color = UIStylist.COLORS['white']
        
        reset = UIStylist.COLORS['reset']
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
        
        reset = UIStylist.COLORS['reset']
        cyan = UIStylist.COLORS['cyan']
        tag_badges = [f"{cyan}[{tag}]{reset}" for tag in tags]
        return " " + " ".join(tag_badges)

    @staticmethod
    def format_task_row(task: Dict[str, Any], max_title_len: int = 25, max_desc_len: int = 20) -> str:
        """
        Format a task as a row in a table-like display.

        Args:
            task (Dict[str, Any]): Task dictionary
            max_title_len (int): Maximum length for title display
            max_desc_len (int): Maximum length for description display

        Returns:
            str: Formatted task row
        """
        # Format status
        status = "[✓]" if task['completed'] else "[ ]"
        status_color = 'green' if task['completed'] else 'yellow'
        status_str = f"{UIStylist.COLORS[status_color]}{status}{UIStylist.COLORS['reset']}"
        
        # Format title and description with truncation
        title = task['title'][:max_title_len-2] + ".." if len(task['title']) > max_title_len else task['title']
        desc = task['description'][:max_desc_len-2] + ".." if len(task['description']) > max_desc_len else task['description']
        
        # Format priority
        priority_str = UIStylist.format_priority(task['priority'])
        
        # Format tags
        tags_str = UIStylist.format_tags(task['tags'])
        
        # Create the row
        row = f"{task['id']:<5} {status_str:<6} {title:<{max_title_len}} {priority_str:<10} {desc:<{max_desc_len}}{tags_str}"
        return row

    @staticmethod
    def display_task_list(tasks: List[Dict[str, Any]], title: str = "TASKS"):
        """
        Display a list of tasks in a table-like format with proper styling.

        Args:
            tasks (List[Dict[str, Any]]): List of task dictionaries to display
            title (str): Title for the task list display
        """
        if not tasks:
            UIStylist.print_warning("No tasks found.")
            return

        # Print header with border
        UIStylist.print_border(title)

        # Print header row
        header = f"{'ID':<5} {'Status':<6} {'Title':<{25}} {'Priority':<10} {'Description':<{20}} Tags"
        UIStylist.print_colored(header, 'blue')

        # Print separator
        UIStylist.print_colored("-" * 80, 'blue')

        # Print each task
        for task in tasks:
            task_row = UIStylist.format_task_row(task)
            print(task_row)

        # Print footer border
        UIStylist.print_border()