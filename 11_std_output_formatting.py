import reprlib

# Displays large or deeply nested containers in abbreviated format
print(reprlib.repr(set('transponder')))



import textwrap

doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

# Inserts newlines for formatting
print(textwrap.fill(doc, width=40))
print('\n')

# makes list of strings, at positions of newlines in original text
print(textwrap.wrap(doc))