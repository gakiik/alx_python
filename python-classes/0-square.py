# -*- coding: utf-8 -*-
"""Square module.

This module defines the Square class, which represents a square with a private size attribute.
"""

class Square:
    """Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initialize the Square instance with a given size.
        area(self): Calculate the area of the square.
    """

    def __init__(self, size):
        """Initialize the Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
