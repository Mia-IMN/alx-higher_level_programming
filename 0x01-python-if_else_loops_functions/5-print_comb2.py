#!/usr/bin/python3

# A program that prints numbers from 0 to 99

for i in range(100):
    if i < 99:
        print("{:02d}{} ".format(i, chr(44)), end="")
    else:
        print("{:02d}".format(i))
