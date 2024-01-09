#!/usr/bin/python3

"""
this file contains one funtion
that prints plascals triangle
"""


def pascal_triangle(n):
    """
    Function that prints pascals triangle

    Args:
        n (int): Number of rows in pascals triangle
    Returns:
        list: List representing pascals triangle
    """
    if n <= 0:
        return ([])

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return (triangle)
