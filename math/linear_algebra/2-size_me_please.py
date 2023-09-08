#!/usr/bin/env python3
# return the matrix's shape
# this means if input is matrix,
#   get it's length, append it to the first dimension
#   if content of input is matrix, repeat above 2 lines
def matrix_shape(matrix):
    thisDim = 0
    thisDepth = matrix
    shape_so_far = []

    thisDim = len(matrix)
    shape_so_far.append(thisDim)
    while isinstance(thisDepth[0], list) is True:
        thisDim = len(thisDepth)
        shape_so_far.append(thisDim)
        thisDepth=thisDepth[0]
    return shape_so_far
