"""
    Comparison of bad and good approach of using list as a queue.
    deque demonstration example.
"""

from collections import deque
from timeit import timeit

def queue_bad():
    """
        Wrong way of using list as queue (very slow)
    """
    queue = ["dog", "cat", "fish", "bear"]
    for n in range(1000):
        queue.pop(0)
        queue.append("crab")

def queue_deque():
    """
        Correct way of using list as queue
    """
    queue = deque(["dog", "cat", "fish", "bear"])
    for n in range(1000):
        queue.popleft()
        queue.append('crab')

print(timeit(queue_bad, number=60000)) # 9.5892716
print(timeit(queue_deque, number=60000)) # 7.6286140
