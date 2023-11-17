#!/usr/bin/python3
"""mylist module"""


class MyList(list):
    """mylist class"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
