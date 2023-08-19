#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if len(a_dictionary) > 0:
        a_dictionary.update({key: value})
    return a_dictionary
