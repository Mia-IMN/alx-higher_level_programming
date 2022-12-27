#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if len(my_list) != 0:
        length = len(my_list)
        for i in reversed(range(length)):
            print("{:d}".format(my_list[i]))
