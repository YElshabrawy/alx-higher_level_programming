#!/usr/bin/python3
"""module"""


def is_kind_of_class(obj, a_class):
    """checks if object is an instance of the specified class or its parents"""
    return isinstance(obj, a_class)
