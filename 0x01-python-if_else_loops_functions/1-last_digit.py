#!/usr/bin/python3

# A program that assigns random signed number to the variable number each time it is executed and then prints out the last digit while describing it

import random
number = random.randint(-10000, 10000)


def lNum(n):
    if n < 0:
        return(n % -10)
    else:
        return(n % 10)


def check(n):
    if n > 5:
        return("and is greater than 5")
    elif n < 6 and n != 0:
        return("and is less than 6 and not 0")
    else:
        return("and is 0")


print("Last digit of {} is {} ".format(number, lNum(number)) + check(number))
