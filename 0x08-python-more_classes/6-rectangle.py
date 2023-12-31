#!/usr/bin/python3
""" defines a class rectangle"""


class Rectangle:
    """ repres rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Instantiation"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """ Rectangle deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """ get width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns rectangle perimiter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ return the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))

    def __repr__(self):
        """ return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
