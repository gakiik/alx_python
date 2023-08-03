#!/usr/bin/python3
"""
4-base_geometry module

Define a class BaseGeometry with the area() method.
"""


class BaseGeometry:
    """
    BaseGeometry class.
    """

    def area(self):
        """
        Public instance method to calculate area.
        """
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()
    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
