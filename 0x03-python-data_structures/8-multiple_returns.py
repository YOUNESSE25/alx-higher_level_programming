#!/usr/bin/python3
def multiple_returns(sentence):
    lgt = len(sentence)
    if lgt == 0:
        r = (0, None)
        return r
    else:
        r = (lgt, sentence[0:1])
        return r
