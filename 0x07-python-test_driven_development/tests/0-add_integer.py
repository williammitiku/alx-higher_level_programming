#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float argument are typecasted to ints before addition is performed.

    Raises:
        TypeError: if either of a and b is a non-integer ans nob-float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result
