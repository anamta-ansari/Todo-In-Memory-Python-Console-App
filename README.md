# Todo In-Memory Console App

A beautiful, professional command-line todo application that stores tasks only in memory. Built with Python using strict spec-driven development.

## Features

- 📝 **Add tasks** with title and description
- 👀 **View tasks** with clear status indicators ([✓] for completed, [ ] for pending)
- ✏️ **Update task** title/description by ID
- 🗑️ **Delete tasks** by ID with confirmation
- ✅ **Mark tasks** as complete OR incomplete (toggle)
- 🎨 **Beautiful terminal interface** with ANSI colors and professional styling
- 💾 **In-memory storage** (data is lost when application terminates)

## Requirements

- Python 3.8 or higher

## Setup Instructions

1. **Clone or download** the repository to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd Todo-In-Memory-Python-Console-App
   ```

3. **(Optional) Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Run the application**:
   ```bash
   python src/run.py
   ```

## Usage

Once the application is running, you'll see a menu with the following options:

```
===================== TODO APPLICATION =====================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
============================================================
```

### Menu Options

1. **Add Task**: Enter a title and description for a new task
2. **View Tasks**: See all tasks with their ID, status, title, and description
3. **Update Task**: Modify a task's title or description by ID
4. **Delete Task**: Remove a task by ID with confirmation
5. **Mark Task Complete**: Mark a task as complete by ID
6. **Mark Task Incomplete**: Mark a task as incomplete by ID
7. **Exit**: Close the application

## Project Structure

```
src/
├── todo_app/
│   ├── __init__.py
│   ├── main.py          # Entry point and main menu loop
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py      # Task class definition
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py  # Task operations (add, update, delete, etc.)
│   └── ui/
│       ├── __init__.py
│       └── cli.py       # CLI interface with ANSI styling
├── __init__.py
└── run.py               # Application entry point
```

## Technologies Used

- Python 3.8+
- Standard Python library only (no external dependencies)
- ANSI escape codes for terminal styling

## Development

This project follows spec-driven development principles:

1. Feature specifications in `/specs/`
2. Implementation following the plan in `/specs/plan.md`
3. Tasks breakdown in `/specs/tasks.md`

## Notes

- All data is stored in memory only and will be lost when the application exits
- No external dependencies required
- Cross-platform compatibility (Windows, macOS, Linux)

## License

This project is open source and available under the MIT License.