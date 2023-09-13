#!/usr/bin/python3
"""
Module containing function inherits_from
checks that an object and a class are the same or share same superclasss
"""


def inherits_from(obj, a_class):
    """inherits_from
    checks that obj and a_class are same or share the same superclasss

    Args:
        obj (object)
        a_class (class):

    Returns:
        Boolean: True or False
    """
    return isinstance(type(obj), a_class)
