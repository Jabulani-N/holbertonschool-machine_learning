#!/usr/bin/env python3
"""this module coantains the matrix_transpose function"""


def matrix_transpose(matrix):
    """ changes the horizontal of a matrix to horizontal, and vice versa
    for example:
    0,1
    2,3
    4,5
    becomes
    0,2,4
    1,3,5
    """

    transMatrix = []
    transRow = []
    for column in range(len(matrix[0])):
        for row in matrix:
            transRow.append(row[column])
        transMatrix.append(transRow)
        transRow = []
    return transMatrix
