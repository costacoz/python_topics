"""
    Decorators extends functions capabilities.

    Here are 2 examples of decorators usage:
    1) With argument
    2) Without argument
"""


def repeater(number):
    def function_generator(decorated_function):
        """
            Function generator that wraps result function.
        """

        def extended_func(*args, **kwargs):
            """
                The result function, that wraps decorated function.
            """
            return number * decorated_function(*args, **kwargs)

        return extended_func

    return function_generator


@repeater(number=7)  # decorator with argument
def function(num1, num2):
    return num1 * num2


print(f'decorator with argument, decorated function with argument: '
      f'{function(2, 5)}')

"""
    Example of decorator without argument. Decorated function without argument.
"""


def multiply_by_two(decorated_function):
    def extended_function():
        return decorated_function() * 2

    return extended_function


@multiply_by_two
def get_number_five():
    return 5


print(f'decorator without argument, decorated function without argument: '
      f'{get_number_five()}')

"""
    Example of decorator without argument. Decorated function with argument.
"""


def add_nine(decorated_function):
    def extended_function(*args, **kwargs):
        return decorated_function(*args, **kwargs) + 9

    return extended_function


@add_nine
def sum_nums(x, y):
    return x + y


print(f'decorator without argument, decorated function with argument: '
      f'{sum_nums(3, 4)}')
