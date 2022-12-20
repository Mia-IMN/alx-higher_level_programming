#!/usr/bin/python3

"Define a class Square"


class Square:
    """ Define a Square class by
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0)
    Public instance method: def area(self)"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return(self.__size * self.__size)
