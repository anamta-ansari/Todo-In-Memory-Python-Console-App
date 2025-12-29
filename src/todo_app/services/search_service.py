"""
Search service for searching, filtering, and sorting tasks.
"""

from typing import List, Dict, Any, Optional
from ..models.task import Task


class SearchService:
    """
    Service class for searching, filtering, and sorting tasks.
    """

    def __init__(self, task_service):
        """
        Initialize the SearchService with a reference to the task service.

        Args:
            task_service: The task service to operate on
        """
        self.task_service = task_service

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword in title or description (case-insensitive).

        Args:
            keyword (str): Keyword to search for

        Returns:
            List[Task]: List of tasks that match the keyword
        """
        if not keyword:
            return []

        keyword_lower = keyword.lower()
        matching_tasks = []

        for task in self.task_service.get_all_tasks():
            if (keyword_lower in task.title.lower() or
                keyword_lower in task.description.lower()):
                matching_tasks.append(task)

        return matching_tasks

    def filter_tasks(self, status: str = None, priority: str = None, tag: str = None) -> List[Task]:
        """
        Filter tasks by status, priority, or tag.

        Args:
            status (str, optional): Filter by status ("pending" or "completed")
            priority (str, optional): Filter by priority ("High", "Medium", "Low")
            tag (str, optional): Filter by exact tag match

        Returns:
            List[Task]: List of tasks that match the filter criteria
        """
        filtered_tasks = self.task_service.get_all_tasks()
        
        # Filter by status
        if status is not None:
            status = status.lower()
            if status == "pending":
                filtered_tasks = [task for task in filtered_tasks if not task.completed]
            elif status == "completed":
                filtered_tasks = [task for task in filtered_tasks if task.completed]
        
        # Filter by priority
        if priority is not None:
            priority = priority.capitalize()
            filtered_tasks = [task for task in filtered_tasks if task.priority == priority]
        
        # Filter by tag
        if tag is not None:
            filtered_tasks = [task for task in filtered_tasks if tag in task.tags]
        
        return filtered_tasks

    def sort_tasks(self, sort_by: str) -> List[Task]:
        """
        Sort tasks by priority, title, or status.

        Args:
            sort_by (str): Sort by "priority", "title", or "status"

        Returns:
            List[Task]: List of tasks sorted according to the specified criteria
        """
        tasks = self.task_service.get_all_tasks()
        
        if sort_by == "priority":
            # Sort by priority: High, Medium, Low
            priority_order = {"High": 1, "Medium": 2, "Low": 3}
            return sorted(tasks, key=lambda task: priority_order[task.priority])
        elif sort_by == "title":
            # Sort by title alphabetically (A-Z)
            return sorted(tasks, key=lambda task: task.title.lower())
        elif sort_by == "status":
            # Sort by status: Pending first, then Completed
            return sorted(tasks, key=lambda task: task.completed)  # False (pending) comes before True (completed)
        else:
            # Return unsorted if invalid sort_by parameter
            return tasks