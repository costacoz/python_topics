"""
    Example of glob module usage (shows files in currect directory
        using wildcards).
"""

import glob

# Print out list of file names from current directory, with *.py extension
print(f'Script files: {glob.glob("*.py")}')

print(f'Readme files: {glob.glob("*.md")}')
