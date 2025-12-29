"""
Unit tests for the SearchService with search, filter, and sort functionality.
"""

import unittest
from src.todo_app.services.task_service import TaskService
from src.todo_app.services.search_service import SearchService


class TestSearchService(unittest.TestCase):
    """
    Unit tests for the SearchService.
    """

    def setUp(self):
        """Set up a fresh TaskService and SearchService for each test."""
        self.task_service = TaskService()
        self.search_service = SearchService(self.task_service)
        
        # Add some test tasks
        self.task_service.add_task("High Priority Task", "This is important", "High", ["work", "urgent"])
        self.task_service.add_task("Low Priority Task", "This can wait", "Low", ["personal"])
        self.task_service.add_task("Medium Priority Task", "Regular task", "Medium", ["work"])
        self.task_service.add_task("Another Work Task", "More work stuff", "High", ["work", "meeting"])

    def test_search_tasks_by_title(self):
        """Test searching tasks by keyword in title."""
        results = self.search_service.search_tasks("High")
        self.assertEqual(len(results), 1)

        titles = [task.title for task in results]
        self.assertIn("High Priority Task", titles)

    def test_search_tasks_by_description(self):
        """Test searching tasks by keyword in description."""
        results = self.search_service.search_tasks("important")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "High Priority Task")

    def test_filter_tasks_by_status(self):
        """Test filtering tasks by status."""
        # Mark one task as completed
        self.task_service.mark_task(1, True)
        
        # Filter by pending
        pending_tasks = self.search_service.filter_tasks(status="pending")
        self.assertEqual(len(pending_tasks), 3)
        
        # Filter by completed
        completed_tasks = self.search_service.filter_tasks(status="completed")
        self.assertEqual(len(completed_tasks), 1)

    def test_filter_tasks_by_priority(self):
        """Test filtering tasks by priority."""
        high_priority_tasks = self.search_service.filter_tasks(priority="High")
        self.assertEqual(len(high_priority_tasks), 2)
        
        low_priority_tasks = self.search_service.filter_tasks(priority="Low")
        self.assertEqual(len(low_priority_tasks), 1)

    def test_filter_tasks_by_tag(self):
        """Test filtering tasks by tag."""
        work_tasks = self.search_service.filter_tasks(tag="work")
        self.assertEqual(len(work_tasks), 3)

    def test_sort_tasks_by_priority(self):
        """Test sorting tasks by priority."""
        tasks = self.search_service.sort_tasks("priority")
        
        # Should be sorted: High, High, Medium, Low
        priorities = [task.priority for task in tasks]
        expected = ["High", "High", "Medium", "Low"]
        self.assertEqual(priorities, expected)

    def test_sort_tasks_by_title(self):
        """Test sorting tasks by title."""
        tasks = self.search_service.sort_tasks("title")
        
        # Should be sorted alphabetically
        titles = [task.title for task in tasks]
        expected = [
            "Another Work Task", 
            "High Priority Task", 
            "Low Priority Task", 
            "Medium Priority Task"
        ]
        self.assertEqual(titles, expected)

    def test_sort_tasks_by_status(self):
        """Test sorting tasks by status."""
        # Mark some tasks as completed
        self.task_service.mark_task(1, True)
        self.task_service.mark_task(3, True)
        
        tasks = self.search_service.sort_tasks("status")
        
        # Should have pending tasks first, then completed
        statuses = [task.completed for task in tasks]
        # We expect 2 pending (False) then 2 completed (True)
        expected = [False, False, True, True]
        self.assertEqual(statuses, expected)


if __name__ == "__main__":
    unittest.main()