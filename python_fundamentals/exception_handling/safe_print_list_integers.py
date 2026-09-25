#!/usr/bin/env python3
"""Safely print integer elements from a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print only integers among the first x elements."""
    count = 0

    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            count += 1
        except (TypeError, ValueError):
            pass

    print()
    return count
