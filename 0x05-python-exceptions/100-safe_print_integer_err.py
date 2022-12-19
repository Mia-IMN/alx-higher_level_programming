#!/usr/bin/python3

# A function that prints an integer

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False
    else:
        return True
