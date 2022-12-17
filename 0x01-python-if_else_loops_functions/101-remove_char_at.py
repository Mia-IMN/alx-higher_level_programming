#!/usr/bin/python

# creates a copy of the string, rmoving the character at the position n

def remove_char_at(str, n):
    return(str[:n] + str[n+1:])
