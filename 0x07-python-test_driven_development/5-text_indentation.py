#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text indentation function."""


def text_indentation(text):
    """Print text with 2 new lines after ., ?, and : characters.

    Args:
        text (str): The input text.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    flag = True  # To handle cases where consecutive separators appear
    for char in text:
        if char in [".", "?", ":"]:
            new_text += char + "\n\n"
            flag = True
        else:
            if char == " " and flag:
                continue
            new_text += char
            flag = False

    print(new_text, end="")
