#!/usr/bin/env python3
"""
Entry point for the Todo In-Memory Console Application.
"""

from todo_app.main import TodoApp


def main():
    """Main entry point for the application."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()