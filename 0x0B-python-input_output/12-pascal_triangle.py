#!/usr/bin/python3
""" defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tr = triangle[-1]
        tm = [1]
        for i in range(len(tr) - 1):
            tm.append(tr[i] + tr[i + 1])
        tm.append(1)
        triangle.append(tm)
    return triangle
