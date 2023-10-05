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
            __W: The weights vector for the neuron
                Upon instantiation,
                    initialized using a random normal distribution
            __b: The bias for the neuron
                Upon instantiation,
                    initialized to 0
            __A: The activated output of the neuron (prediction).
                Upon instantiation,
                    initialized to 0
        """
        if isinstance(nx, int) is False:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__b = 0
        self.__A = 0
        self.__W = np.random.normal(size=(1, nx))

    @property
    def W(self):
        """getter"""
        return self.__W

    @property
    def b(self):
        """getter"""
        return self.__b

    @property
    def A(self):
        """getter"""
        return self.__A

    def forward_prop(self, X):
        """Calculates the forward propagation of the neuron
        X is numpy.ndarray of shape (nx, m) & contains the input data
            nx is the number of input features to the neuron
            m is the number of examples

        Updates the private attribute __A
            The neuron should use a sigmoid activation function

        Returns the private attribute __A
        """
        # I need to multiply everything in X array by the weight
        # weight is self.W()
        # weighted_X = X * 1
        # above is where I need to multiply x by wieghts
        self.__A = self.sigmoid(np.matmul(self.__W, X) + self.__b)
        return self.__A

    def sigmoid(self, x):
        """sigmoid function used in propagation"""
        sig = 1 / (1 + np.exp(-1 * x))
        return sig

    def cost(self, Y, A):
        """determines cost
        uses
            1.0000001 - A
        anytime there would otherwise be a
            1 - A
        Y is numpy.ndarray
            with shape (1, m)
            contains the correct labels for the input data
        A is a numpy.ndarray
            with shape (1, m)
            containing the activated output of the neuron for each example
        """
        m = Y.shape[1]
        # need to multiple -1/m by sum
        loss = (-1 / m) * np.sum(Y *
                                 np.log(A) + ((1.0000001 - A) *
                                              np.log(1.0000001 - A)))
        return loss
