#!/usr/bin/python3
"""Demonstration of Python classes
"""


class Square:
    """Defines a Square

    Attributes:
        size (int): size of the Square
    """
    def __init__(self, size):
        """Initializes a Square object

        Args:
            size (int): size of square
        """
        self.__size = size
