#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size: size of square
            position: position
        """
        self.size = size
        self.position = position

    def area(self):
        """Returns area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """set pos"""
        if (not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
                or not all(num > 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    @size.setter
    def size(self, value):
        """set size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        if self.size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(self.size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
