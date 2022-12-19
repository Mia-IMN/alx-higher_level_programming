B0;10;1c#!/usr/bin/python3

# A function that executes a function safely

def safe_function(fct, *args):
    try:
        result = (fct(*args))
        return result
    except Exception as error: 
        import sys
        print("Exception: {}".format(error), file = sys.stderr)
        return None
