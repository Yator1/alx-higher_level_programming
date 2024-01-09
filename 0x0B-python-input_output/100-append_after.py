#!/usr/bin/python3

"""
this file contains one function
the function inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    this function inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename (str): name of the file
        search_string (str): the string to search from
        new_string (str): text to insert to a file
    Return:
        none
    """
    with open(filename, "r+", encoding='UTF8') as file:
        read_lines = file.readlines()

        for i, line in enumerate(read_lines):
            if search_string in line:
                read_lines.insert(i + 1, new_string)

        file.seek(0)
        file.writelines(read_lines)
