#!/usr/bin/python3

'''
This file contains one function
That creates an object from a json file
'''

import json


def load_from_json_file(filename):
    '''
    this function creates an object from a JSON file

    Args:
        filename (str): the file to create the object with
    Return:
        Object: the pbject creates from the JSON file.
    '''
    with open(filename, encoding='utf-8') as file_6:
        obj = json.load(file_6)

    return (obj)
