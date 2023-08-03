class Square:
    """Represents a square with a private size attribute."""

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
