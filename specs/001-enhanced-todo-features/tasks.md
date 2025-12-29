# Implementation Tasks: Enhanced Todo App with Priority, Tags, Search, Filter, and Sort

**Feature**: Enhanced Todo App with Priority, Tags, Search, Filter, and Sort
**Branch**: 001-enhanced-todo-features
**Generated**: 2025-01-07
**Input**: specs/001-enhanced-todo-features/spec.md, specs/001-enhanced-todo-features/plan.md

## Implementation Strategy

This document outlines the implementation tasks for enhancing the Todo console app with priority levels, tags, search, filter, and sort functionality. The approach follows a phased strategy where we first implement the foundational changes (data model and service layer), then implement each user story as a separate phase, and finally add polish and cross-cutting concerns.

The implementation will maintain backward compatibility with existing functionality while adding new features. The core changes include extending the Task model with priority and tags fields, implementing search/filter/sort functionality, and enhancing the UI with color-coded priorities and tag badges using terminal-ui-stylist.

## Phase 1: Setup

Setup tasks for the project structure and initial files.

- [X] T001 Create models directory if it doesn't exist: src/models/
- [X] T002 Create services directory if it doesn't exist: src/services/
- [X] T003 Create cli directory if it doesn't exist: src/cli/
- [X] T004 Create utils directory if it doesn't exist: src/utils/
- [X] T005 Create __init__.py files in all new directories
- [X] T006 Create contracts directory if it doesn't exist: tests/contract/
- [X] T007 Create unit tests directory if it doesn't exist: tests/unit/
- [X] T008 Create integration tests directory if it doesn't exist: tests/integration/

## Phase 2: Foundational Tasks

Foundational tasks that block all user stories.

- [X] T009 [P] Update Task model in src/todo_app/models/task.py with extended attributes (priority, tags)
- [X] T010 [P] Create UI styling utility in src/utils/ui_stylist.py using terminal-ui-stylist
- [X] T011 [P] Update TaskService in src/todo_app/services/task_service.py with enhanced functionality
- [X] T012 [P] Create SearchService in src/todo_app/services/search_service.py for search/filter/sort
- [X] T013 [P] Update existing run.py to import new modules and services
- [X] T014 [P] Create basic tests for Task model in tests/unit/test_task.py
- [X] T015 [P] Create basic tests for TaskService in tests/unit/test_task_service.py
- [X] T016 [P] Create basic tests for SearchService in tests/unit/test_search_service.py

## Phase 3: User Story 1 - Enhanced Task Management with Priority and Tags (Priority: P1)

As a user of the Todo console app, I want to assign priority levels (High/Medium/Low) and tags to my tasks so that I can better organize and prioritize my work.

**Independent Test**: Can be fully tested by adding tasks with different priorities and tags, and verifying they are displayed with appropriate colors and tag badges in the console.

- [X] T017 [US1] Update add_task function to accept priority and tags parameters with defaults
- [X] T018 [US1] Update update_task function to allow modification of priority and tags
- [X] T019 [US1] Implement validation for priority values (High/Medium/Low)
- [X] T020 [US1] Implement validation for tags format (list of strings)
- [X] T021 [US1] Update CLI to prompt for priority when adding tasks (default Medium)
- [X] T022 [US1] Update CLI to prompt for tags when adding tasks (comma-separated)
- [X] T023 [US1] Update CLI to allow changing priority and tags when updating tasks
- [X] T024 [US1] Create unit tests for priority and tags functionality in test_task_service.py
- [X] T025 [US1] Create integration tests for adding tasks with priority and tags in test_cli.py

## Phase 4: User Story 2 - Search Tasks by Keyword (Priority: P2)

As a user of the Todo console app, I want to search for tasks by keyword in the title or description so that I can quickly find specific tasks among many.

**Independent Test**: Can be fully tested by adding multiple tasks with different titles and descriptions, then searching for keywords and verifying the correct tasks are returned.

- [X] T026 [US2] Implement search_tasks function in SearchService for keyword search
- [X] T027 [US2] Implement case-insensitive search across title and description
- [X] T028 [US2] Add search functionality to CLI menu option
- [X] T029 [US2] Create unit tests for search functionality in test_search_service.py
- [X] T030 [US2] Create integration tests for search functionality in test_cli.py

## Phase 5: User Story 3 - Filter Tasks by Status, Priority, or Tag (Priority: P3)

As a user of the Todo console app, I want to filter tasks by status, priority, or specific tag so that I can focus on specific subsets of tasks.

**Independent Test**: Can be fully tested by filtering tasks by different criteria and verifying only the appropriate tasks are displayed.

- [X] T031 [US3] Implement filter_tasks function in SearchService with status/priority/tag filters
- [X] T032 [US3] Implement filtering by status (pending/completed)
- [X] T033 [US3] Implement filtering by priority (High/Medium/Low)
- [X] T034 [US3] Implement filtering by exact tag match
- [X] T035 [US3] Add filter functionality to CLI menu option
- [X] T036 [US3] Create unit tests for filter functionality in test_search_service.py
- [X] T037 [US3] Create integration tests for filter functionality in test_cli.py

## Phase 6: User Story 4 - Sort Tasks by Priority, Title, or Status (Priority: P4)

As a user of the Todo console app, I want to sort tasks by priority, title, or status so that I can organize my task list in a way that makes sense for my workflow.

**Independent Test**: Can be fully tested by sorting tasks by different criteria and verifying the order is correct.

- [X] T038 [US4] Implement sort_tasks function in SearchService with priority/title/status sorting
- [X] T039 [US4] Implement sorting by priority (High first, then Medium, then Low)
- [X] T040 [US4] Implement sorting by title (A-Z alphabetical order)
- [X] T041 [US4] Implement sorting by status (pending first, then completed)
- [X] T042 [US4] Add sort functionality to CLI menu option
- [X] T043 [US4] Create unit tests for sort functionality in test_search_service.py
- [X] T044 [US4] Create integration tests for sort functionality in test_cli.py

## Phase 7: User Story 5 - Enhanced Menu Navigation (Priority: P5)

As a user of the Todo console app, I want new menu options for Search, Filter, and Sort so that I can easily access these new features.

**Independent Test**: Can be fully tested by navigating the menu and accessing the new features through the menu options.

- [X] T045 [US5] Update main menu to include option 8 for Search
- [X] T046 [US5] Update main menu to include option 9 for Filter
- [X] T047 [US5] Update main menu to include option 10 for Sort
- [X] T048 [US5] Update main menu to include option 11 for Exit
- [X] T049 [US5] Implement submenu for Filter option with status/priority/tag choices
- [X] T050 [US5] Implement submenu for Sort option with priority/title/status choices
- [X] T051 [US5] Create integration tests for new menu options in test_cli.py
- [X] T052 [US5] Update CLI menu display to show all 11 options

## Phase 8: UI Enhancement with terminal-ui-stylist

Enhance the UI with color-coded priorities and tag badges using terminal-ui-stylist.

- [X] T053 [P] Implement colored priority display (red=High, yellow=Medium, green=Low)
- [X] T054 [P] Implement cyan tag badges in task display
- [X] T055 [P] Update task list display to use bordered sections
- [X] T056 [P] Apply consistent table-like formatting to task display
- [X] T057 [P] Update all CLI functions to use terminal-ui-stylist for formatting
- [X] T058 [P] Create contract tests for UI display in tests/contract/test_api_contract.py

## Phase 9: Polish & Cross-Cutting Concerns

Final tasks to ensure quality and completeness.

- [X] T059 Add error handling for invalid inputs in all new functions
- [X] T060 Add input validation for all new parameters
- [X] T061 Update documentation strings for all new functions
- [X] T062 Add type hints to all new functions and classes
- [X] T063 Perform integration testing of all features together
- [X] T064 Update README with new features and usage instructions
- [X] T065 Run all tests to ensure no regressions in existing functionality
- [X] T066 Perform end-to-end testing of the complete workflow

## Dependencies

### User Story Completion Order
1. User Story 1 (Enhanced Task Management) - Foundation for all other stories
2. User Story 2 (Search Tasks) - Depends on User Story 1
3. User Story 3 (Filter Tasks) - Depends on User Story 1
4. User Story 4 (Sort Tasks) - Depends on User Story 1
5. User Story 5 (Enhanced Menu) - Depends on all other stories

### Critical Path
- T009 → T011 → T017 → T021 → T025 (Task model and basic functionality)
- T010 → T053 → T054 → T055 → T056 (UI enhancements)
- T012 → T026 → T031 → T038 (Search/Filter/Sort services)
- T045 → T046 → T047 → T048 → T052 (Menu enhancements)

## Parallel Execution Examples

### Per User Story
- **User Story 1**: Tasks T017-T025 can be worked on in parallel after foundational tasks are complete
- **User Story 2**: Tasks T026-T030 can be worked on in parallel after foundational tasks are complete
- **User Story 3**: Tasks T031-T037 can be worked on in parallel after foundational tasks are complete
- **User Story 4**: Tasks T038-T044 can be worked on in parallel after foundational tasks are complete
- **User Story 5**: Tasks T045-T052 can be worked on in parallel after foundational tasks are complete

### Cross-Story Parallelization
- UI Enhancement phase (Phase 8) can be worked on in parallel with User Stories 2-5 after foundational tasks are complete
- Testing tasks can be done in parallel with implementation tasks