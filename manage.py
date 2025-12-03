#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys# /manage.py

# 🌟 ADD THIS BLOCK TO FIX PATH ERRORS 🌟
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
# ----------------------------------------

def main():
    """Run administrative tasks."""
    # 1. Sets the default settings module (your project's settings file)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'binge_watch_project.settings')
    try:
        # 2. Imports the core Django management function
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # This handles the case where Django isn't installed
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # 3. Executes the command passed from the terminal
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()