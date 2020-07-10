"""
    Beautiful example of templating batch file renamer.
    Why beautiful? Because it uses Template class and make renaming program
    to be versatile by choosing file format.
    Just read the code.

    If want to use placeholders spread around string, wrap them in {}, like:
    %{n}_MyName_%{d}_%f
"""

import time, os.path
from string import Template

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']


class BatchRename(Template):
    delimiter = '%'


fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))
