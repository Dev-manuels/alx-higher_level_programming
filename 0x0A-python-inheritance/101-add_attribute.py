#!/usr/bin/python3
"""
Module containing function add_attribute
"""


def add_attribute(obj, name, value):
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add a new attribute")
    else:
        setattr(obj, name, value)
