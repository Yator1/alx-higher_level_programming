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
        __position (int, int): position of the square

    Raises:
        TypeError: if size is not an interger
        ValueError: if size is less then 0
        TypeError: if position is not a tuple of 2 positive numbers
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the  Square object with the specified size and position

        Args:
            size (int): size of the square
            position (int, int): positionof square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
            TypeError: if position is not a tuple of 2 positive numbers
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(
                    isinstance(coord, int)
                    and coord >= 0
                    for coord in position
                    ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ This method  retrieves position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        This method sets the position of the square

        args:
            value (tuple): 2 positive numbers
        Raises:
            TypeError: if not a tupple of 2 positive numbers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        Print the square
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
