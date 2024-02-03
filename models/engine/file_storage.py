#!/usr/bin/python3
import json

class FileStorage:
    """
    FileStorage class for serializing instances to a JSON file
    and deserializing JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split('.')
                    module_name = "models." + class_name
                    class_ = globals()[class_name]
                    obj = class_(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
