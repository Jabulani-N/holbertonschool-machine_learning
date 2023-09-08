#!/usr/bin/env python3

def matrix_shape(matrix):
    """ determines matrix shape.
    Shape meaning it's length, and thength of internal arrays,"""
    thisDim = 0
    thisDepth = matrix
    shape_so_far = []

    while isinstance(thisDepth[0], list) is True:
        thisDim = len(thisDepth)
        shape_so_far.append(thisDim)
        thisDepth = thisDepth[0]
    # once more, for the lowest level containing no more lists
    thisDim = len(matrix)
    shape_so_far.append(thisDim)
    return shape_so_far
