#!/usr/bin/python3

# Prints the numbers from 1 to 100 with successive words attached

def fizzbuzz():
    for first in range(1, 101):
        if first % 3 == 0 and first % 5 == 0:
            print("{} ".format("FizzBuzz"), end="")
        elif first % 3 == 0:
            print("{} ".format("Fizz"), end="")
        elif first % 5 == 0:
            print("{} ".format("Buzz"), end="")
        else:
            print("{} ".format(first), end="")
