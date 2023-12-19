#!/usr/bin/python3

import os
from sys import path

path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
print(path)
safe_print_division = __import__("3-safe_print_division").safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
