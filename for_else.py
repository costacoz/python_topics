"""
    In for-loop, else statement executes when for loop haven't executed
    break.
"""

for i in range(10):
    if 1 == 2:
        break
else:
    print('break never happened!')

for i in range(10):
    if i == 2:
        break
else:
    print('Did break happen?')
