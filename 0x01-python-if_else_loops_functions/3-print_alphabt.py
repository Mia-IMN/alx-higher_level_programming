#!/usr/bin/python3

# A program that prints the ASCII alphabet, except e and q, in lowercase, followed by a new line

for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")
