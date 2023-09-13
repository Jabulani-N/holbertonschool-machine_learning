#!/usr/bin/env python3
"""this module coantains the poly_derivative function"""


def poly_derivative(poly):
    """ derives polynomial represented by list poly
    with respect to x.
    each posioitn is a power of x
    for example: [1, 3, 5] = 1x^2 + 3x^1 + 5x^0
    remember that x^0 = 1, so 5x^0 == 5
    """

    if isinstance(poly, list) is False or\
       len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    derivedPoly = []

