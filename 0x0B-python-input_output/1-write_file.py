#!/usr/bin/python3
"""Write to file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns number of chars"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
