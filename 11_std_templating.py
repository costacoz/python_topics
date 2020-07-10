"""
    Example on string templating, string module's Template class usage
"""

from string import Template

message = Template(
    'There are $covid_cases in ${country}stan. Please pay $$10 for this info.')

data = dict(covid_cases=207, country='Germany')

print(message.substitute(data))

data2 = dict(covid_cases=1000000)

# safe_substitute allows omit required data and avoid KeyError
print(message.safe_substitute(data2))
