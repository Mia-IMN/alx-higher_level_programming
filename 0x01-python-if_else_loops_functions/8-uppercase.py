#!/usr/bin/python3

# Write a function that prints a string in uppercase followed by a new line

def uppercase(str):
    for i in range(len(str)):
# could also be "for i in str"
        input = ord(str[i])
# If the above commented method is preferred then this code would be "input = ord(i)"
        if input > 96 and input < 123:
            input -= 32
        print("{}".format(chr(input)), end="")
    print("")
