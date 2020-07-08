"""
    Example of using Python's regex module.

    When simple cases, highly recommended to use sting methods, like:
    'tea for too'.replace('too', 'two')
"""

import re

regex = re.findall(r'[A-z]+', 'Luma&Buma, went around b00xes')
print(regex)

x = 'tea for too'.replace('too', 'two')
print(x)
