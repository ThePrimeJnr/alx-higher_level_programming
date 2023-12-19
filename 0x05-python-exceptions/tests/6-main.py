#!/usr/bin/python3

import os
from sys import path

path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
print(path)
raise_exception_msg = __import__("6-raise_exception_msg").raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
