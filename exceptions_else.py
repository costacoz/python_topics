"""
    Exception else statement example.
    Else statement happens, when try block executed successfully.
    Else block should go before finally.
"""

i = 1

try:
    i += 1
    # raise Exception
except:
    print('except block reached')
else:
    print('else block reached')
finally:
    print('finally block reached')
