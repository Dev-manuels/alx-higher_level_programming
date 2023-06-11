#!/usr/bin/python3
def no_c(my_string):
    if not (len(my_string) <= 0):
        new = ""
        for letter in my_string:
            if letter == "c" or letter == "C":
                continue
            new += letter
        return new
