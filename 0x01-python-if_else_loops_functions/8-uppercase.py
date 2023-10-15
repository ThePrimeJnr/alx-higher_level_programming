#!/usr/bin/python3

def uppercase(str):
    result = "".join(
        chr(ord(i) - 32) if ord('a') <= ord(i) <= ord('z') else i for i in str
    )
    print(f"{result}")
