"""
    Another 2 examples of measuring running time.
"""

import time
import timeit


def slow_func():
    # abstract function
    for i in range(1000):
        [str(i) + 'a' for i in range(10000)].sort()


# Easy to remember, but not best approach.
start = time.time()
slow_func()
end = time.time()
print(f'Via time subtraction: {end - start}')

"""
    More correct, !fast! and short approach.
"""

print(f'Via timeit: {timeit.timeit(lambda :slow_func(), number=1)}')
