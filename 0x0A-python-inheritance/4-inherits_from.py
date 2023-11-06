#!/usr/bin/python3
"""module only sub class of"""


def inherits_from(obj, a_class):
    """returns True or False."""
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
