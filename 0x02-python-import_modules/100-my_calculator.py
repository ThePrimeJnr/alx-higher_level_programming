#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    if len(argv) != 4:
        print("usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(argv[1])
    b = int(argv[3])
    oper = str(argv[2])

    if oper == "+":
        print("{} {} {} = {}".format(a, oper, b, add(a, b)))
    elif oper == "-":
        print("{} {} {} = {}".format(a, oper, b, sub(a, b)))
    elif oper == "*":
        print("{} {} {} = {}".format(a, oper, b, div(a, b)))
    elif oper == "/":
        print("{} {} {} = {}".format(a, oper, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
