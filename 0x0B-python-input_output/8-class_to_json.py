#!/usr/bin/python3

"""
This file contains one function
that it returns the dictionary description with simple data structure
for json serialization of an object
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description with simple data structure
    for json serialization of an object

    Args:
        obj: an instance of a class
    Returns:
        the dictionary description with simple data structure
    """
    data = vars(obj)
    json_dict = {}

    for key,  value in data.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return (json_dict)
