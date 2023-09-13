#!/usr/bin/python3
"""
Module containing function is_same_class
checks that an object and a class are same
"""


def is_same_class(obj, a_class):
    return (type(obj) is a_class)
