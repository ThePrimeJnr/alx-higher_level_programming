#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    import calculator_1 as cal

    if len(argv) != 4:
        print("usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = str(argv[2])

    if operator == "+":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, cal.add(a, b)))
    elif operator == "-":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, cal.sub(a, b)))
    elif operator == "*":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, cal.mul(a, b)))
    elif operator == "/":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, cal.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
