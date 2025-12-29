"""
Main application class with menu structure enhanced with priority, tags, search, filter, and sort.
"""

from .services.task_service import TaskService
from .services.search_service import SearchService
from .ui.cli import CLI


class TodoApp:
    """
    Main Todo Application class that handles the menu and user interactions.
    """

    def __init__(self):
        """
        Initialize the TodoApp with required services.
        """
        self.task_service = TaskService()
        self.search_service = SearchService(self.task_service)
        self.cli = CLI()

    def run(self):
        """
        Run the main application loop.
        """
        while True:
            self.cli.display_menu()
            choice = input("Select an option (1-11): ").strip()

            if choice == "1":
                self._add_task()
            elif choice == "2":
                self._view_tasks()
            elif choice == "3":
                self._update_task()
            elif choice == "4":
                self._delete_task()
            elif choice == "5":
                self._mark_task_complete()
            elif choice == "6":
                self._mark_task_incomplete()
            elif choice == "7":
                CLI.print_colored("Goodbye!", 'green')
                break
            elif choice == "8":
                self._search_tasks()
            elif choice == "9":
                self._filter_tasks()
            elif choice == "10":
                self._sort_tasks()
            elif choice == "11":
                CLI.print_colored("Goodbye!", 'green')
                break
            else:
                CLI.print_error("Invalid option. Please select 1-11.")

    def _add_task(self):
        """
        Handle adding a new task with priority and tags.
        """
        CLI.print_border("ADD TASK")
        title, description, priority, tags = CLI.get_task_input_with_priority_and_tags()

        if not title:
            CLI.print_error("Task title is required!")
            return

        try:
            task = self.task_service.add_task(title, description, priority, tags)
            CLI.print_success(f"Task '{task.title}' added successfully with ID {task.id}!")
        except ValueError as e:
            CLI.print_error(f"Error adding task: {str(e)}")

    def _view_tasks(self):
        """
        Handle viewing all tasks.
        """
        CLI.print_border("VIEW TASKS")
        tasks = self.task_service.get_all_tasks()
        CLI.display_tasks(tasks)

    def _update_task(self):
        """
        Handle updating a task with priority and tags.
        """
        CLI.print_border("UPDATE TASK")
        task_id = CLI.get_task_id("Enter task ID to update: ")

        if task_id is None:
            CLI.print_error("Invalid task ID.")
            return

        task = self.task_service.find_task(task_id)
        if not task:
            CLI.print_error(f"Task with ID {task_id} not found.")
            return

        CLI.print_colored(f"Current task: {task.title}", 'yellow')
        CLI.print_colored(f"Current description: {task.description}", 'yellow')
        CLI.print_colored(f"Current priority: {task.priority}", 'yellow')
        CLI.print_colored(f"Current tags: {', '.join(task.tags) if task.tags else 'None'}", 'yellow')

        # Get new title (or press Enter to keep current)
        new_title_input = input(f"Enter new title (or press Enter to keep '{task.title}'): ").strip()
        new_title = new_title_input if new_title_input else None

        # Get new description (or press Enter to keep current)
        new_desc_input = input(f"Enter new description (or press Enter to keep current): ").strip()
        new_description = new_desc_input if new_desc_input else None

        # Get new priority (or press Enter to keep current)
        new_priority_input = input(f"Enter new priority (High/Medium/Low or Enter to keep '{task.priority}'): ").strip()
        new_priority = new_priority_input if new_priority_input else None

        # Get new tags (or press Enter to keep current)
        new_tags_input = input(f"Enter new tags (comma-separated or Enter to keep current): ").strip()
        new_tags = [tag.strip() for tag in new_tags_input.split(",") if tag.strip()] if new_tags_input else None

        # Update the task
        updated_task = self.task_service.update_task(
            task_id,
            title=new_title,
            description=new_description,
            priority=new_priority,
            tags=new_tags
        )
        if updated_task:
            CLI.print_success(f"Task {task_id} updated successfully!")
        else:
            CLI.print_error(f"Failed to update task {task_id}.")

    def _delete_task(self):
        """
        Handle deleting a task.
        """
        CLI.print_border("DELETE TASK")
        task_id = CLI.get_task_id("Enter task ID to delete: ")

        if task_id is None:
            CLI.print_error("Invalid task ID.")
            return

        task = self.task_service.find_task(task_id)
        if not task:
            CLI.print_error(f"Task with ID {task_id} not found.")
            return

        if CLI.confirm_action(f"Are you sure you want to delete task '{task.title}'? (y/n): "):
            if self.task_service.delete_task(task_id):
                CLI.print_success(f"Task {task_id} deleted successfully!")
            else:
                CLI.print_error(f"Failed to delete task {task_id}.")
        else:
            CLI.print_colored("Delete operation cancelled.", 'yellow')

    def _mark_task_complete(self):
        """
        Handle marking a task as complete.
        """
        CLI.print_border("MARK TASK COMPLETE")
        task_id = CLI.get_task_id("Enter task ID to mark complete: ")

        if task_id is None:
            CLI.print_error("Invalid task ID.")
            return

        task = self.task_service.find_task(task_id)
        if not task:
            CLI.print_error(f"Task with ID {task_id} not found.")
            return

        updated_task = self.task_service.mark_task(task_id, True)
        if updated_task:
            CLI.print_success(f"Task {task_id} marked as complete!")
        else:
            CLI.print_error(f"Failed to mark task {task_id} as complete.")

    def _mark_task_incomplete(self):
        """
        Handle marking a task as incomplete.
        """
        CLI.print_border("MARK TASK INCOMPLETE")
        task_id = CLI.get_task_id("Enter task ID to mark incomplete: ")

        if task_id is None:
            CLI.print_error("Invalid task ID.")
            return

        task = self.task_service.find_task(task_id)
        if not task:
            CLI.print_error(f"Task with ID {task_id} not found.")
            return

        updated_task = self.task_service.mark_task(task_id, False)
        if updated_task:
            CLI.print_success(f"Task {task_id} marked as incomplete!")
        else:
            CLI.print_error(f"Failed to mark task {task_id} as incomplete.")

    def _search_tasks(self):
        """
        Handle searching for tasks by keyword.
        """
        CLI.print_border("SEARCH TASKS")
        keyword = input("Enter keyword to search: ").strip()

        if not keyword:
            CLI.print_error("Search keyword is required!")
            return

        tasks = self.search_service.search_tasks(keyword)
        CLI.print_colored(f"Found {len(tasks)} task(s) matching '{keyword}':", 'blue')
        CLI.display_tasks(tasks)

    def _filter_tasks(self):
        """
        Handle filtering tasks by status, priority, or tag.
        """
        CLI.print_border("FILTER TASKS")
        print("Filter by:")
        print("1. Status (pending/completed)")
        print("2. Priority (High/Medium/Low)")
        print("3. Tag")
        print("4. All of the above")

        filter_choice = input("Select filter type (1-4): ").strip()

        status = None
        priority = None
        tag = None

        if filter_choice == "1":
            status_input = input("Enter status (pending/completed): ").strip().lower()
            if status_input in ["pending", "completed"]:
                status = status_input
            else:
                CLI.print_error("Invalid status. Use 'pending' or 'completed'.")
                return
        elif filter_choice == "2":
            priority_input = input("Enter priority (High/Medium/Low): ").strip().capitalize()
            if priority_input in ["High", "Medium", "Low"]:
                priority = priority_input
            else:
                CLI.print_error("Invalid priority. Use 'High', 'Medium', or 'Low'.")
                return
        elif filter_choice == "3":
            tag = input("Enter tag to filter by: ").strip()
            if not tag:
                CLI.print_error("Tag is required for tag filtering.")
                return
        elif filter_choice == "4":
            status_input = input("Enter status (pending/completed, or press Enter to skip): ").strip().lower()
            if status_input and status_input in ["pending", "completed"]:
                status = status_input
            elif status_input and status_input not in ["pending", "completed"]:
                CLI.print_error("Invalid status. Use 'pending' or 'completed'.")
                return

            priority_input = input("Enter priority (High/Medium/Low, or press Enter to skip): ").strip().capitalize()
            if priority_input and priority_input in ["High", "Medium", "Low"]:
                priority = priority_input
            elif priority_input and priority_input not in ["High", "Medium", "Low"]:
                CLI.print_error("Invalid priority. Use 'High', 'Medium', or 'Low'.")
                return

            tag_input = input("Enter tag to filter by (or press Enter to skip): ").strip()
            if tag_input:
                tag = tag_input
        else:
            CLI.print_error("Invalid filter choice.")
            return

        tasks = self.search_service.filter_tasks(status=status, priority=priority, tag=tag)
        CLI.print_colored(f"Found {len(tasks)} task(s) after filtering:", 'blue')
        CLI.display_tasks(tasks)

    def _sort_tasks(self):
        """
        Handle sorting tasks by priority, title, or status.
        """
        CLI.print_border("SORT TASKS")
        print("Sort by:")
        print("1. Priority (High first, then Medium, then Low)")
        print("2. Title (A-Z)")
        print("3. Status (Pending first, then Completed)")

        sort_choice = input("Select sort option (1-3): ").strip()

        if sort_choice == "1":
            sort_by = "priority"
        elif sort_choice == "2":
            sort_by = "title"
        elif sort_choice == "3":
            sort_by = "status"
        else:
            CLI.print_error("Invalid sort option. Please select 1-3.")
            return

        tasks = self.search_service.sort_tasks(sort_by)
        CLI.print_colored(f"Tasks sorted by {sort_by}:", 'blue')
        CLI.display_tasks(tasks)