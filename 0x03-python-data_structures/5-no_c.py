#!/usr/bin/python3
def no_c(my_string):
    if len(my_string) > 0:
        new_string = ""
        for letter in my_string:
            if letter != "c" and letter != "C":
                new_string += letter
        return new_string
