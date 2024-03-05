#!/usr/bin/python3

"""
This module contains one function (MyList)
"""

class MyList(list):
    """
    This method that prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
