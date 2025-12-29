# Skill: terminal-ui-stylist

## Purpose
Make console applications look professional, clean, and visually appealing using only Python standard library.

## Capabilities
- Use ANSI escape codes for colors (no external packages)
- Display status indicators: [✓] for completed (green), [ ] for pending (yellow)
- Print bordered sections and menus with clean alignment
- Format task lists in table-like layout with proper spacing
- Highlight menu options and user prompts
- Error messages in red, success in green

## Example Usage in Code
```python
print("\033[92m[✓] Completed\033[0m")  # Green check
print("\033[93m[ ] Pending\033[0m")     # Yellow pending
print("\033[96m" + "="*60 + "\033[0m")  # Cyan border