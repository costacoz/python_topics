"""
    example of using python's regex module.

    when simple cases, highly recommended to use sting methods, like:
    'tea for too'.replace('too', 'two')
"""

import re

regex = re.findall(r'[a-z]+', 'luma&buma, went around b00xes')
print(regex)

x = 'tea for too'.replace('too', 'two')
print(x)
