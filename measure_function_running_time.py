"""
    Another example of measuring running time.
    More correct approach would be to use example from 10.10_std_timeit.py
"""

import time

start = time.time()

# abstract function
for i in range(1000):
    [str(i)+'a' for i in range(10000)].sort()

end = time.time()

print(end - start)