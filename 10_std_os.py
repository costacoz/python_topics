"""
    This example script shows how to work with files and dirs using Python.
"""

import os  # this style better than using 'from os import *', because of open()
import shutil

print(f'Current dir: {os.getcwd()}')  # Return the current working dir

os.system('RMDIR /S/Q test-dir')  # Remove existing folder
os.mkdir('test-dir')  # Create folder

os.chdir('test-dir')
print(f'Current dir: {os.getcwd()}')

# help(os) -- returns module's __docstring__

# print(dir(os)) # returns a list of all module functions

# print(" shutil ".center(80, '*'))
# print(dir(shutil)) # returns a list of all module functions

# Check if file exists
if os.path.isfile('file'):
    os.remove('file')

open('file', 'a').close()  # Create file
os.mkdir('inner')

shutil.copyfile('file', 'inner/file')

os.chdir('inner')

shutil.move('file', '../file_done')
