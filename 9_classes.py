"""
    Example on how to use classes
"""

class Sample:
    def __init__(self, person, place):
        self.person = person
        self.place = place

    def show_info(self):
        print(f'{self.person} is located in {self.place}')


s = Sample('Grigory Kerensky', 'Bucharest')

represent_data = s.show_info

represent_data()

s.date = '04/08/20'
print(f'{repr(s.date)} is the object\'s date')

# Each value is an object and therefore has a class
print(s.__class__)
print(str('ok').__class__)
print(int(5).__class__)
print((5).__class__)
print((5, 5).__class__)
print({5, 5}.__class__)
print({'b': 5, 'a': 5}.__class__)
