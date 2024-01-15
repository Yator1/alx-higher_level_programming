#!/usr/bin/python3

'''
This module contains one function
the function divides each element of a matrix by a divisor
return a new matrix
'''


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix

    Args:
        matrix (list): the list of integers or floats to be divided
        div (int or float): the divisor

    Raises:
        TypeError: if matrix is not a list of integers or floats
            if the rows of the matrix are not the same
            if div is not an integer of float
        ZeroDivisionError: if div us equal to 0

    Returns:
        list: a new matrix with divided elements rouded up to 2 decimal places
    """

    # validating matrix input
    err_message = "matrix must be a matrix (list of lists) of integers/floats"
    if (
            not isinstance(matrix, list)
            or not all(isinstance(row, list) for row in matrix)
            or not all(
                all(isinstance(number, (int, float)) for number in row)
                for row in matrix)
            ):
        raise TypeError(err_message)

    # validate matrix row sizes
    row_size = set(len(row) for row in matrix)
    if len(row_size) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # check div input
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # check if div == 0:
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # divide and round off into a new matrix
    new_mtrix = [
            [round(element / div, 2) for element in row] for row in matrix
            ]

    return (new_mtrix)
