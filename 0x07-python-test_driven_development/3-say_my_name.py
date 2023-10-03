#!/usr/bin/python3
# 3-say_my_name.py
"""Defines a module that prints a name"""

def say_my_name(first_name, last_name=""):
    """Print a name

    Args:
        first_name (str): first name
        last_name (str): last name

    """
    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last name must be a string")
    print("My name is {} {}".format(first_name, last_name))
