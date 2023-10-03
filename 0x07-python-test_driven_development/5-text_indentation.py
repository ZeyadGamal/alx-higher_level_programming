#!/usr/bin/python3
"""Define a module that prints a text indentation"""


def text_indentation(text):
    """print a text with two new lines

    Args:
        text (string): text to print
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    count = 0
    while count < len(text) and text[count] == '':
        count += 1
    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count += 1
            while count < len(text) and text[count] == '':
                count +=1
            continue
        count += 1
