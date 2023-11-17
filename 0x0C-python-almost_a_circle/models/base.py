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

    @staticmethod
    def from_json_string(json_string):
        """from json to dict"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string to a file"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]

        with open("{}.json".format(cls.__name__), 'w') as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """from dict to obj"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            obj = Rectangle(1, 1)
        elif cls is Square:
            obj = Square(1)
        else:
            obj = None

        obj.update(**dictionary)
        return obj
