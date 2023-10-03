#!/usr/bin/python3
"""Define a module to find max int"""


def max_integer(list=[]):
    """find and return max integer"""
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i+= 1
    return (result)
