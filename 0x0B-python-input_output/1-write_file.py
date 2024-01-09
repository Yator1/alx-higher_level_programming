#!/usr/bin/python3

"""
This file contains one function
The function writes and returns the number of characters written on the files.
"""


def write_file(filename="", text=""):
    """
    This functions writes a string to a text file(UTF8)
    Retruns the characters written

    Args:
        filename: the file name to be written to
        text: the text to be written
    Return:
        numbers of characters on the text
    """
    with open(filename, 'w', encoding="utf-8") as file_1:
            file_1.write(text)
            characters = len(text)

            return (characters)
