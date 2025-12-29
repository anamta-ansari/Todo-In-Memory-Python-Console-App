"""
Enhanced task service for managing tasks in memory with priority and tags.
"""

from typing import List, Optional, Dict, Any
from ..models.task import Task


class TaskService:
    """
    Enhanced service class for managing tasks in memory with priority and tags.
    """

    def __init__(self):
        """
        Initialize the TaskService with an empty task list and ID counter.
        """
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: str = "", priority: str = "Medium", tags: List[str] = None) -> Task:
        """
        Add a new task with the given title, description, priority, and tags.

        Args:
            title (str): Title of the task (required, 1-200 characters)
            description (str): Description of the task (optional, up to 1000 characters)
            priority (str): Priority level of the task (default: "Medium")
            tags (List[str]): List of tags associated with the task (default: empty list)

        Returns:
            Task: The newly created task
        """
        task = Task(self._next_id, title, description, completed=False, priority=priority, tags=tags)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks.

        Returns:
            List[Task]: List of all tasks
        """
        return self.tasks.copy()

    def find_task(self, task_id: int) -> Optional[Task]:
        """
        Find a task by its ID.

        Args:
            task_id (int): ID of the task to find

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: str = None, description: str = None, 
                    completed: bool = None, priority: str = None, tags: List[str] = None) -> Optional[Task]:
        """
        Update a task's attributes.

        Args:
            task_id (int): ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task
            completed (bool, optional): New completion status
            priority (str, optional): New priority for the task
            tags (List[str], optional): New tags for the task

        Returns:
            Optional[Task]: The updated task if found, None otherwise
        """
        task = self.find_task(task_id)
        if task:
            # Only update fields that are provided (not None)
            updated_title = title if title is not None else task.title
            updated_description = description if description is not None else task.description
            updated_completed = completed if completed is not None else task.completed
            updated_priority = priority if priority is not None else task.priority
            updated_tags = tags if tags is not None else task.tags
            
            task.update(
                title=updated_title,
                description=updated_description,
                completed=updated_completed,
                priority=updated_priority,
                tags=updated_tags
            )
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if not found
        """
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_task(self, task_id: int, completed: bool) -> Optional[Task]:
        """
        Mark a task as complete or incomplete.

        Args:
            task_id (int): ID of the task to update
            completed (bool): New completion status

        Returns:
            Optional[Task]: The updated task if found, None otherwise
        """
        task = self.find_task(task_id)
        if task:
            task.update(completed=completed)
            return task
        return None

    def get_next_id(self) -> int:
        """
        Get the next available task ID.

        Returns:
            int: The next available task ID
        """
        return self._next_id