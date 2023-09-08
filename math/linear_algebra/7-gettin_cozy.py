#!/usr/bin/env python3
"""this module coantains the cat_arrays function"""


def cat_matrices2D(mat1, mat2, axis=0):
    """ concatenates array elements
    You can assume that mat1 and mat2 are 2D matrices containing ints/floats

    if lengthes do not align, return None
    axis 0 concatenaes mat 2 to dimension 0
    axis 1 concatenates contents of mat2's dimensoin 1
    to end of each dimension 1 entry of mat1
    """

    catArr = []
    catRow = []
    if axis == 0:
        catArr = mat1 + mat2
    elif axis == 1:
        for row in range(len(mat1)):
            catRow = mat1[row] + mat2[row]
            catArr.append(catRow)
    return catArr
