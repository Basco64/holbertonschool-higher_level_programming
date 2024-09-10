#!/usr/bin/python3

"""
Module for dividing a matrix.

Contains the matrix_divided function, which divides all
the numbers in the matrix by the divisor, rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):

    """
    Divides all the numbers in the matrix by the divisor and returns it.

    @matrix: the matrix to be modified
    @div: the divisor

    Return: The matrix
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    line_len = None

    for line in matrix:
        if not isinstance(line, list) or len(line) == 0:
            raise TypeError(error_msg)

        if line_len is None:
            line_len = len(line)
        elif len(line) != line_len:
            raise TypeError("Each row of the matrix must have the same size")

        for num in line:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError(error_msg)

    return [[round(num / div, 2) for num in line] for line in matrix]
