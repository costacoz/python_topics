"""
    Example for :
        1) sys.argv, which returns arguments from execution;
        2) argparse, allows broader functionality to work with arguments
        more: https://docs.python.org/3/library/argparse.html#module-argparse
"""

import sys, argparse

print(sys.argv)

parser = argparse.ArgumentParser(prog='hm')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', type=int, default=7)
args = parser.parse_args()
print(args)
print(args.l)
print(args.filenames)
