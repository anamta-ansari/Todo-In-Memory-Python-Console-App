# API Contracts: Basic Todo App

## Task Operations Contract

### Add Task
- **Method**: Internal function call
- **Input**: 
  - title (string, required, 1-200 chars)
  - description (string, optional, 0-1000 chars)
- **Output**: 
  - task object with id, title, description, completed
- **Errors**: 
  - ValidationError if title doesn't meet requirements

### View All Tasks
- **Method**: Internal function call
- **Input**: None
- **Output**: 
  - Array of task objects
- **Errors**: None

### Update Task
- **Method**: Internal function call
- **Input**: 
  - id (integer, required)
  - title (string, optional)
  - description (string, optional)
- **Output**: 
  - Updated task object
- **Errors**: 
  - NotFoundError if task doesn't exist

### Delete Task
- **Method**: Internal function call
- **Input**: 
  - id (integer, required)
- **Output**: 
  - Success status (boolean)
- **Errors**: 
  - NotFoundError if task doesn't exist

### Mark Task Complete/Incomplete
- **Method**: Internal function call
- **Input**: 
  - id (integer, required)
  - completed (boolean, required)
- **Output**: 
  - Updated task object
- **Errors**: 
  - NotFoundError if task doesn't exist