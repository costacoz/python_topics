"""
    Example of built-in caching module.

    @functools.lru_cache(maxsize=None, typed=False)

    maxsize: how many results of this function call can be cached at most,
    if None, there is no limit, when set to a power of 2, the performance
    is the best

    typed: If True, calls of different parameter types will be cached
    separately.
"""

import timeit
from functools import lru_cache


@lru_cache(None)
def add(x, y):
    print(f'adding: {x} + {y}')
    return x + y


print(add(1, 2))
print(add(1, 3))
print(add(1, 3))  # notice, how this time it doesn't output "adding: 1 + 3"


@lru_cache(None)
def fib(n):
    """
        Without caching this function takes ~3 seconds to execute, whereas
        with caching it executes 0.0000018 seconds
    """
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


print(f'fibonacci of (35): {timeit.timeit(lambda: fib(35), number=1)}')
