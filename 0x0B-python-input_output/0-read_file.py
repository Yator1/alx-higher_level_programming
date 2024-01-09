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
    with open(filename, encoding="UTF8") as file_a:
        for line in file_a:
            print(line, end='')
