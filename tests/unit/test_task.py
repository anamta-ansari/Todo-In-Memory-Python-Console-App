"""
Unit tests for the enhanced Task model with priority and tags.
"""

import unittest
from src.todo_app.models.task import Task


class TestTask(unittest.TestCase):
    """
    Unit tests for the Task model.
    """

    def test_task_creation_with_defaults(self):
        """Test creating a task with default priority and empty tags."""
        task = Task(1, "Test Task", "Test Description")
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.completed, False)
        self.assertEqual(task.priority, "Medium")
        self.assertEqual(task.tags, [])

    def test_task_creation_with_priority_and_tags(self):
        """Test creating a task with specified priority and tags."""
        task = Task(1, "Test Task", "Test Description", completed=True, priority="High", tags=["work", "urgent"])
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.completed, True)
        self.assertEqual(task.priority, "High")
        self.assertEqual(task.tags, ["work", "urgent"])

    def test_task_update(self):
        """Test updating task attributes."""
        task = Task(1, "Test Task", "Test Description", priority="Low", tags=["personal"])
        
        # Update some attributes
        task.update(title="Updated Task", priority="High", tags=["work", "important"])
        
        self.assertEqual(task.title, "Updated Task")
        self.assertEqual(task.priority, "High")
        self.assertEqual(task.tags, ["work", "important"])

    def test_priority_validation(self):
        """Test priority validation."""
        # Valid priorities
        task = Task(1, "Test Task", priority="high")  # Should be capitalized to "High"
        self.assertEqual(task.priority, "High")
        
        task = Task(1, "Test Task", priority="MEDIUM")  # Should be capitalized to "Medium"
        self.assertEqual(task.priority, "Medium")
        
        # Invalid priority should raise ValueError
        with self.assertRaises(ValueError):
            Task(1, "Test Task", priority="invalid")

    def test_tags_validation(self):
        """Test tags validation."""
        # Valid tags
        task = Task(1, "Test Task", tags=["work", "personal", "work"])  # Duplicates should be removed
        self.assertEqual(task.tags, ["work", "personal"])
        
        # Empty tags list
        task = Task(1, "Test Task", tags=[])
        self.assertEqual(task.tags, [])
        
        # Invalid tags should raise ValueError
        with self.assertRaises(ValueError):
            Task(1, "Test Task", tags="not a list")
        
        with self.assertRaises(ValueError):
            Task(1, "Test Task", tags=[123])  # Non-string tag


if __name__ == "__main__":
    unittest.main()