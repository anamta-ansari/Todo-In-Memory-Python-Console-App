"""
Task model representing a single todo item with priority and tags.
"""

from typing import Dict, Any, List


class Task:
    """
    Represents a single todo item with id, title, description, completion status, priority, and tags.
    """

    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False, 
                 priority: str = "Medium", tags: List[str] = None):
        """
        Initialize a Task instance.

        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task (required, 1-200 characters)
            description (str): Description of the task (optional, up to 1000 characters)
            completed (bool): Completion status of the task (default: False)
            priority (str): Priority level of the task (default: "Medium")
            tags (List[str]): List of tags associated with the task (default: empty list)
        """
        self.id = task_id
        self.title = self._validate_title(title)
        self.description = self._validate_description(description)
        self.completed = completed
        self.priority = self._validate_priority(priority)
        self.tags = self._validate_tags(tags if tags is not None else [])

    def _validate_title(self, title: str) -> str:
        """
        Validate the title according to requirements.

        Args:
            title (str): Title to validate

        Returns:
            str: Validated title

        Raises:
            ValueError: If title doesn't meet requirements
        """
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string")

        if len(title) < 1 or len(title) > 200:
            raise ValueError("Title must be between 1 and 200 characters")

        return title

    def _validate_description(self, description: str) -> str:
        """
        Validate the description according to requirements.

        Args:
            description (str): Description to validate

        Returns:
            str: Validated description
        """
        if not isinstance(description, str):
            raise ValueError("Description must be a string")

        if len(description) > 1000:
            raise ValueError("Description must be less than 1000 characters")

        return description

    def _validate_priority(self, priority: str) -> str:
        """
        Validate the priority according to requirements.

        Args:
            priority (str): Priority to validate

        Returns:
            str: Validated priority

        Raises:
            ValueError: If priority doesn't meet requirements
        """
        if not isinstance(priority, str):
            raise ValueError("Priority must be a string")

        priority = priority.capitalize()
        valid_priorities = ["High", "Medium", "Low"]
        if priority not in valid_priorities:
            raise ValueError(f"Priority must be one of: {', '.join(valid_priorities)}")

        return priority

    def _validate_tags(self, tags: List[str]) -> List[str]:
        """
        Validate the tags according to requirements.

        Args:
            tags (List[str]): Tags to validate

        Returns:
            List[str]: Validated tags

        Raises:
            ValueError: If tags don't meet requirements
        """
        if not isinstance(tags, list):
            raise ValueError("Tags must be a list")

        validated_tags = []
        for tag in tags:
            if not isinstance(tag, str):
                raise ValueError("Each tag must be a string")
            
            if len(tag) < 1 or len(tag) > 50:
                raise ValueError("Each tag must be between 1 and 50 characters")
            
            # Add tag only if it's not already in the list (avoid duplicates)
            if tag not in validated_tags:
                validated_tags.append(tag)

        return validated_tags

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Task instance to a dictionary.

        Returns:
            Dict[str, Any]: Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "priority": self.priority,
            "tags": self.tags
        }

    def update(self, title: str = None, description: str = None, completed: bool = None, 
               priority: str = None, tags: List[str] = None):
        """
        Update task attributes.

        Args:
            title (str, optional): New title for the task
            description (str, optional): New description for the task
            completed (bool, optional): New completion status for the task
            priority (str, optional): New priority for the task
            tags (List[str], optional): New tags for the task
        """
        if title is not None:
            self.title = self._validate_title(title)

        if description is not None:
            self.description = self._validate_description(description)

        if completed is not None:
            self.completed = completed

        if priority is not None:
            self.priority = self._validate_priority(priority)

        if tags is not None:
            self.tags = self._validate_tags(tags)

    def __str__(self) -> str:
        """
        String representation of the task.

        Returns:
            str: Formatted string representation
        """
        status = "[✓]" if self.completed else "[ ]"
        return f"{status} {self.id}. {self.title} (Priority: {self.priority})"

    def __repr__(self) -> str:
        """
        Developer-friendly string representation of the task.

        Returns:
            str: Detailed string representation
        """
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed}, priority={self.priority}, tags={self.tags})"