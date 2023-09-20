#!/usr/bin/env python3
"""this module coantains the poisson class"""

class Poisson:
    def __init__(self, data=None, lambtha=1.):
        """ represetns a poisson distribution
        data is a list of integers, data is used to estimate the distribution
            I assume this is the source from which we
            determine the "average" that poisson distribution requires
        lambtha (float) is the expected number of occurences in a given time frame
            it seems like this means 'average'

        If lambtha is not a positive value or equals to 0,
            raise a ValueError with the message
                'lambtha must be a positive value'
        If data is not given,
            skip calculations and assume the average is lambtha
        If data is not a list,
            raise a TypeError with the message data must be a list
        If data does not contain at least two data points,
            raise a ValueError with the message data must contain multiple values

            If data DOES exist
                it will replace lambtha with a calculated lambtha
        """
        if  data == None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = lambtha
        elif isinstance(data, list) is False:
            raise TypeError("data must be a list")
        elif len(data) < 2:
            raise ValueError("data must contain multiple values")
        # we do not use else here, because
        # data == none, lambtha = 1. (no data given) is valid


