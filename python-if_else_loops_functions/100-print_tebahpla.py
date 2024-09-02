#!/usr/bin/python3
for letter in range(122, 96, -2):
    print(f"{chr(letter)}{chr((letter - 1) - 32)}", end="")
