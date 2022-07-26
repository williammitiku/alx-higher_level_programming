#!/usr/bin/python3
"""Defin a matric division function"""


def matrix_divided(matrix, div):
    """Divid all element if a mattrix by divisior.

    Args:
        Matrix(list):  list of lists of integers or floats.
        div: divisor for all element of a matrix.
    Raise:
         TypeError: if a mattrix contain non-number.
         TypeError: if all row size of a mattrix is not equal.
         TypeError: if div is not int or float.
         ZeroDivisionError: if div is zero.
    Return:
         a new matrix that result from old mattrix divided by div
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(ele, int) or (isinstance(ele, float))
                for ele in[num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and (div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
