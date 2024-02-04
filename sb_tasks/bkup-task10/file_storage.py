#!/usr/bin/python3
"""
Module for FileStorage class
"""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    FileStorage class to serialize and deserialize instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists)
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                dict_loaded = json.load(file)
            for key, value in dict_loaded.items():
                class_name = value['__class__']
                obj = eval(class_name)(**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
