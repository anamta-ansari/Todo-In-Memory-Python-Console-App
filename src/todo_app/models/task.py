"""
Task model representing a single todo item.
"""

from typing import Dict, Any


class Task:
    """
    Represents a single todo item with id, title, description, and completion status.
    """
    
    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        """
        Initialize a Task instance.
        
        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task (required, 1-200 characters)
            description (str): Description of the task (optional, up to 1000 characters)
            completed (bool): Completion status of the task (default: False)
        """
        self.id = task_id
        self.title = self._validate_title(title)
        self.description = self._validate_description(description)
        self.completed = completed
    
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
            "completed": self.completed
        }
    
    def update(self, title: str = None, description: str = None, completed: bool = None):
        """
        Update task attributes.
        
        Args:
            title (str, optional): New title for the task
            description (str, optional): New description for the task
            completed (bool, optional): New completion status for the task
        """
        if title is not None:
            self.title = self._validate_title(title)
        
        if description is not None:
            self.description = self._validate_description(description)
        
        if completed is not None:
            self.completed = completed
    
    def __str__(self) -> str:
        """
        String representation of the task.
        
        Returns:
            str: Formatted string representation
        """
        status = "[✓]" if self.completed else "[ ]"
        return f"{status} {self.id}. {self.title}"
    
    def __repr__(self) -> str:
        """
        Developer-friendly string representation of the task.
        
        Returns:
            str: Detailed string representation
        """
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"