#!/usr/bin/env python3
"""this module coantains the exponential class"""
e = 2.7182818285
pi = 3.1415926536


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

    def pdf(self, x):
        """Calculates value of the PDF for a given time period
        x is the time period
        Returns the PDF value for x
        If x is out of range, return 0
        0 is not a special case
        """
        if x < 0:
            return 0
        return self.lambtha * e ** (-1 * self.lambtha * x)

    def cdf(self, x):
        """ sum of values up to x"""
        if x < 0:
            return 0
        total = 0
        for num in range(1, x):
            total += self.pdf(num)
        return total
