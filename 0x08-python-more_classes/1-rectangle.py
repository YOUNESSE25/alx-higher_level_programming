#!/usr/bin/python3
""" empty class Rectangle"""


class Rectangle:
    """ representation rectangle"""
    def __init__(self, width=0, height=0):
        """ Instantiation rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """private instance width"""
        return self.__width

    @property
    def height(self):
        """private instance height"""
        return self.__height
    @width.setter

    def width(self, value):
        """setter for the private attribue width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    @height.setter
    def height(self, value):
        """setter for the private attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
