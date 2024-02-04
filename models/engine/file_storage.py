import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Class for serialization and deserialization of objects."""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serial_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serial_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                deserial_dict = json.load(file)
                for k, v in deserial_dict.items():
                    class_name, obj_id = k.split('.')
                    class_dict = {"BaseModel": BaseModel, "User": User}
                    obj = class_dict[class_name](**v)
                    FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass
