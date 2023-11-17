#!/usr/bin/python3
""" base class """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """from dict to json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string to a file"""
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

            with open("{}.json".format(cls.__name__), 'w') as f:
                f.write(cls.to_json_string(list_dicts))
