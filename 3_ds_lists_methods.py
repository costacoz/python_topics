"""
    This file contains examples for each method that list type has.
"""

"""
    list.append(element)
"""


def list_append():
    """
        list.append(element) example
    """
    alpha_list = ['cat', 'dog', 'hamster']
    alpha_list.append('fox')
    print(alpha_list)


print(list_append.__doc__)
list_append()

"""
    list.extend(iterable)
"""


def list_extend():
    """
        list.extend(iterable) example
    """
    beta_list = ['hibiscus', 'palm', 'coconut']
    gamma_list = ['sunflower', 'rose', 'cactus']  # iterable list
    delta_list = {'mushroom', 'garlic'}  # notice dic, which is iterable too
    beta_list.extend(gamma_list)
    beta_list.extend(delta_list)
    print(beta_list)


print(list_extend.__doc__)
list_extend()

"""
    list.insert(i, x) example. Being used as opposite to append(), when
    need to insert element not into end of the list. 
"""


def list_insert():
    """
        list.insert(i, x) example
    """
    epsilon = ['cat', 'dog', 'fox']
    epsilon.insert(0, 'hamster')
    epsilon.insert(2, 'frog')
    print(epsilon)


print(list_insert.__doc__)
list_insert()

"""
    list.remove(el) example.
"""


def list_remove():
    """
    list.remove(el) example.
    """
    zeta = ['fox', 'lion', 'fish']
    zeta.remove('lion')
    print(zeta)
    try:
        zeta.remove('BOBBY!')
    except ValueError:
        print('element to remove is not in the list')


print(list_remove.__doc__)
list_remove()

"""
    list.pop([i]) example. Square brackets - optional.
"""


def list_pop():
    """
    list.pop([i]) example.
    """
    eta = ['gold', 'silver', 'bronze', 'copper']
    eta.pop(1)
    print('after pop(1): {0}'.format(eta))
    eta.pop()
    print('after pop(): {0}'.format(eta))


print(list_pop.__doc__)
list_pop()

"""
    list.clear() example.
"""


def list_clear():
    """
    list.clear() example.
    """
    theta = ['dog', 'shark', 'hamster']
    theta.clear()
    print('after clear(): {0}'.format(theta))


print(list_clear.__doc__)
list_clear()

"""
    list.index(el[, start[, end]]) example. 'start' and 'end' notation works as
    slice (list[start:end]), therefore end is not included into lookup range.
    Invocation with specified range must be invoked with exception wrapping.
"""


def list_index():
    """
    list.index(el[, start[, end]]) example.
    """
    iota = ['cat', 'frog', 'fish', 'bird']
    print("index of 'frog': {0}".format(iota.index('frog')))
    try:
        print("index(frog, 2, 3) of 'frog': {0}".format(
            iota.index('frog', 2, 3)))
    except ValueError:
        print('not found')

    try:
        print("index(frog, 0, 2) of 'frog': {0}".format(
            iota.index('frog', 0, 2)))
    except ValueError:
        print('not found')


print(list_index.__doc__)
list_index()

"""
    list.count(el) example.
"""


def list_count():
    """
        list.count(el) example.
    """
    kappa = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'alpha']
    print("alpha word count: {}".format(kappa.count('alpha')))


print(list_count.__doc__)
list_count()

"""
    list.sort(key=None, reverse=False) example.
"""


def list_sort():
    """
        list.sort(key=None, reverse=False) example.
    """
    kappa = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    print('kappa before sort: {}'.format(kappa))
    kappa.sort()
    print('kappa after sort: {}'.format(kappa))


print(list_sort.__doc__)
list_sort()

"""
    list.reverse() example.
"""


def list_reverse():
    """
        list.reverse() example.
    """
    kappa = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    kappa.reverse()
    print(kappa)


print(list_reverse.__doc__)
list_reverse()

# analog is str[::-1]
print('first_edition'[::-1])

"""
    list.copy() example.
"""


def list_copy():
    """
        list.copy() example.
    """
    omicron = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    omega = omicron.copy()
    print('initial omicron: {}'.format(omicron))
    print('omega: {}'.format(omega))
    omicron = omicron[2:]
    print('omicron after modify: {}'.format(omicron))
    print('omega: {}'.format(omega))


print(list_copy.__doc__)
list_copy()
