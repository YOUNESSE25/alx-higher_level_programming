#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(list_length):
        try:
            resl = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            resl = 0
        except (ZeroDivisionError):
            print("division by 0")
            resl = 0
        except (IndexError):
            print("out of range")
            resl = 0
        finally:
            n_list.append(resl)
    return n_list
