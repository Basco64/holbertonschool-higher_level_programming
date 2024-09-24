#!/usr/bin/python3
"""base geometry"""


class BaseGeometry:
    """base geometry"""

    def area(self):
        """exception if area is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """is an integer?"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """ Rectangle"""

    def __init__(self, width, height):
        """initialization method"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """print"""
        return "[{}] {}/{}".format(__class__.__name__,
                                   self.__width, self.__height)

    def area(self):
        """calculate the area"""
        return self.__width * self.__height


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """initialization method"""
        self.integer_validator('size', size):
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculate the area"""
        return super().area()
