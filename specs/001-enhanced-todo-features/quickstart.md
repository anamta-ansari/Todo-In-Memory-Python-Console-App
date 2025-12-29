# Quickstart Guide: Enhanced Todo App

## Overview

This guide provides a quick overview of how to set up and run the enhanced Todo console app with priority, tags, search, filter, and sort functionality.

## Prerequisites

- Python 3.8 or higher
- No external dependencies required (uses only Python standard library)

## Setup

1. Clone or download the repository
2. Navigate to the project directory
3. Ensure you have Python 3.8+ installed:
   ```bash
   python --version
   ```

## Running the Application

1. Navigate to the project root directory
2. Run the application:
   ```bash
   python -m src.run
   ```
   
   Or if in the src directory:
   ```bash
   python run.py
   ```

## Using the Enhanced Features

### Adding Tasks with Priority and Tags

1. Select option 1 from the main menu to add a task
2. Enter the task title
3. Enter the task description (optional)
4. Enter the priority level (High, Medium, or Low - defaults to Medium)
5. Enter tags as a comma-separated list (optional)

### Viewing Tasks

1. Select option 2 from the main menu to view all tasks
2. Tasks will be displayed with:
   - Color-coded priority (Red=High, Yellow=Medium, Green=Low)
   - Cyan tag badges
   - Status indicators

### Updating Tasks

1. Select option 3 from the main menu to update a task
2. Enter the task ID
3. Update the title and/or description as needed
4. You can also update the priority and tags

### Searching Tasks

1. Select option 8 from the main menu to search tasks
2. Enter a keyword to search in task titles or descriptions
3. The app will display all matching tasks

### Filtering Tasks

1. Select option 9 from the main menu to filter tasks
2. Choose a filter criterion:
   - Filter by status (pending/completed)
   - Filter by priority (High/Medium/Low)
   - Filter by tag (exact match)
3. The app will display tasks matching your filter

### Sorting Tasks

1. Select option 10 from the main menu to sort tasks
2. Choose a sorting criterion:
   - Sort by priority (High first, then Medium, then Low)
   - Sort by title (A-Z alphabetical)
   - Sort by status (pending first, then completed)
3. The app will display tasks in the sorted order

### Exiting the Application

1. Select option 11 from the main menu to exit
2. The application will terminate (note: tasks are stored in memory only and will be lost)

## Example Usage

```
Todo Console App
================
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Mark task as complete/incomplete
6. [Original options 6-7 if applicable]
7. [Original options 6-7 if applicable]
8. Search tasks
9. Filter tasks
10. Sort tasks
11. Exit
Choose an option: 1

Enter task title: Complete project
Enter task description: Finish the project documentation
Enter priority (High/Medium/Low) [default: Medium]: High
Enter tags (comma-separated) [optional]: work,urgent

Task added successfully with ID: 1
```

## Troubleshooting

- If you get an import error, make sure you're running the app from the project root
- If the colors don't display properly in your terminal, try a different terminal application
- Remember that tasks are stored only in memory and will be lost when the application exits