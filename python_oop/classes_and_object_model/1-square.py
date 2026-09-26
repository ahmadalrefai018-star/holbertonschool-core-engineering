#!/usr/bin/env python3
"""Define a square with a private size attribute."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a square with a private size."""
        self.__size = size
