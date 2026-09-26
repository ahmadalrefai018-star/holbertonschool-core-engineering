#!/usr/bin/env python3
"""Define a square with controlled access to its size."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a square with a validated size."""
        self.size = size

    @property
    def size(self):
        """Return the current square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set and validate the square size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
