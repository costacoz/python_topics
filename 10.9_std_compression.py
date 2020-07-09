"""
    Example on zlib module usage
"""

import zlib

str = b'one two three four five six seven eight nine ten eleven twelve'
str += str

print(len(str))

zipped_str = zlib.compress(str)

print(len(zipped_str))

print(zlib.decompress(zipped_str))

print(zlib.crc32(str))
