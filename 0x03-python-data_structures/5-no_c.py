#!/usr/bin/python3
def no_c(my_string):
    n = my_string.translate({ord('c'): None})
    n = n.translate({ord('C'):None})
    return n
