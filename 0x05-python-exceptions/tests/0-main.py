#!/usr/bin/python3

import os
from sys import path

path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
print(path)
safe_print_list = __import__("0-safe_print_list").safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
