#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Defines a new rectangle"""

    def __init__(self, width=0, height=0):
        width = width
        height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.width = val

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.height = val
