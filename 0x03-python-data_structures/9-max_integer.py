#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_num = my_list[0]
        for ser in range(len(my_list)):
            if my_list[ser] > max_num:
                max_num = my_list[ser]
        return max_num
