#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if not my_list:
        return None

    my_list.pop(idx)
    return my_list
