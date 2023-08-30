#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    # *args - made me remember pointers in C
    try:
        fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
