"""
    This example shows how to create and use function with:
        1.  required positional parameter;
        2.  formal positional parameter;
        3.  keyword parameter with default value;
        4.  final formal parameter (with keywords), dic type

"""


def show_args(first, *optional, nationality='american', **others):
    """
    Function that takes required argument, formal parameter and final formal parameter.
    :param first: required positional parameter.
    :param optional: formal positional parameter. Everything that goes after required and keyword parameter.
    :param nationality: keyword parameter with default value.
    :param others: final formal parameter, dic type.
    :return: None
    """

    print('first parameter is: {}'.format(first))
    print('nationality is: {}'.format(nationality))
    for idx, o in enumerate(optional):
        print('optional parameter #{0}: {1}'.format(idx, o))
    for idx, o in enumerate(others):
        print('additional set of descriptions #{0}: {1} - {2}'.format(idx, o, others[o]))


# Notice how nationality goes into nationality parameter, but the rest goes to **others parameter.
show_args('John', 'United States', 'Bronx', nationality='spanish', style='rocker', age=27)
