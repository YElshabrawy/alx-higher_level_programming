#!/usr/bin/python3
"""Add func module"""


def add_integer(a, b=98):
    """Adds 2 int or float values, return int"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
