#!/usr/bin/python3

"""
This file contains one function that
appends a string at the end of a text file
it returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    this function appends a string at the end of a text file
    Returns the number of character added

    Args:
        filename: the name of the file to be appended
        text: the text to be appended
    Return:
        numbers of characters to be appended
    """
    with open(filename, 'a', encoding="utf-8") as file_2:
        file_2.write(text)
        characters_appending = len(text)

    return (characters_appending)
