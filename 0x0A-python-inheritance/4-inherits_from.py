#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """Returns True if object is an instance of a class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
