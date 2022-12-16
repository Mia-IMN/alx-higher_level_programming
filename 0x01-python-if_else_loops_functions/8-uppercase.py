#!/usr/bin/python3

# Write a function that prints a string in uppercase followed by a new line

def uppercase(str):
    for i in str:
        l = ord(i)
        if l > 96 and l < 123:
            l -= 32
        print("{}".format(chr(l)), end="")
    print(" ")

