#!/usr/bin/python3
"""
Module containing function is_kind_of_class
checks that an object and a class are the same or share same superclasss
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class
    checks that obj and a_class are same or share the same superclasss

    Args:
        obj (object)
        a_class (class):

    Returns:
        Boolean: True or False
    """
    return isinstance(obj, a_class)
