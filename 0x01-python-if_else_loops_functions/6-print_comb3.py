#!/usr/bin/python3

# A program that prints all possible different combinations of two digits

for tens in range(10):
    for units in range(tens + 1, 10):
        if tens == 8 and units == 9:
            print("{}{}".format(tens, units))
        else:
            print("{}{}{} ".format(tens, units, chr(44)), end="")
