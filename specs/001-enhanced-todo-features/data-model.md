# Data Model: Enhanced Todo App with Priority, Tags, Search, Filter, and Sort

## Overview

This document defines the data model for the enhanced Todo console app, including the extended Task entity with priority and tags functionality.

## Task Entity

### Attributes

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| id | int | Yes | Auto-generated | Unique identifier for the task |
| title | str | Yes | N/A | Title of the task |
| description | str | No | Empty string | Detailed description of the task |
| status | str | Yes | "pending" | Status of the task ("pending" or "completed") |
| priority | str | Yes | "Medium" | Priority level ("High", "Medium", or "Low") |
| tags | list[str] | No | Empty list | List of tags associated with the task |

### Validation Rules

1. **ID**: Must be a positive integer, auto-incremented from the highest existing ID
2. **Title**: Must be a non-empty string with 1-200 characters
3. **Description**: Optional, can be empty, maximum 1000 characters
4. **Status**: Must be one of "pending" or "completed" (case-insensitive)
5. **Priority**: Must be one of "High", "Medium", or "Low" (case-insensitive, defaults to "Medium")
6. **Tags**: List of strings, each tag must be 1-50 characters, no duplicates in the list

### State Transitions

- Status can transition from "pending" to "completed" and vice versa
- All other attributes can be modified when updating a task

## Example Task Objects

```python
# Example of a high priority task with tags
{
    "id": 1,
    "title": "Complete project proposal",
    "description": "Finish the proposal document for client review",
    "status": "pending",
    "priority": "High",
    "tags": ["work", "urgent", "client"]
}

# Example of a low priority task with no tags
{
    "id": 2,
    "title": "Organize desk",
    "description": "Clean and organize the workspace",
    "status": "pending",
    "priority": "Low",
    "tags": []
}

# Example of a completed task with tags
{
    "id": 3,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread, fruits",
    "status": "completed",
    "priority": "Medium",
    "tags": ["personal", "shopping"]
}
```

## Relationships

The Task entity is self-contained and does not have explicit relationships with other entities in this implementation. However, tasks can be logically grouped by:
- Status (pending vs completed)
- Priority (High vs Medium vs Low)
- Tags (tasks sharing the same tags)

## Data Access Patterns

1. **Create**: Add a new task with specified attributes
2. **Read**: Retrieve all tasks or a specific task by ID
3. **Update**: Modify task attributes (title, description, status, priority, tags)
4. **Delete**: Remove a task by ID
5. **Search**: Find tasks containing a keyword in title or description
6. **Filter**: Get tasks matching specific criteria (status, priority, tag)
7. **Sort**: Order tasks by priority, title, or status