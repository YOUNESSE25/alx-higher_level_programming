#!/usr/bin/python3

def sqr(x):
    return (x**2)


def square_matrix_simple(matrix=[]):
    n = matrix[:]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            n[i] = list(map(sqr, matrix[i]))
    return n
