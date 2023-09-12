#!/usr/bin/env python3
"""this module coantains the summation_i_squared function"""


def summation_i_squared(n):
    """ calculates the summation of i squared
    for i = 0 up to n
    without loops
    """

    if isinstance(n, int) is False:
        return None

    if n == 0:
        return 0
    if n < 0:
        return None

    return (n * (n + 1) * (2 * n + 1))/6
