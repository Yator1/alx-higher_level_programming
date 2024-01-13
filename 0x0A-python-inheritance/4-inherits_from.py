#!/usr/bin/python3

"""
this module contains one function inherits_from
"""


def inherits_from(obj, a_class):
    """
    This function checks if an object is an instance of a class that inherited
    directly or indirectly from the specified class
    Returns true or false.
    """
    return (isinstance(obj, a_class) and issubclass(type(obj), a_class) and
            type(obj) is not a_class)
