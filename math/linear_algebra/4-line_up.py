#!/usr/bin/env python3
"""this module coantains the add_arrays function"""


def add_arrays(arr1, arr2):
    """ adds array elements
    assume bot arr's are same shape
    and filled with int/float
    """

    sumMatrix = []

    if len(arr1) != len(arr2):
        return None

    for column in range(len(arr1)):
        sumMatrix.append(arr1[column] + arr2[column])
    return sumMatrix
