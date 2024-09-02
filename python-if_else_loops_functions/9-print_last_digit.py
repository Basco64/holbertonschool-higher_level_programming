#!/usr/bin/python3
def print_last_digit(num):
    lastDigit = abs(num) % 10
    print(lastDigit, end="")
    return lastDigit
