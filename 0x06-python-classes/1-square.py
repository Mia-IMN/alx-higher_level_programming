#!/usr/bin/python3

"Define class Square"


class Square:
    """Defines a square by size
    -Private instance attribute: size
    -Instantiation with size (no type/value verification)"""
    def __init__(self, size):
        self.__size = size
