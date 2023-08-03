#!/usr/bin/python3
"""
3-base_geometry module

Define an empty class BaseGeometry.
"""


class BaseGeometry:
    """
    An empty class representing BaseGeometry.
    """

    def __dir__(self):
        """
        Override the dir() method to exclude __init_subclass__ from the list of attributes.
        """
        attributes = super().__dir__()
        # Exclude __init_subclass__ from the list of attributes
        attributes = [attr for attr in attributes if attr != "__init_subclass__"]
        return attributes


if __name__ == "__main__":
    bg = BaseGeometry()
    print(bg)
    print(dir(bg))
    print(dir(BaseGeometry))
