"""
    The example approach shows how to create nested for-loops in a more
    short and exquisite manner.
"""

from itertools import product

list1 = range(1, 3)
list2 = range(4, 6)
list3 = range(7, 9)

for i1, i2, i3 in product(list1, list2, list3):
    print(i1, i2, i3)
