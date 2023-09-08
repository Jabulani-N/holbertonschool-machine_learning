#!/usr/bin/env python3
"""this module coantains the cat_arrays function"""


def cat_arrays(arr1, arr2):
    """ concatenates array elements
    You can assume that arr1 and arr2 are lists of ints/floats
    """

    catArr = []
    for dim1 in arr1:
        catArr.append(dim1)
    for dim1 in arr2:
        catArr.append(dim1)

    return catArr
