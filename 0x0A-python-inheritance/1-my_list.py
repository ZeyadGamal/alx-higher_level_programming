#!/usr/bin/python3
"""My list"""


class MyList(list):
    """Class that inherits list"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
