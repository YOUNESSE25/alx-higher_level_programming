#!/usr/bin/python3
def uniq_add(my_list=[]):
    plus = 0
    for i in set(my_list):
        plus += i
    return plus
