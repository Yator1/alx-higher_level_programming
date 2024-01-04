#!/usr/bin/python3

"""
This module contains one class rectagle
"""


class Rectangle:
    """
    Defines a rectangle.

    Attribute:
        __width (int): the widht of the rectangle
        __height (int): the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initialises the private attributa widht and height

        Args:
            width (int): width of rectangle
            height (int):height of rectangle

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is less than zero
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        retrieves the width
        Returns:
            int: width of the rectangle
        """
        return (self.__width)

    @property
    def height(self):
        """
        retrieves the height
        Returns:
            int: height of the rectangle
        """
        return (self.__height)

    @width.setter
    def width(self, value):
        """
        sets the width value
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        sets the height value
        Raises:
            TypeError: if length is not an integer
            ValueError: if length is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returhs the area of the rectangle """
        return (self.__height * self.__width)

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))
