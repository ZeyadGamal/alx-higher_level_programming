#!/usr/bin/python3
def remove_char_at(str, n):
    newString = ""
    i = 0
    for c in str:
        if i == n:
            i += 1
            continue
        i += 1
        newString += c
    return (newString)
