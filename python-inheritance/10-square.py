#!/usr/bin/python3
"""base geometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """initialization method"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """calculate the area"""
        return self.__size ** 2
