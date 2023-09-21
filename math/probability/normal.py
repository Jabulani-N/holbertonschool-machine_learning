#!/usr/bin/env python3
"""this module coantains the normal class"""
e = 2.7182818285
pi = 3.1415926536


class Normal:
    """ represents normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        if stddev <= 0:
            raise ValueError("stddev must be a positive value")
        else:
            self.stddev = float(stddev)
        self.mean = mean

        if isinstance(data, list) is False and\
                data is not None:
            raise TypeError("data must be a list")
        elif isinstance(data, list) and\
                len(data) < 2:
            raise\
                ValueError("data must contain multiple values")
        elif data is not None:
            self.mean = (sum(data) / len(data))  # mean is average
            # calculate standard deviation (square root of variance)
            xMinusxBar = []
            xMinusxBarSquared = []
            for index in range(0, len(data)):
                xMinusxBar.append(data[index] - self.mean)
                xMinusxBarSquared.append(xMinusxBar[index] ** 2)
            self.stddev = (sum((xMinusxBarSquared))\
                            / len(xMinusxBarSquared)) ** 0.5
