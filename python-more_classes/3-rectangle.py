#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Define a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Print the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        lines = []
        for _ in range(self.height):
            lines.append('#' * self.width)
        return '\n'.join(lines)

    def __repr__(self):
        """Represents the rectangle"""
        return "Rectangle(width={}, height={})".format(self.width, self.height)
