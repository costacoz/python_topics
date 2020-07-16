"""
    Example of partial functions.

    Partial functions allow one to derive a function with x parameters
    to a function with fewer parameters and fixed values set for
    the more limited function.
"""

from functools import partial


def multiply(x, y):
    return x * y


# create a new function that multiplies by 2
dbl = partial(multiply, 2)
print(dbl(4))


# Exercise

def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x


new_func = partial(func, 10, 4, 2)
print(new_func(4))
