#!/usr/bin/python3
"""Square class"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Initialize the square"""
        self.size = size

    @property
    def size(self):
        """Define the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
