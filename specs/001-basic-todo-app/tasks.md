# Implementation Tasks: Basic Todo App

**Feature**: Basic Todo App
**Branch**: 001-basic-todo-app
**Generated**: 2025-12-29
**Input**: specs/001-basic-todo-app/plan.md, spec.md, data-model.md, contracts/, research.md

## Implementation Strategy

MVP approach: Implement User Story 1 (Add New Tasks) first to create a minimal working application, then incrementally add other features. Each user story should be independently testable.

## Dependencies

User stories are largely independent, but share common foundational components (Task class, TaskService, CLI interface). The main menu (US6) is required for navigation between all other features.

## Parallel Execution Examples

- Task model and CLI interface can be developed in parallel
- Individual task operations (add, view, update, delete, mark) can be developed in parallel after foundational components exist
- UI styling can be applied in parallel with feature development

---

## Phase 1: Setup

- [X] T001 Create project structure per implementation plan in src/todo_app/
- [X] T002 Create src/todo_app/__init__.py files for all packages
- [X] T003 Create src/__init__.py and src/run.py entry point
- [X] T004 Create tests/ directory structure with __init__.py files
- [X] T005 Set up basic Python project configuration files

## Phase 2: Foundational Components

- [X] T006 [P] Create Task class in src/todo_app/models/task.py with id, title, description, completed fields
- [X] T007 [P] Create TaskService class in src/todo_app/services/task_service.py with in-memory storage
- [X] T008 [P] Create CLI interface in src/todo_app/ui/cli.py with ANSI color styling utilities
- [X] T009 [P] Create main application class in src/todo_app/main.py with menu structure
- [X] T010 [P] Implement find_task helper method in TaskService

## Phase 3: User Story 1 - Add New Tasks (Priority: P1)

**Goal**: Enable users to add new tasks with a title and description

**Independent Test**: Can be fully tested by adding a new task with title and description and verifying it appears in the task list, delivering the core value of task creation.

- [X] T011 [US1] Implement add_task method in TaskService with validation (title required, 1-200 chars)
- [X] T012 [US1] Implement add_task UI in CLI with prompts for title and description
- [X] T013 [US1] Implement auto-incrementing ID functionality starting from 1
- [X] T014 [US1] Add error handling for invalid input in add_task
- [X] T015 [US1] Test add_task functionality with valid inputs
- [X] T016 [US1] Test add_task validation with invalid inputs

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to view all tasks with clear status indicators

**Independent Test**: Can be fully tested by viewing the list of tasks and verifying they display with ID, title, description, and status indicators, delivering the core value of task visibility.

- [X] T017 [US2] Implement view_tasks method in TaskService to retrieve all tasks
- [X] T018 [US2] Implement view_tasks UI in CLI with ANSI color formatting and borders
- [X] T019 [US2] Display tasks with aligned columns and status indicators ([✓] for completed, [ ] for pending)
- [X] T020 [US2] Apply cyan borders and proper ANSI colors as specified
- [X] T021 [US2] Handle case when no tasks exist
- [X] T022 [US2] Test view_tasks functionality with various task states

## Phase 5: User Story 6 - Navigate Main Menu (Priority: P1)

**Goal**: Provide a clear menu system for easy access to all todo functionality

**Independent Test**: Can be fully tested by navigating through the menu options and accessing all features, delivering the value of easy navigation.

- [X] T023 [US6] Implement main menu loop in src/todo_app/main.py with options 1-7
- [X] T024 [US6] Map menu options to corresponding functionality
- [X] T025 [US6] Implement menu navigation and return to main menu after operations
- [X] T026 [US6] Add Exit option to terminate the application
- [X] T027 [US6] Implement input validation for menu selections
- [X] T028 [US6] Test menu navigation with valid and invalid inputs

## Phase 6: User Story 3 - Update Task Details (Priority: P2)

**Goal**: Allow users to update the title and/or description of their tasks

**Independent Test**: Can be fully tested by updating a task's title and/or description by ID and verifying the changes are reflected, delivering the value of task modification.

- [X] T029 [US3] Implement update_task method in TaskService with optional field updates
- [X] T030 [US3] Implement update_task UI in CLI with ID prompt and optional field updates
- [X] T031 [US3] Allow pressing Enter to skip updating specific fields
- [X] T032 [US3] Add error handling for invalid task IDs in update_task
- [X] T033 [US3] Test update_task functionality with valid inputs
- [X] T034 [US3] Test update_task with invalid task IDs

## Phase 7: User Story 4 - Delete Tasks (Priority: P2)

**Goal**: Allow users to delete tasks they no longer need

**Independent Test**: Can be fully tested by deleting a task by ID and verifying it's removed from the list, delivering the value of task removal.

- [X] T035 [US4] Implement delete_task method in TaskService with confirmation
- [X] T036 [US4] Implement delete_task UI in CLI with ID prompt and confirmation message
- [X] T037 [US4] Display success message after task deletion
- [X] T038 [US4] Add error handling for invalid task IDs in delete_task
- [X] T039 [US4] Test delete_task functionality with valid inputs
- [X] T040 [US4] Test delete_task with invalid task IDs

## Phase 8: User Story 5 - Mark Tasks Complete/Incomplete (Priority: P2)

**Goal**: Allow users to mark tasks as complete or incomplete to track progress

**Independent Test**: Can be fully tested by marking a task as complete or incomplete and verifying the status changes, delivering the value of progress tracking.

- [X] T041 [US5] Implement mark_task method in TaskService to toggle completion status
- [X] T042 [US5] Implement mark_complete UI in CLI with ID prompt
- [X] T043 [US5] Implement mark_incomplete UI in CLI with ID prompt
- [X] T044 [US5] Add error handling for invalid task IDs in mark operations
- [X] T045 [US5] Test mark_complete functionality
- [X] T046 [US5] Test mark_incomplete functionality
- [X] T047 [US5] Test mark operations with invalid task IDs

## Phase 9: Polish & Cross-Cutting Concerns

- [X] T048 Apply consistent terminal styling throughout the application using terminal-ui-stylist
- [X] T049 Implement comprehensive error handling for all user inputs
- [X] T050 Add success messages in green and errors in red as specified
- [X] T051 Ensure all UI elements use ANSI colors as specified (cyan for borders, etc.)
- [X] T052 Test complete workflow from task creation to deletion
- [X] T053 Perform final integration testing of all features
- [X] T054 Document any remaining implementation details in quickstart.md