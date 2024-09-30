#!/usr/bin/python3

"""load from json file"""


import json


def load_from_json_file(filename):
    """load from json file"""
    with open(filename, 'r') as my_file:
        return json.load(my_file)
