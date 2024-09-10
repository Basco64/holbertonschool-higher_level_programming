#!/usr/bin/python3
"""Defines text_indentation function."""


def text_indentation(text):

    """
    Prints a text with 2 newlines after: '.', '?' and ':'

    @text: The text to print.

    Return: Nothing
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    specChar = {".", "?", ":"}
    start = 0

    for end in range(len(text)):
        if text[end] in specChar:
            line = text[start:end + 1] + "\n\n"
            start = end + 1
            print("{}".format(line.strip(" ")), end="")

    if start < len(text):
        print("{}".format(text[start:].strip()), end="")
