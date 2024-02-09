import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objs = {}
        for key, value in self.__objects.items():
            serialized_objs[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                loaded_objs = json.load(f)
                for key, value in loaded_objs.items():
                    class_name, obj_id = key.split('.')
                    cls = BaseModel
                    if class_name != 'BaseModel':
                        cls = eval(class_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
