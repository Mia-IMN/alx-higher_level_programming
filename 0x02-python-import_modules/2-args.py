#!/usr/bin/python3

# Program that prints out number of arguments followed by the argument passed

import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(len(sys.argv) - 1):
        print("{}: {}".format (i + 1, sys.argv[i + 1]))
