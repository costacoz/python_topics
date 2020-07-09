"""
    Example shows how to work with datetime module of Python
"""

from datetime import date

now = date.today()

print(f'{repr(now)}')
print(now)

str_now = now.strftime("%d-%m-%y means that today is %A of %Y the %B")

print(str_now)

birthday = date(1994, 3, 31)
age = now - birthday
print(f'My age is: {age.days / 365}')
