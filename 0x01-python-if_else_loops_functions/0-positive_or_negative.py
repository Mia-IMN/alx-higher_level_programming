#!/usr/bin/python3

# Assigns random number and prints out the number while saying if it's negative, positive or zero

import random
number = random.randint(-10, 10)
if number < 0:
    print("{} is negative".format(number))
elif number > 0:
    print("{} is positive".format(number))
else:
    print("{} is zero".format(number))
