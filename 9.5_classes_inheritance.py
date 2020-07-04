"""
    Example for classes inheritance
"""


class Human:
    def voice(self):
        print('I am a human')

    def shout(self):
        print('I AM A HUMAN!!!')


class Boy(Human):

    def shout(self):
        """
            Not just replacing base class method,
            but extending its functionality...
        """
        Human.shout(self)  # ... using this line
        print('I AM A BOY!!!')


g = Boy()

g.voice()
g.shout()

# Here should be !class!
print( issubclass(Boy, Human) )

# Here should be !object!
print( isinstance(g, Human) )