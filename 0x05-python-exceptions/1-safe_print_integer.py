#!/usr/bin/python3

# Function that prints an integer with "{:d}".format()

def safe_print_integer(value):
    isInt = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        isInt = False
    if isInt:
        return True
    else:
        return False
