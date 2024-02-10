#!/usr/bin/python3

"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    FileStorage class
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
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        odict = FileStorage.__objects
        objdict = {key: obj.to_dict() for key, obj in odict.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(objdict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if the JSON file exists)
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                objdict = json.load(file)
                for key, value in objdict.items():
                    cls_name, obj_id = key.split('.')
                    cls = eval(cls_name)
                    new_obj = cls(**value)
                    FileStorage.__objects[key] = new_obj
        except FileNotFoundError:
            pass  # Handle the case where the file does not exist gracefully
