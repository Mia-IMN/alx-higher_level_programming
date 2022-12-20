#!/usr/bin/python3

"Define class called Square"


class Square:
    """ Defines a square by:
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
