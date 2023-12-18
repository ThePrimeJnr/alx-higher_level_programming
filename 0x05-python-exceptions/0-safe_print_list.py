#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """A function that prints x elements of a list."""
    for i in range(x):
        try:
            print(my_list[i], end="")
        except IndexError:
            x = i
            break
    print()
    return x
