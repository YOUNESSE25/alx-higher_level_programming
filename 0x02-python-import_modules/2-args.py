#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    cont = len(sys.argv) - 1

    if cont == 0:
        print("{} argument.".format(cont))
    elif cont == 1:
        print("{} argument:".format(cont))
    else:
        print("{} arguments:".format(cont))

    if cont >= 1:
        cont = 0
        for arg in sys.argv:
            if cont != 0:
                print("{}: {}".format(cont, arg))
            cont += 1
