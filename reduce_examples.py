"""
    Example of reduce.

    reduce(func, iterable[, initial])

    iterable - should have at least 1 element, otherwise Exception thrown
"""

from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]


def custom_sum(first, second):
    return first + second


result = reduce(custom_sum, numbers)
print(result)

result = reduce(custom_sum, numbers, 1)
print(result)
