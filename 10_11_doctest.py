"""
    Examples of tests approaches:
        1. doctest;
        2. unittest.
"""

# **** testing via doctest ****

import doctest


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> average([20, 30, 70])
    40.0
    """
    return sum(values) / len(values)


doctest.testmod()  # automatically validate the embedded tests
