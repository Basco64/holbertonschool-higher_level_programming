#!/usr/bin/python3

"""append write"""


def append_write(filename="", text=""):
    """append write"""
    with open(filename, "a") as my_file:
        return my_file.write(text)
