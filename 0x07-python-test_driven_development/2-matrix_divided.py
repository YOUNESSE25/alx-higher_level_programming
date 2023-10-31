#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix."""

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"

    for element in matrix:

        if not element or not isinstance(element, list):
            raise TypeError(msg)

        if len_e != 0 and len(element) != len_e:
            raise TypeError(msg_size)

        for num in element:
            if not type(num) in (int, float):
                raise TypeError(msg)

        len_e = len(element)

    n = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (n)
