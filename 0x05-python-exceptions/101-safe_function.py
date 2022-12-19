#!/usr/bin/python3

# A function that executes a function safely

def safe_function(fct, *args):
    try:
        return(fct(*args))
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
