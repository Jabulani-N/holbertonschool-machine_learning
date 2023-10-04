#!/usr/bin/env python3
"""contains class Neuron"""

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

        public instance attributes:
            W: The weights vector for the neuron
                Upon instantiation,
                    initialized using a random normal distribution
            b: The bias for the neuron
                Upon instantiation,
                    initialized to 0
            A: The activated output of the neuron (prediction).
                Upon instantiation,
                    initialized to 0
        """
        # put nx checks nx here so it doesn't start if invalid
        self.b = 0
