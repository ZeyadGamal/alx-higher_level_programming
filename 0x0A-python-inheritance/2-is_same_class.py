#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly and instance of a_class

    Args:
        obj (any): object
        a_class (type): class
    """
    if type(obj) is a_class:
        return (True)
    return (False)
