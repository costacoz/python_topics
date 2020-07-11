"""
    array module provides array() object that is more compact than list and
    stores homogenous items.
"""

from array import array

a = array('H', [4000, 10, 700, 22222])  # H means unsigned byte
print(sum(a))
print(a[1:3])

"""
    collections module has deque object that is like list, but with faster
    appends and pops from the left side. However it's slower with lookups in
    the middle. It is best for implementing queues and breadth first tree
    searches.
"""

from collections import deque

d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

"""
    bisect module provides support for maintaining a list in sorted order 
    without having to sort the list after each insertion. 
    For long lists of items with expensive comparison operations, this can be 
    an improvement over the more common approach.
    More here:
    https://docs.python.org/3/library/bisect.html#module-bisect
"""

import bisect

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

"""
    heapq module provides functions for implementing heaps based on regular 
    lists. The lowest valued entry is always kept at position zero. 
    This is useful for applications which repeatedly access the smallest 
    element but do not want to run a full list sort.
"""

from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)  # rearrange the list into heap order
heappush(data, -5)  # add a new entry
print([heappop(data) for i in range(3)])  # fetch the three smallest entries
