#!/usr/bin/python3

# A function that outputs a string in uppercase followed by a new line

def uppercase(str):
    for i in str:
        string = ord(i)
        if l > 96 and l < 123:
            string -= 32
        print("{}".format(chr(l)), end="")
    print("")

