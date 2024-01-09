#!/usr/bin/python3

"""
This file contains one function
it returns an object represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    this Function returns an object(Python data structure) represented
    by a JSON string

    Args:
        my_str (str): the JSON string

    Return:
        The object
    """
    return (json.loads(my_str))
