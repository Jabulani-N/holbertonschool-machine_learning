#!/usr/bin/env python3
"""import is permitted"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """concatenates arrays.
    numpy can concatenate any nyumber of arrays this way
    """
    return np.concatenate((mat1, mat2), axis)
