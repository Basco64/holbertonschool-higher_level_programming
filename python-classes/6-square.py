#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not self.__is_a_valid_position(position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

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
        else:
            self.__size = value

    @property
    def position(self):
        """Define the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if self.__is_a_valid_position(value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square"""
        if not self.size:
            print()
        else:
            for spaces_Y in range(self.position[1]):
                print()
            for row in range(self.size):
                for spaces_X in range(self.position[0]):
                    print(" ", end="")
                for row in range(self.size):
                    print("#", end="")
                print()

    def __is_a_valid_position(self, positions):
        """Checks that the square has a valid position"""
        if type(positions) is tuple\
                and len(positions) == 2\
                and type(positions[0]) is int and type(positions[1]) is int\
                and positions[0] >= 0 and positions[1] >= 0:
            return True
        else:
            return False
