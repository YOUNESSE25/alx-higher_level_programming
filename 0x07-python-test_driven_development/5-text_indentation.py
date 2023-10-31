#!/usr/bin/python3
"""Module composed by a function that prints a text with 2 new lines after each of these characters: ., ? """


def text_indentation(text):
    """ Function that prints a text with 2 new lines after each of these characters: ., ? """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = 0

    for d in text:
        if s == 0:
            if d == ' ':
                continue
            else:
                s = 1
        if s == 1:
            if d == '?' or d == '.' or d == ':':
                print(d)
                print()
                s = 0
            else:
                print(a, end="")