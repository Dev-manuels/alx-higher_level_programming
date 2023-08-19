#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) > 0:
        large = 0
        b_key = ""
        for key, value in a_dictionary.items():
            if value >= large:
                large = value
                b_key = key
        return b_key
    return None
