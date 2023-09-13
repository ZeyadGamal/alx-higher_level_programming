#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    res = 0

    for integer in uniq_list:
        res += integer

    return (res)
