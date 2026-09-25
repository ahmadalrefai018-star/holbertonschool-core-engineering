#!/usr/bin/env python3
"""Safely print elements from a list."""


def safe_print_list(my_list=[], x=0):
    """Print up to x elements and return the number actually printed."""
    count = 0

    for index in range(x):
        try:
            print(my_list[index], end="")
            count += 1
        except IndexError:
            break

    print()
    return count
