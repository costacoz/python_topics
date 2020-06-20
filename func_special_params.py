"""
    This example demonstrates how to use special characters that
    define type of arguments for a function: whether it
        1. strictly positional argument
        2. positional/keyword argument
        3. strictly keyword argument

"""


def call_dogs(whistle_type, /, dog_name):
    print('Using {0} whistle, John called dog named: {1}'.format(whistle_type, dog_name))


def call_cats(voice_type, /, *cat_names):
    """
    :param voice_type: Positional argument
    :param cat_names: Positional formal argument
    :return: None
    """
    print('Using {0} voice, Peter called cats:'.format(voice_type))
    for idx, cat in enumerate(cat_names):
        print('{0}. {1}'.format(idx, cat))


def call_birds(*, place):
    print('Steven called birds at {0}'.format(place))


def call_frogs(*, urgency):
    print('frogs called, status: {0}'.format(urgency))


call_dogs('melodic', 'Rex')
call_cats('gentle', 'Lumpy', 'Frowny', 'Jolly')
call_birds(place='stadium')
call_frogs(urgency='highly urgent')
