# Quickstart Guide: Basic Todo App

## Getting Started

### Prerequisites
- Python 3.8 or higher
- No external dependencies required

### Installation
1. Clone or download the repository
2. Navigate to the project directory
3. Ensure you have Python 3.8+ installed

### Running the Application
1. Navigate to the project root directory
2. Run the application:
   ```bash
   python -m src.run
   ```
   or
   ```bash
   python src/run.py
   ```

## Using the Application

### Main Menu
The application presents a numbered menu with the following options:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit

### Adding a Task
1. Select option 1 from the main menu
2. Enter the task title when prompted
3. Enter the task description when prompted
4. The task will be added with an auto-incremented ID

### Viewing Tasks
1. Select option 2 from the main menu
2. All tasks will be displayed with:
   - ID number
   - Title
   - Description
   - Status indicator ([✓] for completed, [ ] for pending)
   - Formatted with ANSI colors

### Updating a Task
1. Select option 3 from the main menu
2. Enter the task ID when prompted
3. Enter the new title (or press Enter to skip)
4. Enter the new description (or press Enter to skip)
5. The task will be updated with the new information

### Deleting a Task
1. Select option 4 from the main menu
2. Enter the task ID when prompted
3. Confirm the deletion when prompted
4. The task will be removed from the list

### Marking Tasks
- To mark complete: Select option 5, enter task ID
- To mark incomplete: Select option 6, enter task ID

### Exiting
- Select option 7 to exit the application
- Note: All data is stored in memory only and will be lost on exit

## Error Handling
- Invalid task IDs will result in error messages
- Invalid menu selections will prompt for valid input
- Empty titles will result in error messages