#!/usr/bin/python3

import os
from sys import path

path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
print(path)
safe_print_integer_err = __import__(
    "100-safe_print_integer_err").safe_print_integer_err

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
