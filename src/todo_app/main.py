"""
Main application class with menu structure.
"""

from .services.task_service import TaskService
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
        self.cli = CLI()
    
    def run(self):
        """
        Run the main application loop.
        """
        while True:
            self.cli.display_menu()
            choice = input("Select an option (1-7): ").strip()
            
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
            else:
                CLI.print_error("Invalid option. Please select 1-7.")
    
    def _add_task(self):
        """
        Handle adding a new task.
        """
        CLI.print_border("ADD TASK")
        title, description = CLI.get_task_input()
        
        if not title:
            CLI.print_error("Task title is required!")
            return
        
        try:
            task = self.task_service.add_task(title, description)
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
        Handle updating a task.
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
        
        # Get new title (or press Enter to keep current)
        new_title_input = input(f"Enter new title (or press Enter to keep '{task.title}'): ").strip()
        new_title = new_title_input if new_title_input else None
        
        # Get new description (or press Enter to keep current)
        new_desc_input = input(f"Enter new description (or press Enter to keep current): ").strip()
        new_description = new_desc_input if new_desc_input else None
        
        # Update the task
        updated_task = self.task_service.update_task(task_id, new_title, new_description)
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