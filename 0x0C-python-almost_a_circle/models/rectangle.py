#!/usr/bin/python3
""" rect module """
from models.base import Base


class Rectangle(Base):
    """ rect class """

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if val > 0:
            self.__width = val
        else:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if val > 0:
            self.__height = val
        else:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
