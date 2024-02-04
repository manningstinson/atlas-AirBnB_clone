#!/usr/bin/python3
"""
Unit tests for BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """
    def setUp(self):
        """
        Set up method to create an
        instance of BaseModel
        """
        self.my_model = BaseModel()

    def test_attributes(self):
        """
        Test the attributes
        of BaseModel instance
        """
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

    def test_str_method(self):
        """
        Test the __str__ method
        of BaseModel
        """
        expected_str = "[BaseModel] ({}) {}".format(
            self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_str)

    def test_save_method(self):
        """
        Test the save method of BaseModel
        """
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(old_updated_at, self.my_model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of BaseModel
        """
        my_model_dict = self.my_model.to_dict()
        self.assertTrue('__class__' in my_model_dict)
        self.assertTrue('id' in my_model_dict)
        self.assertTrue('created_at' in my_model_dict)
        self.assertTrue('updated_at' in my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
