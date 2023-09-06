#!/usr/bin/python3
"""
Module text_indentation
"""


def text_indentation(text=None):
    """text_indentation: function that prints a text with 2 new
     lines after each of these characters: ., ? and :

    Args:
        text (str): text to be indented/printed. Defaults to None.

    Raises:
        TypeError: if text is not a valid string
    """
    if isinstance(text, str):
        for character in text:
            if character in ('.', '?', ':'):
                print(character + "\n\n", end="")
            else:
                print(character, end="")
    else:
        raise TypeError("text must be a string")
