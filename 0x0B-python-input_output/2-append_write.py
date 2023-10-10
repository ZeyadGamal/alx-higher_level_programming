#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """appends a string at the end of text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
