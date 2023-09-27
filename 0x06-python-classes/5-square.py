#!/usr/bin/python3
"""class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """class Square that defines a square by: (based on 4-square.py)"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """fn that prints in stdout the square with the character #"""

        if self.__size != 0:
            for n in range(self.__size):
                for m in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
