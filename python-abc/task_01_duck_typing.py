#!/usr/bin/python3

"""duck typing"""

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
        self.radius = radius

    def area(self):
        """area method"""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """perimeter method"""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        """initialization"""
        self.width = width
        self.height = height

    def area(self):
        """area method"""
        return self.width * self.height

    def perimeter(self):
        """perimeter method"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """print methods result of the shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
