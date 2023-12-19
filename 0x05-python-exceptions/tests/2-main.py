#!/usr/bin/python3

import os
from sys import path

path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
print(path)
safe_print_list_integers = __import__(
    "2-safe_print_list_integers"
).safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
