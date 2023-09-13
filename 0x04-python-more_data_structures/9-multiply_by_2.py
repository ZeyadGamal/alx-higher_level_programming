#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_directory = a_dictionary.copy()
    for v in new_directory:
        new_directory[v] *= 2
    return (new_directory)
