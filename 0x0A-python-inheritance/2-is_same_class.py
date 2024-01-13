#!/usr/bin/python3

"""
this module contains one function (is_same_class)
"""


def is_same_class(obj, a_class):
    """
    This function checks if an object is an instance of the specified class
    Returns: True if same otherwise False
    """
    return (type(obj) == a_class)
