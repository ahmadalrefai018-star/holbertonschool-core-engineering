#!/usr/bin/env python3
"""Safely divide two values."""


def safe_print_division(a, b):
    """Divide a by b, always print the result, and return it."""
    result = None

    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        pass
    finally:
        print("Inside result: {}".format(result))

    return result
