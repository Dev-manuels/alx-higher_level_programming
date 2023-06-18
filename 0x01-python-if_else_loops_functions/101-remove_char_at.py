#!/usr/bin/python3
def remove_char_at(str, n):
    if str is not None:
        new_str = ""
        for i, letter in enumerate(str):
            if i != n:
                new_str += letter
        return new_str
