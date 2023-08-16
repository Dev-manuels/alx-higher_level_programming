#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    if my_string is not None and len(my_string) > 0:
        for letter in my_string:
            if letter != "c" and letter != "C":
                new_string += letter
        return new_string
    return new_string
