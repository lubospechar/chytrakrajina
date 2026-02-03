#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from decouple import config


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chytrakrajina.settings")

    # Read from .env via python-decouple; only fallback to Local if missing
    os.environ.setdefault("DJANGO_CONFIGURATION", config("DJANGO_CONFIGURATION", default="Local"))

    try:
        from configurations.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import django-configurations (or Django). "
            "Are you sure it's installed and available on your PYTHONPATH? "
            "Did you forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
