#!/usr/bin/python3

"""
This module contains a function for adding two integers.

The add_integer function takes two arguments, converts them to integers if necessary,
and returns their sum. If the arguments are not integers or floats,
a TypeError exception is thrown.

"""

def add_integer(a, b=98):

    """
    Adds two integers or floats and returns their sum.

    Args:
        a (int, float): The first number.
        b (int, float, optional): The second number, default 98.

    Returns:
        int: The sum of `a` and `b`, after conversion to integers.

    Raises:
        TypeError: If `a` or `b` are not integers or floats.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")

    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
