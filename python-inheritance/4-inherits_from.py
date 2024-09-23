#!/usr/bin/python3
"""inherits from"""

def inherits_from(obj, a_class):
    """inherits from"""

    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
