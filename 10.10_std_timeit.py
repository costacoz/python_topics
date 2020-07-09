"""
    Example of timeit module usage to measure execution time.
"""

import random
from timeit import Timer, timeit

t1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()

print(f't1 = {t1}')

code_block = """
a,b = b,a
"""

t2 = Timer(code_block, 'a=1; b=2').timeit()

print(f'f2 = {t2}')


def heavy_function(nums):
    nums.copy().sort()
    return nums


sample = random.sample(range(1000), 500)

print(timeit(
    stmt='heavy_function(nums)',
    setup='nums=sample',
    number=80000,
    globals=globals()))
