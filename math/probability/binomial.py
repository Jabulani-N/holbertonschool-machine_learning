#!/usr/bin/env python3
"""this module coantains the binomial class"""
e = 2.7182818285
pi = 3.1415926536


class Binomial:
    """ represents Binomial distribution
    calculate p first, then n, then recalculate p
    """

    def __init__(self, data=None, n=1, p=0.5):
        if n <= 0:
            raise ValueError("n must be a positive value")
        else:
            self.n = int(n)

        if p < 0 or p > 1:
            raise ValueError("p must be greater than 0 and less than 1")
        self.p = float(p)

        if isinstance(data, list) is False and\
                data is not None:
            raise TypeError("data must be a list")
        elif isinstance(data, list) and\
                len(data) < 2:
            raise\
                ValueError("data must contain multiple values")
        elif data is not None:
            pass  # where p & n would be calculated
