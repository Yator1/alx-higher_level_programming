#!/usr/bin/python3
"""
This module contains one class.
this class defines a square
"""

class Square:
    """
    this class defines a square using a private attribute size

    Attributes:
        __size (int): size of the square

    Raises:
        TypeError: if size is not an interger
        ValueError: if size is less then 0
    """
    def __init__(self, size=0):
        """
        Initializes the  Square object with the specified size

        Args:
            size (int): size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        This method calculates the area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        This method retrieves size
        Returns:
            int: the value of size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        this method sets the value of size
        Args:
            value (int): the value to set size with
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
