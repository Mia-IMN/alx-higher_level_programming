#!/usr/bin/python3

# Function that prints x elements of a list

def safe_print_list(my_list=[], x=0):
    serial = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        else:
            serial += 1

    print()
    return(serial)
