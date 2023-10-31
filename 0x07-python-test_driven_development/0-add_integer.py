#!/usr/bin/python3
"""This module is composed by a function that adds 2 integers."""


def add_integer(a, b=98):
    """ addition 2 numb"""

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
