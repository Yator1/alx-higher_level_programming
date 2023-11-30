#!/usr/bin/python3
from magic_calculation_102 import add
def magic_calculation(a, b):
    if a < b:
        _sum = add(a, b)
        for i in range(4, 6):
            _sum = add(_sum, i)
        return (_sum)
