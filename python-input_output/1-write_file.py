#!/usr/bin/python3

"""write file"""


def write_file(filename="", text=""):
    """write file"""
    with open(filename, 'w') as my_file:
        return my_file.write(text)
