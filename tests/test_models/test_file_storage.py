import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        # Ensure that storage is properly initialized
        self.storage.reload()
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        self.obj3 = BaseModel()
        self.storage.new(self.obj1)
        self.storage.new(self.obj2)
        self.storage.new(self.obj3)

    def tearDown(self):
        """Tear down test environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test all method."""
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 3)
        self.assertIn("BaseModel." + self.obj1.id, all_objs)
        self.assertIn("BaseModel." + self.obj2.id, all_objs)
        self.assertIn("BaseModel." + self.obj3.id, all_objs)

    def test_save_reload(self):
        """Test save and reload methods."""
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertEqual(len(all_objs), 3)
        self.assertIn("BaseModel." + self.obj1.id, all_objs)
        self.assertIn("BaseModel." + self.obj2.id, all_objs)
        self.assertIn("BaseModel." + self.obj3.id, all_objs)


if __name__ == '__main__':
    unittest.main()