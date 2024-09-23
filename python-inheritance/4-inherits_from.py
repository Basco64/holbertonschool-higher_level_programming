#!/usr/bin/python3
"""inherits from"""

def inherits_from(obj, a_class):
    """inherits from"""

    if typeof(obj) == a_class:
        return False
    return issubclass(typeof(obj), a_class)
