#!/usr/bin/env python3
"""Safely print an integer."""


def safe_print_integer(value):
    """Print value as an integer and return whether printing succeeded."""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
