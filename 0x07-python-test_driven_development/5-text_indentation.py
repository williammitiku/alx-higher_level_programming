#!/usr/bin/python3
"""Defin text indentation function.
"""


def text_indentation(text):
    """Return a splited text

    Args:
        text (str): Text that must be a string

    Raises:
        TypeError: if Text is not a
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for l in '.:?':
        text = text.replace(l, '{}\n'.format(l))
    lines = text.splitlines()
    for index, line in enumerate(lines):
        print(line.strip(), end='' if index == len(lines) - 1 else '\n\n')
