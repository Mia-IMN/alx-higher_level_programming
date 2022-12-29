#!/usr/bin/python3

def max_integer(my_list=[]):
    max_num = 0
    for ser in my_list:
        if my_list[ser] > max_num:
            max_num = my_list[ser]
        return max_num
