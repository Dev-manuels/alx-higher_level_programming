#!/usr/bin/python3
"""
Module containing a function that writes
a python Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file
    function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj (python object): objects to be converted to JSON string
        filename (filename): file to wrte the equivalent of my_obj using JSON
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
