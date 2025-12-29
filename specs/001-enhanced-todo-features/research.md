# Research: Enhanced Todo App with Priority, Tags, Search, Filter, and Sort

## Overview

This document captures research findings for implementing enhanced features in the Todo console app, including priority levels, tags, search, filter, and sort functionality.

## Research Findings

### 1. Data Model Extension

**Decision**: Extend the existing Task model to include priority and tags fields
**Rationale**: The existing Task model needs to be enhanced with two new fields:
- `priority`: string field with values 'High', 'Medium', 'Low' (default 'Medium')
- `tags`: list of string values for categorization
**Alternatives considered**: 
- Separate priority and tags tables/models - rejected as unnecessary complexity for in-memory storage
- Using integers for priority instead of strings - rejected for readability and clarity

### 2. Terminal UI Styling

**Decision**: Use terminal-ui-stylist for enhanced UI with colors and formatting
**Rationale**: The specification requires using terminal-ui-stylist for professional appearance, with colored priority text (red=High, yellow=Medium, green=Low) and cyan tag badges
**Alternatives considered**:
- Using standard print statements - rejected as it doesn't meet UI requirements
- Using a different styling library - rejected as specification mandates terminal-ui-stylist

### 3. Search Implementation

**Decision**: Implement case-insensitive substring search across title and description
**Rationale**: The specification requires searching for keywords in title or description, with case-insensitive matching
**Implementation approach**: 
- Use Python's `in` operator with `.lower()` for case-insensitive matching
- Search both title and description fields
- Return all tasks that match the keyword in either field

### 4. Filter Implementation

**Decision**: Implement filtering by status, priority, and exact tag
**Rationale**: The specification requires filtering by status (pending/completed), priority (High/Medium/Low), or exact tag
**Implementation approach**:
- Create filter functions that take a criteria and return matching tasks
- For tag filtering, check if the specified tag exists in the task's tags list
- Allow filtering by multiple criteria if needed

### 5. Sort Implementation

**Decision**: Implement sorting by priority, title, and status
**Rationale**: The specification requires sorting by priority (High first, then Medium, then Low), title (A-Z), or status (pending first, then completed)
**Implementation approach**:
- Create sort functions using Python's `sorted()` with custom key functions
- For priority sorting, use a mapping to assign numeric values to priority levels
- For status sorting, treat pending as higher priority than completed

### 6. Menu Expansion

**Decision**: Add new menu options 8-11 while preserving existing options 1-7
**Rationale**: The specification requires adding new menu options for Search (8), Filter (9), Sort (10), and Exit (11) while keeping original functionality
**Implementation approach**:
- Extend the existing menu loop to handle new options
- Create dedicated functions for each new feature
- Maintain backward compatibility with existing menu options

### 7. Input Validation

**Decision**: Implement validation for priority values and tag format
**Rationale**: Need to ensure data integrity and prevent invalid values from being stored
**Implementation approach**:
- Validate priority values are one of 'High', 'Medium', 'Low' (case-insensitive)
- Validate tags are non-empty strings
- Provide clear error messages for invalid inputs

## Technical Considerations

### Performance
- For search, filter, and sort operations, aim for O(n) or O(n log n) time complexity
- For up to 1000 tasks, operations should complete in under 1 second as per requirements

### Memory Usage
- Since the app uses in-memory storage, ensure the enhanced data model doesn't significantly increase memory usage
- Tags are stored as lists of strings, which should be efficient for typical use cases

### Error Handling
- Implement proper error handling for invalid inputs
- Provide user-friendly error messages
- Gracefully handle edge cases like empty task lists during sorting/filtering

## Implementation Strategy

1. First, extend the Task model with priority and tags fields
2. Update the TaskService to handle the new fields
3. Implement search, filter, and sort functionality
4. Create UI functions using terminal-ui-stylist
5. Update the menu system to include new options
6. Test all functionality to ensure backward compatibility