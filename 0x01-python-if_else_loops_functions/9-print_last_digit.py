#!/usr/bin/python3

def print_last_digit(number):
    absolute = abs(number) % 10
    if number < 0:
        absolute = -absolute
    print("{} ".format(absolute), end="")
