#!/usr/bin/python3

"""
This file contains a function
that reads a text file(UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    function read a text file and print it to stdout

    Args:
        filename (file): file to open

    """
    with open(filename, encoding="utf-8") as file_0:
        f_contents = file_0.read()
        print(f_contents, end='')
