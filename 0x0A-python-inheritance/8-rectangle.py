#!/usr/bin/python3
"""Working with Python inheritance"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle object"""

    def __init__(self, width, height):
        """Initializes a Rectangle object"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
