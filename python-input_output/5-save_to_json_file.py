#!/usr/bin/python3

"""save to json file"""


import json


def save_to_json_file(my_obj, filename):
    """from json string"""
    with open(filename, 'w') as my_file:
        json.dump(my_obj, my_file)
