import unittest
from datetime import datetime
from models.base_model import BaseModel, storage


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up method to create instances."""
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        self.obj3 = BaseModel(id="123", created_at="2023-01-01T00:00:00.000001",
                              updated_at="2023-01-01T00:00:00.000001", name="Test")

    def test_init(self):
        """Test initialization of BaseModel"""
        self.assertIsInstance(self.obj1.id, str)
        self.assertIsInstance(self.obj1.created_at, datetime)
        self.assertIsInstance(self.obj1.updated_at, datetime)

    def test_str(self):
        """Test string representation"""
        self.assertEqual(str(self.obj1), "[BaseModel] ({}) {}".format(self.obj1.id, self.obj1.__dict__))

    def test_save(self):
        """Test save method"""
        prev_updated_at = self.obj1.updated_at
        self.obj1.save()
        self.assertNotEqual(prev_updated_at, self.obj1.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        obj_dict = self.obj1.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.obj1.id)
        self.assertEqual(obj_dict['created_at'], self.obj1.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.obj1.updated_at.isoformat())

    def test_reload_from_dict(self):
        """Test reload_from_dict method"""
        obj_dict = self.obj1.to_dict()
        new_obj = BaseModel()
        new_obj.reload_from_dict(obj_dict)
        self.assertEqual(self.obj1.__dict__, new_obj.__dict__)


if __name__ == '__main__':
    unittest.main()
