#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """square"""

    @property
    def size(self):
        """retrives size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size):
        """initializes a square

        Args:
            size (int): size of square
        """
        self.size = size

    def area(self):
        """return area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints square"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
