#!/usr/bin/python3

"""
This module contains one class BaseGeometry
"""


class BaseGeometry:
    """
    This class contains the method area() and integer_validator
    Raises:
        Exception - area() is not implemented
        TypeError - <name> must be an integer
        ValueError - <name> must be greater the 0
    """
    def area(self):
        """This method raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
