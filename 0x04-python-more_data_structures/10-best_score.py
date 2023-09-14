#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        max = list(a_dictionary.keys())[0]
        for k in a_dictionary:
            if a_dictionary[k] > a_dictionary[max]:
                max = k
        return max
    return None
