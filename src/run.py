#!/usr/bin/env python3
"""
Entry point for the Todo In-Memory Console Application.
"""

import sys
import os
# Add the src directory to the path so we can import from todo_app
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from todo_app.main import TodoApp


def main():
    """Main entry point for the application."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()