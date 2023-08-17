#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        tmp = dict([(key, value)])
        a_dictionary.update(tmp)
    return a_dictionary
