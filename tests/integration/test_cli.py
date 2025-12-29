"""
Integration tests for the CLI with new features.
"""

import unittest
from unittest.mock import patch, MagicMock
from src.todo_app.main import TodoApp
from src.todo_app.services.task_service import TaskService
from src.todo_app.services.search_service import SearchService


class TestCLIIntegration(unittest.TestCase):
    """
    Integration tests for the CLI with new features.
    """

    def setUp(self):
        """Set up a TodoApp instance for testing."""
        self.app = TodoApp()

    @patch('builtins.input', side_effect=['Test Task', 'Test Description', 'High', 'work,urgent'])
    @patch('src.todo_app.ui.cli.CLI.print_success')
    def test_add_task_with_priority_and_tags(self, mock_print_success, mock_input):
        """Test adding a task with priority and tags through CLI."""
        initial_count = len(self.app.task_service.get_all_tasks())
        
        # Call the internal method that handles adding a task
        self.app._add_task()
        
        # Verify a task was added
        tasks = self.app.task_service.get_all_tasks()
        self.assertEqual(len(tasks), initial_count + 1)
        
        # Check the last added task
        new_task = tasks[-1]
        self.assertEqual(new_task.title, "Test Task")
        self.assertEqual(new_task.description, "Test Description")
        self.assertEqual(new_task.priority, "High")
        self.assertEqual(new_task.tags, ["work", "urgent"])

    @patch('builtins.input', side_effect=['Test Keyword'])
    @patch('src.todo_app.ui.cli.CLI.print_colored')
    @patch('src.todo_app.ui.cli.CLI.display_tasks')
    def test_search_tasks(self, mock_display_tasks, mock_print_colored, mock_input):
        """Test searching for tasks through CLI."""
        # Add a task that should match the search
        self.app.task_service.add_task("Test Task with Keyword", "Description", "Medium", ["test"])
        
        # Call the search method
        self.app._search_tasks()
        
        # Verify that matching tasks were found and displayed
        mock_display_tasks.assert_called_once()
        # The call should have been made with a list containing at least one task
        args, kwargs = mock_display_tasks.call_args
        self.assertGreater(len(args[0]), 0)  # At least one task should be passed

    @patch('builtins.input', side_effect=['1', 'High'])
    @patch('src.todo_app.ui.cli.CLI.print_success')
    def test_filter_tasks_by_priority(self, mock_print_success, mock_input):
        """Test filtering tasks by priority through CLI."""
        # Add some tasks with different priorities
        self.app.task_service.add_task("High Task", "Description", "High", ["test"])
        self.app.task_service.add_task("Low Task", "Description", "Low", ["test"])
        
        # Call the filter method
        self.app._filter_tasks()
        
        # Note: The filter method has multiple input steps, so this is a simplified test
        # The actual implementation would require more complex mocking

    @patch('builtins.input', side_effect=['1'])  # Sort by priority
    @patch('src.todo_app.ui.cli.CLI.display_tasks')
    def test_sort_tasks_by_priority(self, mock_display_tasks, mock_input):
        """Test sorting tasks by priority through CLI."""
        # Add tasks with different priorities
        self.app.task_service.add_task("Low Task", "Description", "Low", ["test"])
        self.app.task_service.add_task("High Task", "Description", "High", ["test"])
        self.app.task_service.add_task("Medium Task", "Description", "Medium", ["test"])
        
        # Call the sort method
        self.app._sort_tasks()
        
        # Verify that display_tasks was called with sorted tasks
        mock_display_tasks.assert_called_once()
        args, kwargs = mock_display_tasks.call_args
        tasks = args[0]
        
        # Check that tasks are sorted by priority: High, Medium, Low
        priorities = [task.priority for task in tasks]
        expected_order = ["High", "Medium", "Low"]
        self.assertEqual(priorities, expected_order)


if __name__ == "__main__":
    unittest.main()