#!/usr/bin/python3

"""Module for adding integers.

Contains the add_integer function
function, which adds two
numbers after converting them to integers."""


def add_integer(a, b=98):

    """Adds two numbers after conversion to integers
    a: First number.
    b: Second number."""

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")

    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
