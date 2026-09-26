#!/usr/bin/env python3
"""Define mixins and a Dragon class."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Print the swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Print the flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon that can swim and fly."""

    def roar(self):
        """Print the dragon's roar."""
        print("The dragon roars!")
