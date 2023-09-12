#!/usr/bin/python3
def multiple_returns(sentence):
    longg = len(sentence)
    if longg == 0:
        r = (0, None)
        return r
    else:
        r = (longg, sentence[0:1])
        return r
