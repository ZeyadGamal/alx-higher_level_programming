#!/usr/include/python3
def subtract(list_number):
    sub = 0
    max_list = max(list_number)

    for num in list_number:
        if max_list > num:
            sub += num
    return (max_list - sub)


def roman_to_int(roman_string):
    if roman_string is None:
        return (0)
    if not isinstance(roman_string, str):
        return (0)
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    number = 0
    last = 0
    list_number = [0]
    for c in roman_string:
        for k in numerals:
            if c == k:
                if numerals.get(c) <= last:
                    number += subtract(list_number)
                    list_number = [numerals.get(c)]
                else:
                    list_number.append(numerals.get(c))
                last = numerals.get(c)
    number += subtract(list_number)

    return (number)
