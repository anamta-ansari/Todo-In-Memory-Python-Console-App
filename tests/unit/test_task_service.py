"""
Unit tests for the enhanced TaskService with priority and tags functionality.
"""

import unittest
from src.todo_app.services.task_service import TaskService


class TestTaskService(unittest.TestCase):
    """
    Unit tests for the TaskService.
    """

    def setUp(self):
        """Set up a fresh TaskService for each test."""
        self.service = TaskService()

    def test_add_task_with_priority_and_tags(self):
        """Test adding a task with priority and tags."""
        task = self.service.add_task("Test Task", "Test Description", "High", ["work", "urgent"])
        
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.priority, "High")
        self.assertEqual(task.tags, ["work", "urgent"])
        self.assertEqual(task.id, 1)

    def test_update_task_with_priority_and_tags(self):
        """Test updating a task with priority and tags."""
        # Add a task first
        task = self.service.add_task("Test Task", "Test Description", "Low", ["personal"])
        
        # Update the task
        updated_task = self.service.update_task(
            task.id, 
            title="Updated Task", 
            priority="High", 
            tags=["work", "important"]
        )
        
        self.assertEqual(updated_task.title, "Updated Task")
        self.assertEqual(updated_task.priority, "High")
        self.assertEqual(updated_task.tags, ["work", "important"])

    def test_get_all_tasks(self):
        """Test getting all tasks."""
        # Add a few tasks
        self.service.add_task("Task 1", priority="High", tags=["work"])
        self.service.add_task("Task 2", priority="Low", tags=["personal"])
        
        tasks = self.service.get_all_tasks()
        
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].priority, "High")
        self.assertEqual(tasks[1].priority, "Low")


if __name__ == "__main__":
    unittest.main()