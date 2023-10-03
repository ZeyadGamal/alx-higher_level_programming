#!/usr/bin/python3
"""Define a module print square"""


def print_square(size):
    """prints a square with character #

    Args:
        size (int): size length of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
