"""
    List comprehensions or simply listcomp.
"""

squares = []

for x in range(10):
    squares.append(x ** 2)

print(squares)

# map(function, iterable, ..)
squares_2 = list(map(lambda z: z ** 2, range(10)))

print(squares_2)

# create elements inside list, using for loop
squares_3 = [y ** 2 for y in range(10)]

print(squares_3)

# additional example for creating list, using for loop
frogs = ['frog{}'.format(f) for f in range(7)]
print(frogs)

# additional example for creating list, using for loop
numbers = [n for n in [1, 2, 3, 4, 5]]
print(numbers)

comb = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(comb)


# 1. What we are doing;
# 2. How many times we are doing it;
# 3. Check if we can do it at all.

pairs = [ (a, b) for a in ['Peter', 'Shaun', 'Michael']
          for b in ['Peter', 'Shaun', 'Michael']
          if a != b
          ]

print(pairs)
