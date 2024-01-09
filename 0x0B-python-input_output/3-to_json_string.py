#!/usr/bin/python3

"""
This file contains one function
that return the JSON represantation of an object(string)
"""
import json


def to_json_string(my_obj):
    """
    This function returns the json representation of an object

    Args:
        my_obj (str): the object to be converted to json

    Return:
        The JSON represantation of the object
    """
    json_rep = json.dumps(my_obj)

    return (json_rep)
