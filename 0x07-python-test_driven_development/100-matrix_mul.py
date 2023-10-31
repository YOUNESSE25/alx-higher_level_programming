#!/usr/bin/python3
"""Module composed by a function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for ele in m_a:
        if not isinstance(ele, list):
            raise TypeError("m_a must be a list of lists")

    for ele in m_b:
        if not isinstance(elems, list):
            raise TypeError("m_b must be a list of lists")

    for lists in m_a:
        for ele in lis:
            if not type(ele) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for ele in lis:
            if not type(ele) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    lng = 0

    for ele in m_a:
        if lng != 0 and lng != len(ele):
            raise TypeError("each row of m_a must be of the same size")
        lng = len(ele)

    lng = 0
    for ele in m_b:
        if lng != 0 and lng != len(ele):
            raise TypeError("each row of m_b must be of the same size")
        lng = len(ele)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    r = []
    i = 0
    for a in m_a:
        rr = []
        ii = 0
        num = 0
        while (ii < len(m_b[0])):
            num += a[i] * m_b[i][ii]
            if i == len(m_b) - 1:
                i = 0
                ii += 1
                rr.append(num)
                num = 0
            else:
                i += 1

        r.append(rr)

    return r1
