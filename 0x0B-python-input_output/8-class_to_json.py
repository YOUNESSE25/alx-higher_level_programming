#!/usr/bin/python3
""" function that returns the dictionary description with a simple data
structure for a JSON serialization of an object """


def class_to_json(obj):
    """ function that retuns the dictionary description """

    r = {}
    if hasattr(obj, "__dict__"):
        r = obj.__dict__.copy()
    return r
