#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square"""

    def area(self):
        """Returns area of square"""
        return self.__size * self.__size

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: size of square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
