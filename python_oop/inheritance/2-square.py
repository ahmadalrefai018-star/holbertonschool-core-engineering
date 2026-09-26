#!/usr/bin/env python3
"""Define a complete Square class."""


Rectangle = __import__("2-rectangle").Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a square with a validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the square description."""
        return f"[Square] {self.__size}/{self.__size}"
