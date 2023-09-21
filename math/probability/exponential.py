#!/usr/bin/env python3
"""this module coantains the exponential class"""


class Exponential:
    """represents exponential distribution of data
    data is a list of integers, data is used to estimate the distribution
            I assume this the source from which we
            determine the "average" that poisson distribution requires
        lambtha (float) is expected number of occurences in a given time frame
            it seems like this means 'average'

        If lambtha is not a positive value or equals to 0,
            raise a ValueError with the message
                'lambtha must be a positive value'
        If data is not given,
            skip calculations and assume the average is lambtha
        If data is not a list,
            raise a TypeError with message data must be a list
        If data does not contain at least two data points,
            raise ValueError with message data must contain multiple values

        If data DOES exist
            replace lambtha with a calculated lambtha
    """

    def __init__(self, data=None, lambtha=1.):
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        else:
            self.lambtha = float(lambtha)

        if isinstance(data, list) is False and\
                data is not None:
            raise TypeError("data must be a list")
        elif isinstance(data, list) and\
                len(data) < 2:
            raise\
                ValueError("data must contain multiple values")
        elif data is not None:
            self.lambtha = 1 / (sum(data) / len(data))  # lambtha = 1 / average
