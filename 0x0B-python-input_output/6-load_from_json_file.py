#!/usr/bin/python3
"""
Module containing a function that creates
an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """load_from_json_file
    creates an Object from a JSON file

    Args:
        filename (JSON file): file containing JSON string
        representing the python object to be created

    Returns:
        python object: the decoded python object from the JSON file
    """
    if len(filename) > 0:
        with open(filename, encoding="utf-8") as file:
            return json.loads(file.read())
