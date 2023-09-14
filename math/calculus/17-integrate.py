#!/usr/bin/env python3
"""this module coantains the poly_integral function"""


def poly_integral(poly, C=0):
    """ integrates polynomial represented by list poly
    with respect to x.
    each posioitn is a power of x
    for example: [1, 3, 5] = 1x^0 + 3x^1 + 5x^2
    remember that x^0 = 1, so 5x^0 == 5
    C is the constant that got deleted via deriving
    """

    if isinstance(poly, list) is False or\
       len(poly) == 0 or\
       isinstance(C, int) is False:
        return None
    if len(poly) == 1:
        return [C, poly[0]]
    integratedPoly = []
    poly.reverse()
    for position in range(len(poly) - 1):
        integratedPoly.append(poly[position] * (len(poly) - 1 - position))
    integratedPoly.reverse()
    return integratedPoly
