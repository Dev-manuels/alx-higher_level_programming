#!/usr/bin/python3
def remove_char_at(str, n):
    string = []
    j = 0
    for letter in str:
        if j != n:
            string.append(letter)
        j += 1
