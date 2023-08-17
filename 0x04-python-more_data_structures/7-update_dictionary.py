#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None and len(a_dictionary) > 0:
        tmp = dict([(key, value)])
        a_dictionary.update(tmp)
    return a_dictionary
