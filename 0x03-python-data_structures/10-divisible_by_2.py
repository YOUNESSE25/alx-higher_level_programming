#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        n = list(my_list)
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                n[i] = True
            else:
                n[i] = False
        return n
