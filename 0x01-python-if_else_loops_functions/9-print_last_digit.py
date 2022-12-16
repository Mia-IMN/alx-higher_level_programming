#!/usr/bin/python3

# Write a function that prints the last digit of a number.

def print_last_digit(number):
    absolute = abs(number) % 10
    print("{}".format(absolute), end="")
    return(absolute)
