"""
    Examples of filter() built-in function usage.

    filter() returns iterator.
    To get normal output for print, after filter() usage, need to use list()
"""


def is_number(a):
    return isinstance(a, int)


stash = ['ab', 5, ('1', 51), '11', 777]

print(list(filter(is_number, stash)))  # simple case of filter usage


def safe_to_int(a):
    try:
        return int(a)
    except:
        pass


# convert possible strings numbers to ints
print(list(filter(lambda x: is_number(safe_to_int(x)), stash)))
