# Data Model: Basic Todo App

## Task Entity

### Fields
- **id**: Integer (auto-incremented, starting from 1)
- **title**: String (required, non-empty)
- **description**: String (optional, can be empty)
- **completed**: Boolean (default: False)

### Validation Rules
- ID must be a positive integer
- Title must be a non-empty string (1-200 characters)
- Description can be an empty string or up to 1000 characters
- Completed status must be a boolean value

### State Transitions
- New task: `completed = False`
- Mark complete: `completed = True`
- Mark incomplete: `completed = False`

## Task List Structure

### In-Memory Storage
- **Type**: List of dictionaries
- **Access pattern**: Index-based and ID-based lookups
- **Operations**: Add, update, delete, retrieve by ID, retrieve all

### Example Structure
```python
tasks = [
    {
        "id": 1,
        "title": "Sample task",
        "description": "This is a sample task description",
        "completed": False
    },
    {
        "id": 2,
        "title": "Another task",
        "description": "Another task description",
        "completed": True
    }
]
```

## Operations

### Add Task
- Input: title (str), description (str)
- Process: Create new task dict with auto-incremented ID, set completed=False
- Output: New task with assigned ID

### Update Task
- Input: task ID (int), new title (str, optional), new description (str, optional)
- Process: Find task by ID, update specified fields only
- Output: Updated task

### Delete Task
- Input: task ID (int)
- Process: Remove task from list by ID
- Output: Success/failure status

### Mark Complete/Incomplete
- Input: task ID (int), target status (bool)
- Process: Find task by ID, update completed status
- Output: Updated task

### Retrieve All Tasks
- Input: None
- Process: Return entire task list
- Output: List of all tasks

### Retrieve Task by ID
- Input: task ID (int)
- Process: Find task by ID
- Output: Single task or None if not found