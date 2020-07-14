"""
    As written in official Python tutorial, when file size is too big
    (>10Gb), then it's our problem to solve, if we want to read it.
    If 10Gb file is in one line, then we can't even read it using readline.

    So here comes handy this example, where it shows how to read large files
    in blocks.
    The idea is to use read method, that specifies fixed size of content
    to be read from the file.
"""

from functools import partial


def read_from_file(filename, block=1024 * 8):
    """
        Here partial() method is being used to optimize the code size.
    """
    with open(filename, "r") as fp:
        for chunk in iter(partial(fp.read, block), ""):
            yield chunk # returns generator


for i in read_from_file('README.md'):
    print(len(i))
