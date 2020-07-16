"""
    map and reduce come built-in (__builtins__ module).
    Meanwhile, reduce needs to be imported from functools module.
"""


def simple_map():
    """
        Simplest map case.
    """
    codes = ['1a', '2x']
    result = map(str.upper, codes)  # returns map object (iterable)
    result = list(result)  # convert to list, to be able to output normally.
    print(result)


simple_map()


def with_lambda():
    """
        Example with lambda usage.
    """
    strs = ['vub,bop', 'bix,leb']
    result2 = map(lambda x: x.split(','), strs)
    print(list(result2))


with_lambda()


def multiple_arguments():
    """
        Example with multiple arguments with map.
        round(number, decimal_place) uses two arguments.
    """
    circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
    result = list(map(round, circle_areas, range(1, 7)))
    print(result)


multiple_arguments()


def zipper():
    """
        Example of how we can zip together two lists, using zip()
        buil-in function.
    """
    my_strings = ['a', 'b', 'c', 'd', 'e']
    my_numbers = [1, 2, 3, 4, 5]
    results = list(zip(my_strings, my_numbers))
    print(results)


zipper()


def custom_zip():
    """
        Custom zip function, that works as built-in zip function
    """

    my_strings = ['a', 'b', 'c', 'd', 'e']
    my_numbers = [1, 2, 3, 4, 5]
    results = list(map(lambda x, y: (x, y), my_strings, my_numbers))
    print(results)


custom_zip()
