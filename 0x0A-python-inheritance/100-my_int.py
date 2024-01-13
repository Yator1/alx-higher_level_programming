#!/usr/bin/python3

"""
This module contains one class (MyInt)
"""


class MyInt(int):
    """
    This class inherits from class int
    Attributes:
        other
    """
   def __eq__(self, other):
       return int.__ne__(self, other)

   def __ne__(self, other):
       return int.__eq__(self, other)
