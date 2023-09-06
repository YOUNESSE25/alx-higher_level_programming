#!/usr/bin/python3

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

def uppercase(str):
    for sh in str:
        print("{:c}"
                .format(ord(sh) if not islower(sh) else ord(sh) - 32),
                end="")
    print("")
