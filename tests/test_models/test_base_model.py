import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """Test initialization of BaseModel"""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        """Test string representation"""
        obj = BaseModel()
        self.assertEqual(str(obj), "[BaseModel] ({}) {}".format(obj.id, obj.__dict__))

    def test_save(self):
        """Test save method"""
        obj = BaseModel()
        prev_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(prev_updated_at, obj.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
