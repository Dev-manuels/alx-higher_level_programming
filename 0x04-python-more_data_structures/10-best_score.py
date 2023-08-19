#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        large = -50
        for value in a_dictionary.values():
            if value >= large:
                large = value
        return large
    return None
