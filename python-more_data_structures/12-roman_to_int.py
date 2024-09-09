#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0

    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0

    for i in range(len(roman_string)):
        value = digits[roman_string[i]]

        if i < len(roman_string) - 1 and digits[roman_string[i + 1]] > value:
            total -= value
        else:
            total += value

    return total
