#!/usr/bin/python3

"""Student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """represents the student #sisi"""
        if not isinstance(attrs, list):
            return self.__dict__

        filtered_dict = {}

        for key, value in self.__dict__.items():
            if key in attrs and isinstance(key, str):
                filtered_dict[key] = value

        return filtered_dict
