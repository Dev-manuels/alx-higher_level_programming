#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None and key in a_dictionary:
        new_dict = dict()
        for keys, values in a_dictionary.items():
            if keys == key:
                new_dict.update({keys: value})
            else:
                new_dict.update({keys: values})
        return new_dict
    return a_dictionary
