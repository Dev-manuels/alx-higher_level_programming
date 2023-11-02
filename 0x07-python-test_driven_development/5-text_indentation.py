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
        i = 0
        while i < len(text):
            if text[i] == ' ' and text[i + 1] in ('.', '?', ':'):
                i += 1
                print(text[i] + "\n\n", end="")
                try:
                    if text[i + 1] == ' ':
                        i = i + 1
                except IndexError:
                    pass
            elif text[i] in ('.', '?', ':'):
                print(text[i] + "\n\n", end="")
                try:
                    if text[i + 1] == ' ':
                        while (text[i + 1] == " "):
                            i += 1
                except IndexError:
                    pass
            else:
                print(text[i], end="")
            i += 1
    else:
        raise TypeError("text must be a string")
