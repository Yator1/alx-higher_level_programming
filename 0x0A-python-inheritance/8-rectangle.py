#!/usr/bin/python3

"""
This module contains one class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class inherits from class BaseGeometry
    Attributes:
        width (int): the width of rectangle
        height(int): the height of rectangle.
    """
    def __init__(self, width, height):
        self.width = 0
        self.height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        #self.__width = width
        #self.__height = height
