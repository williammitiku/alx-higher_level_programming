#!/usr/bin/python3
# 2-Rectangle.py
# Marta A
"""Define a Rectangle class."""


class Rectangle:
    """Represent rectangele."""

    def __init__(self, width=0, height=0):
        """Intialize a new Rectangle

        Args:
            width (int): the width of the new rectangle.
            height (int): the height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set current width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current Height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return: int area: height * Width. """
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__height + self.__width))
