#!/usr/bin/python3
""" dds a new attribute to an object if its possible """


def add_attribute(obj, attribute, value):
    """ads a new attribute"""

    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    if '__slots__' in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
