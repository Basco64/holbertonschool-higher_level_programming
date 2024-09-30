#!/usr/bin/python3

""" read file"""


def read_file(filename=""):
    """ read file"""
    with open(filename, "r") as my_file:
        print(my_file.read())
