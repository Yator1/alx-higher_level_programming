#!/usr/bin/python3

"""
This module contains one class.
the class is defining a square
"""

class Square:
    """
    this class defines a square using a private attribute size
    Attributes:
        __size (int): size of the square

    Exceptions:
        TypeError: if size is not an interger
        ValueError: if size is less then 0
    """
    def __init__(self, size=0):
        """
        this method instantiates the attribute size
        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
