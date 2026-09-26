#!/usr/bin/env python3
"""Define a printable square with a position."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the current square position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set and validate the square position."""
        if (type(value) is not tuple or len(value) != 2
                or type(value[0]) is not int
                or type(value[1]) is not int
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the # character."""
        print(self)

    def __str__(self):
        """Return a string representation of the square."""
        if self.__size == 0:
            return ""

        lines = [""] * self.__position[1]
        row = " " * self.__position[0] + "#" * self.__size
        lines.extend([row] * self.__size)

        return "\n".join(lines)
