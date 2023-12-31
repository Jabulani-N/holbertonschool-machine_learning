#!/usr/bin/env python3
"""this module coantains the poisson class"""


class Poisson:
    """represents poisson distribution of data"""

    def __init__(self, data=None, lambtha=1.):
        """ represetns a poisson distribution
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
                it will replace lambtha with a calculated lambtha
        """
        # consider a check for forcing lambtha to be a number (int/flaot)
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
            self.lambtha = (sum(data) / len(data))  # lambtha is average

    def factorial(self,k):
        fact = 1
        for i in range(1, k+1):
            fact*=i
        return fact

    def pmf(self, k):
        """return p (pmf) for a given number of successes
        lambtha is used for mu in poisson dist.
        k is used for x in poisson dist.
        if k is out of range (negative p?)
            return 0
        if k is not int, convert to int
        """
        e = 2.7182818285
        if k<0:
            return 0
        return ((e** -self.lambtha) * self.lambtha ** k) /(self.factorial(k))

    def cdf(self, k):
        """return CDF for a given number of successes
        lambtha is used for mu in poisson dist.
        k is used for number of successes
        if k is out of range (negative p?)
            return 0
        if k is not int, convert to int
        """
        kInt = int(k)
        if kInt < 0:
            return 0
        probability = 0

        for num in range(0, kInt + 1):
            probability += self.pmf(num)
        return probability

        # numFact = 1
        # for num in range(1, kInt + 1):
        #     for numFactNum in range (1, num + 1):
        #         numFact *= numFactNum
        #         # print("numFact is ", numFact)
        #     probability += (self.lambtha ** num) / numFact
        #     # print("probability is currently ", probability)
        #     numFact = 1
        # probability *= e ** (-1 * self.lambtha)
        # return probability
