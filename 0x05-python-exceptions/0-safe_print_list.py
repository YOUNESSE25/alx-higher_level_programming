#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cont = 0
    for n in range(x):
        try:
            print(my_list[n], end="")
            cont = cont + 1
        except IndexError:
            break
    print()
    return cont
