#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_ks = []
    for k in a_dictionary:
        if a_dictionary[k] == value:
            del_ks.append(k)
    for k in del_ks:
        del a_dictionary[k]
    return a_dictionary
