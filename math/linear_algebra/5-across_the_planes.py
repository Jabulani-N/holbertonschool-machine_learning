#!/usr/bin/env python3
"""this module coantains the add_arrays function"""


def add_matrices2D(mat1, mat2):
    """ adds array elements
    assume bot arr's are same shape
    and filled with lists
        lists are filled with int/float
    """

    if len(mat1) != len(mat2):
        return None
    if len(mat1[0]) != len(mat2[0]):
        return None

    sumMatrix = []
    sumRow = []

    # Consider replacing terms row, column
    # with terms dimensiton 1, dimension2
    # so higher dimensions will come naturally
    for row in range(len(mat1)):
        for column in range(len(mat1[row])):
            sumRow.append(mat1[row][column] +
                          mat2[row][column])
        sumMatrix.append(sumRow)
        sumRow = []

    return sumMatrix
