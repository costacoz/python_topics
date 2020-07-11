"""
    Floating point arithmetic in computers is approximate due to architecture.

    So decimal module offers a Decimal datatype for decimal floating point
    arithmetic.

    Compared to the built-in float implementation of binary floating point,
    the class is especially helpful for

    * financial applications and other uses which require exact decimal
    representation,

    * control over precision,

    * control over rounding to meet legal or regulatory requirements,

    * tracking of significant decimal places, or

    * applications where the user expects the results to match
    calculations done by hand.
"""

from decimal import *

# calculate 5% tax on 70 cent bill, using Decimal will give correct result
print(f'(Decimal) 0.70 * 1.05 = ', round(Decimal('0.70') * Decimal('1.05'), 2))

# via regular float operation it will give wrong answer:
print(f'(regular float) 0.70 * 1.05 = ', round(.70 * 1.05, 2))

# Another example of getting modulo calculation with floating point numbers:
print(f'1.00 % 0.10 via Decimal:', Decimal('1.00') % Decimal('.10'))

# again, float type gives wrong result:
print(f'1.00 % 0.10 via regular float = {1.00 % 0.10}')

print(sum([Decimal('0.1')] * 10) == Decimal('1.0'))

print(sum([0.1] * 10) == 1.0)
