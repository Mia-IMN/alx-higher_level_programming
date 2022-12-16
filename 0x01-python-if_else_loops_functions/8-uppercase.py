#!/usr/bin/python3

# Write a function that prints a string in uppercase followed by a new line

def uppercase(str):
    for i in range(len(str)):
        input = ord(str[i])
        if input > 96 and input < 123:
            input -= 32
        print("{}".format(chr(input)), end="")
    print("")
