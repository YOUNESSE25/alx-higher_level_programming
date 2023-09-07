#!/usr/bin/python3
import sys
if __name__ != "__main__":
    exit()

argc = len(sys.argv) - 1

c = 0
r = 0
for arg in sys.argv:
    if c != 0:
        r += int(arg)
    else:
        c += 1
print("{:d}".format(r))
