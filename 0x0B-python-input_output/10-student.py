#!/usr/bin/python3
""" Module that defines the class Student """


class Student:
    """ repr student """

    def __init__(self, first_name, last_name, age):
        """ initialize new student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns directory description """
        objct = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return objct

            d_list = {}

            for iatr in range(len(attrs)):
                for satr in objct:
                    if attrs[iatr] == satr:
                        d_list[satr] = objct[satr]
            return d_list

        return objct
