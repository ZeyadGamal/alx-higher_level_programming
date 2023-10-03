#!/usr/bin/python3
"""Defines an integer addition"""


def add_integer(a, b=98):
    """Return a + b

    Raises:
        TypeError: if either a or b is non-integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
