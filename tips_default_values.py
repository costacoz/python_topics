"""
    If default value in function has mutable type, like list, object, etc.,
    then changes to that object will be saved throughout execution.

    Pythons default arguments to functions are evaluated at compile time,
    not runtime!

    If default value is mutable, such as a list, appending to the list in
    the function will always be appending to the same default list.
"""


def bad_default(new_value, other=['other']):
    """
        Bad approach:
            the value of "other" will be mutated and saved throughout execution
            and it will become bug that is hard to find.
            Because other is an object.
    """
    other.append(new_value)
    print(other)


bad_default('A')
bad_default('B')  # notice, how bad_default still includes 'A'


def good_default(new_value, other=None):
    """
        Good approach:
            1) firstly assign None to default value;
            2) if no value supplied, then assign desired real default value.
    """
    if other == None:
        other = ['other']
    other.append(new_value)
    print(other)


good_default('A')
good_default('B')
