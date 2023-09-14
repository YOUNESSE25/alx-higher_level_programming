#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    for i in roman_string:
        if (i != 'I' and i != 'V' and i != 'X' and i != 'L'
                and i != 'C' and i != 'D' and i != 'M'):
            return 0
    dec = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    n = []
    for i in range(len(roman_string) - 1, - 1, - 1):
        if i == len(roman_string) - 1:
            largnum = dec[roman_string[i]]
        if dec[roman_string[i]] < largnum:
            n.append(largnum - dec[roman_string[i]])
            n.remove(largnum)
            largnum = dec[roman_string[i]]
        else:
            n.append(dec[roman_string[i]])
            largnum = dec[roman_string[i]]
    return sum(n)
