#!/usr/bin/python3

from sys import argv

result = 0
for i in range(1, len(argv)):
    result += int(argv[i])

print(result)
