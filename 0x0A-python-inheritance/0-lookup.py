#!/usr/bin/python3

"""
This module contains one function (lookup)
"""


def lookup(obj):
    """
    this function returns the list of available attrubutes and methods
    of an object
    Args:
        obj: the object to find attributes of
    """
    return ([attr_meth for attr_meth in dir(obj)])
