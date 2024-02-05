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

    def test_save_reload(self):
        # Create a BaseModel instance
        model = BaseModel()
        model.name = "Test Model"
        model.save()

        # Reload storage
        new_storage = FileStorage()
        new_storage.reload()

        # Check if the saved object exists in the reloaded storage
        self.assertIn(f"BaseModel.{model.id}", new_storage.all())

        # Check if the attributes are correctly saved and loaded
        loaded_model = new_storage.all()[f"BaseModel.{model.id}"]
        self.assertEqual(loaded_model.name, "Test Model")

if __name__ == '__main__':
    unittest.main()
