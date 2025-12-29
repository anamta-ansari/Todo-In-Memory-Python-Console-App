<!-- SYNC IMPACT REPORT
Version change: N/A → 1.0.0
Added sections: Core Principles (6 principles), Additional Constraints, Development Workflow, Governance
Modified principles: N/A (new constitution)
Removed sections: N/A
Templates requiring updates: 
- ✅ .specify/templates/plan-template.md - updated
- ✅ .specify/templates/spec-template.md - updated  
- ✅ .specify/templates/tasks-template.md - updated
- ⚠ .specify/templates/commands/*.md - pending manual review
- ⚠ README.md - pending manual review
Follow-up TODOs: None
-->

# Todo In-Memory Console App Constitution

## Core Principles

### I. Spec-Driven Development
All features must be specified before implementation; Specifications serve as contracts that guide development and testing; Changes to behavior require specification updates first before code changes.

### II. Clean Code Principles
Code must be readable, maintainable, and well-structured; Follow Python PEP 8 style guidelines; Functions and classes should have single responsibilities; Proper documentation and type hints required.

### III. Proper Python Project Structure
Organize code following standard Python project conventions; Separate source code in src/ directory; Tests in tests/ directory; Proper package structure with __init__.py files; Use virtual environments for dependency management.

### IV. No External Dependencies
The application must run with standard Python library only; No pip packages beyond what's in standard library; Self-contained implementation to ensure portability and simplicity; All functionality built from scratch.

### V. Beautiful and Professional Terminal Interface
Create an intuitive, user-friendly command-line experience; Clear, well-formatted output with proper spacing and alignment; Consistent command syntax and helpful error messages; Professional visual presentation in terminal.

### VI. In-Memory Data Storage
Tasks are stored only in memory during application runtime; No persistent storage to files or databases; Data is lost when application terminates; Focus on core functionality without persistence complexity.

## Additional Constraints

### Exact Scope Requirements
Implement ONLY these 5 features:
1. Add task with title and description
2. View all tasks with ID and clear status indicators
3. Update task title/description by ID
4. Delete task by ID
5. Mark task as complete OR incomplete (toggle)

### Technical Rules
- All changes must go through specs first
- Code only in src/ directory
- Specs in specs-history/ directory
- Reusable intelligence in .qwen/skills/ and documented in qwen.md
- No external dependencies beyond Python standard library

## Development Workflow

### Implementation Process
- Create detailed specifications before writing code
- Write tests to validate against specifications
- Implement features following specification exactly
- Verify implementation matches specification requirements
- Document any deviations or clarifications needed

### Quality Standards
- Code must be clean, readable, and well-documented
- Proper error handling for all user inputs
- Consistent formatting and naming conventions
- Comprehensive testing of all features
- Professional terminal interface design

## Governance

This constitution governs all development practices for the Todo In-Memory Console App project. All team members must follow these principles and constraints. Amendments to this constitution require explicit approval and documentation of the changes and their rationale.

Specifications take precedence over implementation; if there's a conflict between what the code does and what the spec says, the spec is correct and the code must be updated.

**Version**: 1.0.0 | **Ratified**: 2025-01-01 | **Last Amended**: 2025-12-29