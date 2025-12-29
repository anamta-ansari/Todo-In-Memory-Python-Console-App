# Todo In-Memory Console App

A beautiful command-line todo application built using spec-driven development with Qwen CLI. Now upgraded with priorities, tags, search, filter, and sorting for a polished and practical feel.

## Features

- 📝 **Add/Update tasks** with title, description, priority (High/Medium/Low), and tags
- 👀 **View tasks** with colored priority and tag badges
- 🔍 **Search** by keyword
- 🎚️ **Filter** by status/priority/tag
- 📊 **Sort** by priority/title/status
- ✏️ **Update task** title/description by ID
- 🗑️ **Delete tasks** by ID with confirmation
- ✅ **Mark tasks** as complete OR incomplete (toggle)
- 🎨 **Beautiful terminal interface** with ANSI colors, symbols, and badges using terminal-ui-stylist skill
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
5. Mark Complete
6. Mark Incomplete
7. Exit
8. Search
9. Filter
10. Sort
11. Exit
============================================================
```

### Menu Options

1. **Add Task**: Enter a title, description, priority, and tags for a new task
2. **View Tasks**: See all tasks with their ID, status, title, description, priority, and tags
3. **Update Task**: Modify a task's title, description, priority, or tags by ID
4. **Delete Task**: Remove a task by ID with confirmation
5. **Mark Complete**: Mark a task as complete by ID
6. **Mark Incomplete**: Mark a task as incomplete by ID
7. **Exit**: Close the application
8. **Search**: Find tasks by keyword in title or description
9. **Filter**: Filter tasks by status, priority, or tags
10. **Sort**: Sort tasks by priority, title, or status
11. **Exit**: Close the application

## Project Structure

```
src/
├── cli/
│   ├── __init__.py
│   └── cli.py           # CLI interface with ANSI styling
├── models/
│   ├── __init__.py
│   └── task.py          # Task class definition
├── services/
│   ├── __init__.py
│   └── task_service.py  # Task operations (add, update, delete, etc.)
├── todo_app/
│   ├── __init__.py
│   └── main.py          # Main application logic
├── utils/
│   └── __init__.py
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
- Beautiful terminal UI with colors/symbols/badges using terminal-ui-stylist skill
- Cross-platform compatibility (Windows, macOS, Linux)

## License

This project is open source and available under the MIT License.