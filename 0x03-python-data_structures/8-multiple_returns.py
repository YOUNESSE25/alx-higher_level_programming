#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        r = (0, None)
        return r
    else:
        r = (l, sentence[0:1])
        return r
