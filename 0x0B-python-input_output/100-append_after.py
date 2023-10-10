#!/usr/bin/python3
"""Search and Update"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line to a file, after each line containing a string"""
    line = ""
    with open(filename) as f:
        for curr_line in f:
            line += curr_line
            if search_string in curr_line:
                line += new_string
    with open(filename, "w") as w:
        w.write(line)
