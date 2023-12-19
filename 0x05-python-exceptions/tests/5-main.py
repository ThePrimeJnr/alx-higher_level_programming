#!/usr/bin/python3

import os
from sys import path

path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
print(path)
raise_exception = __import__("5-raise_exception").raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")