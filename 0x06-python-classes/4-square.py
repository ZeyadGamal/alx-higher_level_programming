#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Square"""

    def __init__(self, size=0):
        """Initializes a square

        Args:
            size (int): size of square
        """
        self.size = size

    @property
    def size(self):
        """Retrive size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set size of square

        Args:
            value (int): size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of square"""
        return (self.__size * self.__size)
