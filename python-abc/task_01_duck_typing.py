#!/usr/bin/python3

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """Shape class"""

    @abstractmethod
    def area(self):
        """area method"""
        pass

    @abstractmethod
    def perimeter(self):
        """perimeter method"""
        pass

class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        """initialization"""
        self.__radius = radius

    def area(self):
        """area method"""
        return pi * (self.__radius ** 2)

    def perimeter(self):
        """perimeter method"""
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        """initialization"""
        self.__width = width
        self.__height = height

    def area(self):
        """area method"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter method"""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """print methods result of the shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))


circle = Circle(5)
rectangle = Rectangle(4, 7)

shape_info(circle)
shape_info(rectangle)
