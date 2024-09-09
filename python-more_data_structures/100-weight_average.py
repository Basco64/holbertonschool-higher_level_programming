#!/usr/bin/python3

def weight_average(my_list=[]):

    if len(my_list) == 0:
        return 0

    first = 0
    second = 0

    for a, b in my_list:
        first += (a * b)
        second += b

    return (first / second)
