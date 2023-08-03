#!/usr/bin/python3
"""
3-base_geometry module

Define an empty class BaseGeometry.
"""

class BaseGeometry:
    """
    An empty class representing BaseGeometry.
    """
    pass


if __name__ == "__main__":
    bg = BaseGeometry()
    print(bg)
    bg_attrs = [attr for attr in dir(bg) if attr != "__init_subclass__"]
    print(bg_attrs)
    
    BaseGeometry_attrs = [attr for attr in dir(BaseGeometry) if attr != "__init_subclass__"]
    print(BaseGeometry_attrs)
