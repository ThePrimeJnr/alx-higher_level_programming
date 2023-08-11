#!/usr/bin/python3

from sys import argv

length = len(argv)

if length == 1:
    print("0 argument.")
elif length == 2:
    print("{} arguments:".format(length - 1))
    print("1: {}".format(argv[1]))
else:
    print("{} arguments:".format(length - 1))
    for i in range(1, length):
        print("{}: {}".format(i, argv[i]))
