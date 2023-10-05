#!/usr/bin/env python3
"""contains class Neuron"""


import numpy as np


class Neuron:
    """performs binary classification"""

    def __init__(self, nx):
        """nx is number of input features
        If nx is not an integer,
            raise a TypeError with the exception:
                nx must be an integer
        If nx is less than 1,
            raise a ValueError with the exception:
                nx must be a positive integer

        private instance attributes:
            _W: The weights vector for the neuron
                Upon instantiation,
                    initialized using a random normal distribution
            _b: The bias for the neuron
                Upon instantiation,
                    initialized to 0
            _A: The activated output of the neuron (prediction).
                Upon instantiation,
                    initialized to 0
        """
        if isinstance(nx, int) is False:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self._b = 0
        self._A = 0

        self._W = np.random.normal(size=(1, nx))
