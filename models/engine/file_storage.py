import json


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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as file:
            obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            print("Saving objects:", obj_dict)  # Debugging print statement
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if the JSON file exists)
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                print("Loaded objects:", obj_dict)  # Debugging print statement
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    cls = eval(cls_name)
                    new_obj = cls(**value)
                    FileStorage.__objects[key] = new_obj
        except FileNotFoundError:
            pass  # Handle the case where the file does not exist gracefully
