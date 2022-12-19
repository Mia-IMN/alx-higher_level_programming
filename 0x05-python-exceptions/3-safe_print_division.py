#!/usr/bin/python3

# Function that divides 2 integers and prints the result

def safe_print_division(a, b):
    try:
        print("Inside result: {}".format(a / b))
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        if b > 0:
            return(a / b)
        else:
            return(None)
