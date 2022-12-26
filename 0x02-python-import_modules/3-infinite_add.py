#!/usr/bin/python3

# A program that prints the result of the addition of all arguments

import sys


if __name__ == '__main__':
    result = 0
    for i in sys.argv[1:]:
        result += int(i)
    print("{:d}".format(result))
