#!/usr/bin/python3
"""
This module contains one funtion
it add two integers or floats and returns the sum
"""


def add_integer(a, b=98):
    """
    function that adds two integers and returns the sume

    Args:
        a (int or float): The first number.
        b (int or float, optional): the second number. Defaults set to 98

    Raises:
        TypeError: If 'a' or 'b' is not an integer or float

    Return:
        int: The sum of 'a' anb 'b'
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    _sum = int(a) + int(b)

    return (_sum)
