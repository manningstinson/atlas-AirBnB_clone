import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_file_path(self):
        # Test if __file_path attribute exists
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))
        # Test if __file_path has the correct value
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        # Test if __objects attribute exists
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))
        # Test if __objects is a dictionary
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    class FileStorage:
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
            serialized_objs[f"{type(value).__name__}.{value.id}"] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                loaded_objs = json.load(f)
                print("Loaded objects:", loaded_objs)  # Debugging
                for key, value in loaded_objs.items():
                    class_name, obj_id = key.split('.')
                    cls = BaseModel
                    if class_name != 'BaseModel':
                        cls = eval(class_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()

