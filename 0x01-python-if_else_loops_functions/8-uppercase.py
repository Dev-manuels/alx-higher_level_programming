#!/usr/bin/python3
def uppercase(str):
    word = []
    for letter in str:
        if ord(letter) >= ord("a") and ord(letter) <= ord("z"):
            word.append(chr((ord(letter) - 32)))
        else:
            word.append(letter)
    string = "".join(word)
    print(string)
