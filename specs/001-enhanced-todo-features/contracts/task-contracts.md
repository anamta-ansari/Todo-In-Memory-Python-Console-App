# API Contracts: Enhanced Todo App

## Overview

This document defines the API contracts for the enhanced Todo console app functionality, including the new search, filter, and sort features.

## Task Operations

### 1. Add Task
- **Function**: `add_task(title: str, description: str = "", priority: str = "Medium", tags: list[str] = []) -> int`
- **Input**: 
  - title (required): Task title (1-200 chars)
  - description (optional): Task description (max 1000 chars)
  - priority (optional): "High", "Medium", or "Low" (defaults to "Medium")
  - tags (optional): List of tag strings (max 50 chars each)
- **Output**: Task ID (int) of the newly created task
- **Error cases**: Invalid input parameters

### 2. Get All Tasks
- **Function**: `get_all_tasks() -> list[dict]`
- **Input**: None
- **Output**: List of all tasks as dictionaries with all attributes
- **Error cases**: None

### 3. Get Task by ID
- **Function**: `get_task(task_id: int) -> dict`
- **Input**: Task ID (int)
- **Output**: Task dictionary with all attributes
- **Error cases**: Task ID not found

### 4. Update Task
- **Function**: `update_task(task_id: int, title: str = None, description: str = None, status: str = None, priority: str = None, tags: list[str] = None) -> bool`
- **Input**: 
  - task_id (required): ID of the task to update
  - title (optional): New title
  - description (optional): New description
  - status (optional): New status ("pending" or "completed")
  - priority (optional): New priority ("High", "Medium", or "Low")
  - tags (optional): New list of tags
- **Output**: Boolean indicating success (True) or failure (False)
- **Error cases**: Task ID not found, invalid input parameters

### 5. Delete Task
- **Function**: `delete_task(task_id: int) -> bool`
- **Input**: Task ID (int)
- **Output**: Boolean indicating success (True) or failure (False)
- **Error cases**: Task ID not found

### 6. Toggle Task Status
- **Function**: `toggle_task_status(task_id: int) -> bool`
- **Input**: Task ID (int)
- **Output**: Boolean indicating success (True) or failure (False)
- **Error cases**: Task ID not found

## New Enhanced Operations

### 7. Search Tasks
- **Function**: `search_tasks(keyword: str) -> list[dict]`
- **Input**: keyword (str) - text to search for in title or description
- **Output**: List of tasks that contain the keyword (case-insensitive)
- **Error cases**: None (returns empty list if no matches)

### 8. Filter Tasks
- **Function**: `filter_tasks(status: str = None, priority: str = None, tag: str = None) -> list[dict]`
- **Input**: 
  - status (optional): Filter by status ("pending" or "completed")
  - priority (optional): Filter by priority ("High", "Medium", or "Low")
  - tag (optional): Filter by exact tag match
- **Output**: List of tasks matching the filter criteria
- **Error cases**: Invalid filter parameters

### 9. Sort Tasks
- **Function**: `sort_tasks(sort_by: str) -> list[dict]`
- **Input**: sort_by (str) - "priority", "title", or "status"
- **Output**: List of tasks sorted according to the specified criteria:
  - "priority": High, Medium, Low
  - "title": Alphabetical A-Z
  - "status": Pending first, then Completed
- **Error cases**: Invalid sort_by parameter

## UI Display Contract

### 10. Format Task for Display
- **Function**: `format_task_for_display(task: dict) -> str`
- **Input**: Task dictionary
- **Output**: Formatted string with color-coded priority and tag badges
- **Requirements**: 
  - Priority displayed in color: Red for High, Yellow for Medium, Green for Low
  - Tags displayed as cyan badges
  - Consistent table-like formatting